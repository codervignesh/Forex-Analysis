from report import generateReport
import pandas as pd #data frames
import numpy as np #calculations
import yfinance as yf #data set
import warnings # to remove warnings
from datetime import datetime 
import argparse, textwrap
import charts

def fetchLongData(currency):
    return yf.Ticker(currency)

def fetch10YData(currency):
    return yf.download(currency, start="2010-01-01")

def regressionModel(df):
    # df.reset_index(inplace = True)
    # df.ffill(inplace = True)
    # regDf = df.copy()
    # regDf = regDf[['Adj Close']]
    # predict_days = 7
    # regDf['Prediction'] = regDf[['Adj Close']].shift(-predict_days)

    # x = np.array(regDf.drop(['Prediction'], 1)) #Takes only Adj Close
    # x = x[:-predict_days]
    # y = np.array(regDf['Prediction']) # takes Prediction
    # y = y[:-predict_days]

    df.reset_index(inplace = True)
    df = df.loc[(df.Date >= '2021-01-01')]

    df.ffill(inplace = True)

    df['Date'] = pd.to_datetime(df['Date'], origin='unix') - pd.datetime(2021,1,1)
    df['DATE'] = df['Date'].dt.days.astype(int)
    #df.iloc[:,-1]

    x = df.iloc[:,-1] #DATE
    y = df.iloc[:,4]  #close
    x = list(x)
    y = list(y)

    X_mean = np.nanmean(x) #Actual Price
    Y_mean = np.nanmean(y) #Shifted Price
    num = 0
    den = 0
    for i in range(len(x)):
        num += (x[i] - X_mean)*(y[i] - Y_mean)
        den += (x[i] - X_mean)**2 # Square Value
    m = num / den
    c = Y_mean - m*X_mean
    print("M = "+str(m))
    print("C = "+str(c))
    datelist, xPred = findForecast(m,c,x,y)
    return datelist,xPred,m,c

def findForecast(m,c,x,y):
    #x_forecast = np.array(regDf.drop(['Prediction'],1))[-predict_days:]

    x_forecast = []
    final = int(x[-1])

    for i in range(7):
        x_forecast.append(final+i)

    xPred = [(final+q)*m+c for q in range(7)] #predicted value
    #xPred.reverse()
    # for abc in x_forecast:
    #     v = float(abc*m+c)
    #     xPred.append(v)

    se = 0
    xTarget = [(final-q)*m+c for q in range(7)] #actual value
    
    y = y[-7:]  

    for i in range(7):      
        se += (xTarget[i] - y[i])**2
    mse = se/7
    rmse = np.sqrt(mse)
    print("rmse = " + str(rmse))

    datelist = pd.date_range(datetime.today(), periods=100).tolist()
    return datelist, xPred

if __name__ == '__main__':
    warnings.filterwarnings("ignore", category=FutureWarning)
    pd.options.mode.chained_assignment = None  # removes other warnings
    my_parser = argparse.ArgumentParser(allow_abbrev=False, formatter_class=argparse.RawTextHelpFormatter)

    my_parser.add_argument('--currency', action='store', help = textwrap.dedent("""\
                                Available Currencies
                                #ISO code
                                EURUSD=X  =>  Euro to USD 
                                JPY=X  =>  Japanese Yen to USD 
                                GBPUSD=X  =>  Pound sterling to USD 
                                AUDUSD=X  =>  Australian Dollar to USD 
                                NZDUSD=X  =>  New Zealand Dollar to USD 
                                EURJPY=X  =>  Euro to Japanese Yen 
                                GBPJPY=X  =>  Pound sterling to Japanese Yen 
                                EURGBP=X  =>  Euro to Pound sterling 
                                EURCAD=X  =>  Euro to Canadian Dollar 
                                EURSEK=X  =>  Euro to Swedish Krona 
                                EURCHF=X  =>  Euro to Swiss Franc 
                                EURHUF=X  =>  Euro to Hungarian Forint 
                                EURJPY=X  =>  Euro to Japanese Yen 
                                CNY=X  =>  USD to Chinese Yuan 
                                HKD=X  =>  USD to Hong Kong Dollar 
                                SGD=X  =>  USD to Singapore Dollar 
                                INR=X  =>  USD to Indian Rupees 
                                MXN=X  =>  USD to Mexican Peso 
                                PHP=X  =>  USD to Philippine peso 
                                IDR=X  =>  USD to Indonesian Rupiah 
                                THB=X  =>  USD to Thai Baht 
                                MYR=X  =>  USD to Malaysian Ringgit 
                                ZAR=X  =>  USD to South African Rand 
                                RUB=X  =>  USD to Russian Ruble 
    """)  ,type=str, required=True)
    my_parser.add_argument('--output', action='store', help = 'Specify path to save the report' , type=str, required=True)
    my_parser.add_argument('--date', action='store', help = 'Predict price of currency on the specific date (yyyy-mm-dd) ' , type=str, required=False)
    
    args = my_parser.parse_args()
    currency = args.currency
    outPath = args.output
    
    inr = fetchLongData(currency)
    df = fetch10YData(currency)
    dfInfo = inr.info
    datelist, xPred, m, c= regressionModel(df)
    try:
        date = args.date
        x = pd.to_datetime(date, origin='unix') - pd.datetime(2021,1,1)
        value = int(x.days) * m + c
        print("Predicted price on :" + str(date) + ":\t" +  str(value))
    except:
        pass

    fig, newFig = charts.smaChart(df)
    theFig, yesFig = charts.yesterday(currency)
    weeklyFig = charts.weeklyChart(dfInfo, currency)
    monthlyFig =  charts.monthlyChart(dfInfo, currency)
    generateReport(dfInfo, weeklyFig, monthlyFig, newFig, df, datelist, xPred, fig, yesFig, theFig, outPath)
    print("Report Generated Successfully")