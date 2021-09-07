import datetime
#import htmlmin

def generateReport(dfInfo, weeklyFig, monthlyFig, newFig, df, datelist, xPred, fig, yesFig, theFig, outPath):
    temp = xPred[-1:]
    for i in temp:
       yesterdayPrice = str(round(float(i),2)) 
    htmlFile = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="style.css" />
        <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
        crossorigin="anonymous"
        />
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>        
    </head>
    <body>
        <div class="container-fluid" style="font-family: 'Rubik', sans-serif;">
        <div class="row">
            <div>
            <h3 class="text-center">Analysis Report For """+dfInfo['shortName']+"""</h3>
            </div>
            <div class="col-sm-12 col-md-12 col-lg-6">
            """ + weeklyFig.to_html() + """
            <div class="card-caption">
                <h3 class="text-center">Weekly Performance For """+dfInfo['shortName']+"""</h3>
            </div>
            </div>
            <div class="col-sm-12 col-md-12 col-lg-6">
            """ + monthlyFig.to_html() + """
            <div class="card-caption">
                <h3 class="text-center">Monthly Performance For """+dfInfo['shortName']+"""</h3>
            </div>
            </div>
            <div class="mx-auto col-sm-4 col-lg-12 col-md-12 p-5">
            """ + newFig.to_html() + """
            <div class="card-caption">
                <h3 class="text-center">TimeLine Chart For """+dfInfo['shortName']+"""</h3>
            </div>
            </div>
            <div class="table-responsive-md col-6 p-5">
            <h2 class="text-center">Summary</h2>
            <table class="table">
                <tbody>
                <tr>
                    <th scope="row">Exchange</th>
                    <td>"""+str(dfInfo['exchange'])+"""</td>
                </tr>
                <tr>
                    <th scope="row">Symbol</th>
                    <td>"""+str(dfInfo['symbol'])+"""</td>
                </tr>
                <tr>
                    <th scope="row">Previous Close</th>
                    <td>"""+str(dfInfo['previousClose'])+"""</td>
                </tr>
                <tr>
                    <th scope="row">Regular Market Previous Close</th>
                    <td>"""+str(dfInfo['regularMarketPreviousClose'])+"""</td>
                </tr>
                <tr>
                    <th scope="row">Regualr Market Open</th>
                    <td>"""+str(dfInfo['regularMarketOpen'])+"""</td>
                </tr>
                <tr>
                    <th scope="row">Open</th>
                    <td>"""+str(dfInfo['open'])+"""</td>
                </tr>
                <tr></tr>
                <tr>
                    <th scope="row">Regualr Market High</th>
                    <td>"""+str(dfInfo['regularMarketDayHigh'])+"""</td>
                </tr>
                <tr>
                    <th scope="row">Day High</th>
                    <td>"""+str(dfInfo['dayHigh'])+"""</td>
                </tr>
                <tr>
                    <th scope="row">Regualr Market Low</th>
                    <td>"""+str(dfInfo['regularMarketDayLow'])+"""</td>
                </tr>
                <tr>
                    <th scope="row">Day Low</th>
                    <td>"""+str(dfInfo['dayLow'])+"""</td>
                </tr>
                </tbody>
            </table>
            </div>
            <div class="table-responsive-md col-6 p-5">
                <h2 class="text-center">One Week Data</h2>
                <table class="table">
                <tbody>
                    <thead>
                        <tr>
                            <th scope="col">Date</th>
                            <th scope="col">Open</th>
                            <th scope="col">High</th>
                            <th scope="col">Low</th>
                            <th scope="col">Close</th>
                            <th scope="col">Adj Close</th>
                        </tr>
                    </thead>
                    <tr>
                    <th scope="row">"""+str(df['Date'][-7:-6].dt.date.to_string(index=False))+"""</th>
                    <td>"""+str(df['Open'][-7:-6].to_string(index=False))+"""</td>
                    <td>"""+str(df['High'][-7:-6].to_string(index=False))+"""</td>
                    <td>"""+str(df['Low'][-7:-6].to_string(index=False))+"""</td>
                    <td>"""+str(df['Close'][-7:-6].to_string(index=False))+"""</td>
                    <td>"""+str(df['Adj Close'][-7:-6].to_string(index=False))+"""</td>
                    </tr>
                    <tr>
                        <th scope="row">"""+str(df['Date'][-6:-5].dt.date.to_string(index=False))+"""</th>
                        <td>"""+str(df['Open'][-6:-5].to_string(index=False))+"""</td>
                        <td>"""+str(df['High'][-6:-5].to_string(index=False))+"""</td>
                        <td>"""+str(df['Low'][-6:-5].to_string(index=False))+"""</td>
                        <td>"""+str(df['Close'][-6:-5].to_string(index=False))+"""</td>
                        <td>"""+str(df['Adj Close'][-6:-5].to_string(index=False))+"""</td>
                    </tr>
                    <tr>
                        <th scope="row">"""+str(df['Date'][-5:-4].dt.date.to_string(index=False))+"""</th>
                        <td>"""+str(df['Open'][-5:-4].to_string(index=False))+"""</td>
                        <td>"""+str(df['High'][-5:-4].to_string(index=False))+"""</td>
                        <td>"""+str(df['Low'][-5:-4].to_string(index=False))+"""</td>
                        <td>"""+str(df['Close'][-5:-4].to_string(index=False))+"""</td>
                        <td>"""+str(df['Adj Close'][-5:-4].to_string(index=False))+"""</td>
                    </tr>
                    <tr>
                        <th scope="row">"""+str(df['Date'][-4:-3].dt.date.to_string(index=False))+"""</th>
                        <td>"""+str(df['Open'][-4:-3].to_string(index=False))+"""</td>
                        <td>"""+str(df['High'][-4:-3].to_string(index=False))+"""</td>
                        <td>"""+str(df['Low'][-4:-3].to_string(index=False))+"""</td>
                        <td>"""+str(df['Close'][-4:-3].to_string(index=False))+"""</td>
                        <td>"""+str(df['Adj Close'][-4:-3].to_string(index=False))+"""</td>
                    </tr>
                    <tr>
                        <th scope="row">"""+str(df['Date'][-3:-2].dt.date.to_string(index=False))+"""</th>
                        <td>"""+str(df['Open'][-3:-2].to_string(index=False))+"""</td>
                        <td>"""+str(df['High'][-3:-2].to_string(index=False))+"""</td>
                        <td>"""+str(df['Low'][-3:-2].to_string(index=False))+"""</td>
                        <td>"""+str(df['Close'][-3:-2].to_string(index=False))+"""</td>
                        <td>"""+str(df['Adj Close'][-3:-2].to_string(index=False))+"""</td>
                    </tr>
                    <tr>
                        <th scope="row">"""+str(df['Date'][-2:-1].dt.date.to_string(index=False))+"""</th>
                        <td>"""+str(df['Open'][-2:-1].to_string(index=False))+"""</td>
                        <td>"""+str(df['High'][-2:-1].to_string(index=False))+"""</td>
                        <td>"""+str(df['Low'][-2:-1].to_string(index=False))+"""</td>
                        <td>"""+str(df['Close'][-2:-1].to_string(index=False))+"""</td>
                        <td>"""+str(df['Adj Close'][-2:-1].to_string(index=False))+"""</td>
                    </tr>
                    <tr>
                        <th scope="row">"""+str(df['Date'][-1:].dt.date.to_string(index=False))+"""</th>
                        <td>"""+str(df['Open'][-1:].to_string(index=False))+"""</td>
                        <td>"""+str(df['High'][-1:].to_string(index=False))+"""</td>
                        <td>"""+str(df['Low'][-1:].to_string(index=False))+"""</td>
                        <td>"""+str(df['Close'][-1:].to_string(index=False))+"""</td>
                        <td>"""+str(df['Adj Close'][-1:].to_string(index=False))+"""</td>
                    </tr>
                    </tbody>
                </table>
            </div>
            </div>
            <h3 class="mx-auto">Analysis Charts</h3>
            <div class="col-sm-12 col-md-12 col-lg-12">
            """ + fig.to_html() + """
            <div class="card-caption">
                <h3 class="text-center p-2">SMA(Simple Moving Average) Chart For """+dfInfo['shortName']+"""</h3>
            </div>
            </div>
            <div class="col-sm-12 col-md-12 col-lg-12">
            """ + newFig.to_html() + """
            <div class="card-caption">
                <h3 class="text-center p-2">EMA(Exponential Moving Average) Chart For """+dfInfo['shortName']+"""</h3>
            </div>
            </div>
            <div class="col-sm-12 col-md-12 col-lg-12">
            """ + yesFig.to_html() + """
            <div class="card-caption">
                <h3 class="text-center p-2">Yesterday's EMA Performance For """+dfInfo['shortName']+"""</h3>
            </div>
            </div>
            <div class="col-sm-12 col-md-12 col-lg-12">
            """ + theFig.to_html() + """
            <div class="card-caption">
                <h3 class="text-center p-2">Yesterday's SMA Performance For """+dfInfo['shortName']+"""</h3>
            </div>
            </div>
            </div>
            <div class="table-responsive-md mx-auto col-6 p-5">
            <h4 class="text-center">Projected Prediction For """+dfInfo['shortName']+"""</h4>
            <table class="table">
                <tbody>
                <thead>
                    <tr>
                        <th scope="col">Date</th>
                        <th scope="col">Predicted Price</th>
                    </tr>
                </thead>
                <tr>
                    <th scope="row">"""+str(datelist[0].strftime("%Y-%m-%d"))+"""</th>
                    <td>"""+str(dfInfo['currency'])+""" """+ str(round(xPred[0], 2))+"""</td>
                </tr>
                <tr>
                    <th scope="row">"""+str(datelist[1].strftime("%Y-%m-%d"))+"""</th>
                    <td>"""+str(dfInfo['currency'])+""" """+ str(round(xPred[1], 2))+"""</td>
                </tr>
                <tr>
                    <th scope="row">"""+str(datelist[2].strftime("%Y-%m-%d"))+"""</th>
                    <td>"""+str(dfInfo['currency'])+""" """+ str(round(xPred[2],2))+"""</td>
                </tr>
                <tr>
                    <th scope="row">"""+str(datelist[3].strftime("%Y-%m-%d"))+"""</th>
                    <td>"""+str(dfInfo['currency'])+""" """+ str(round(xPred[3],2))+"""</td>
                </tr>
                <tr>
                    <th scope="row">"""+str(datelist[4].strftime("%Y-%m-%d"))+"""</th>
                    <td>"""+str(dfInfo['currency'])+""" """+ str(round(xPred[4],2))+"""</td>
                </tr>
                <tr>
                    <th scope="row">"""+str(datelist[5].strftime("%Y-%m-%d"))+"""</th>
                    <td>"""+str(dfInfo['currency'])+""" """+ str(round(xPred[5], 2))+"""</td>
                </tr>
                <tr></tr>
                <tr>
                    <th scope="row">"""+str(datelist[6].strftime("%Y-%m-%d"))+"""</th>
                    <td>"""+str(dfInfo['currency'])+""" """+ str(round(xPred[6], 2))+"""</td>
                </tr>
                </tbody>
            </table>
            </div>        
        </div>
    </body>
    </html>
    """
    #minified = htmlmin.minify(htmlFile, remove_empty_space=True)
    sym = dfInfo['shortName'].replace('/','-')
    today = datetime.datetime.today().replace(microsecond=0)
    today = str(today).replace(":",'-')
    with open(f"{outPath}/Analysis Report For {sym} on {today}.html",'w') as fl:
        fl.write(htmlFile)