import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import datetime as dTime

def smaChart(df):
    tempDf = df.copy()
    tempDf['SMA5'] = tempDf.Close.rolling(5).mean()
    tempDf['SMA20'] = tempDf.Close.rolling(20).mean()
    tempDf['SMA50'] = tempDf.Close.rolling(50).mean()
    fig = go.Figure(data=[go.Ohlc(x=tempDf['Date'],
                open=tempDf['Open'],
                high=tempDf['High'],
                low=tempDf['Low'],
                close=tempDf['Close'], name = "OHLC"),
                go.Scatter(x=tempDf.Date, y=tempDf.SMA5, line=dict(color='orange', width=1), name="SMA5"),
                go.Scatter(x=tempDf.Date, y=tempDf.SMA20, line=dict(color='green', width=1), name="SMA20"),
                go.Scatter(x=tempDf.Date, y=tempDf.SMA50, line=dict(color='blue', width=1), name="SMA50")])
    newFig = emaChart(tempDf)
    return fig, newFig

def emaChart(tempDf):
    tempDf['EMA5'] = tempDf.Close.ewm(span=5, adjust=False).mean()
    tempDf['EMA20'] = tempDf.Close.ewm(span=20, adjust=False).mean()
    newFig = go.Figure(data=[go.Ohlc(x=tempDf['Date'],
                open=tempDf['Open'],
                high=tempDf['High'],
                low=tempDf['Low'],
                close=tempDf['Close'], name = "OHLC"),
                go.Scatter(x=tempDf.Date, y=tempDf.SMA5, line=dict(color='orange', width=1), name="SMA5"),
                go.Scatter(x=tempDf.Date, y=tempDf.SMA20, line=dict(color='green', width=1), name="SMA20"),
                go.Scatter(x=tempDf.Date, y=tempDf.SMA50, line=dict(color='blue', width=1), name="SMA50"),
                go.Scatter(x=tempDf.Date, y=tempDf.EMA5, line=dict(color='orange', width=1), name="EMA5"),
                go.Scatter(x=tempDf.Date, y=tempDf.EMA20, line=dict(color='blue', width=1), name="EMA50")])
    return newFig

def yesterday(currency):
    theFig, yesFig = yesterdaySma(currency)
    return theFig, yesFig

def yesterdaySma(currency):
    newDf = yf.download(str(currency),start=str(dTime.datetime.now().date() - dTime.timedelta(days = 1)),end=str(dTime.datetime.now().date()),interval="5m")
    newDf = newDf.reset_index()
    newDf['SMA5'] = newDf.Close.rolling(5).mean()
    newDf['SMA20'] = newDf.Close.rolling(20).mean()
    newDf['SMA50'] = newDf.Close.rolling(50).mean()

    theFig = go.Figure(data=[go.Ohlc(x=newDf['Datetime'],
                open=newDf['Open'],
                high=newDf['High'],
                low=newDf['Low'],
                close=newDf['Close'], name = "OHLC"),
                go.Scatter(x=newDf.Datetime, y=newDf.SMA5, line=dict(color='orange', width=1), name="SMA5"),
                go.Scatter(x=newDf.Datetime, y=newDf.SMA20, line=dict(color='green', width=1), name="SMA20"),
                go.Scatter(x=newDf.Datetime, y=newDf.SMA50, line=dict(color='blue', width=1), name="SMA50")])
    theFig.update_layout(title="SMA Chart")
    yesFig = yesterdayEma(newDf)
    return theFig, yesFig

def yesterdayEma(newDf):
    newDf['EMA5'] = newDf.Close.ewm(span=5, adjust=False).mean()
    newDf['EMA20'] = newDf.Close.ewm(span=20, adjust=False).mean()
    yesFig = go.Figure(data=[go.Ohlc(x=newDf['Datetime'],
                open=newDf['Open'],
                high=newDf['High'],
                low=newDf['Low'],
                close=newDf['Close'], name = "OHLC"),
                go.Scatter(x=newDf.Datetime, y=newDf.EMA5, line=dict(color='orange', width=1), name="EMA5"),
                go.Scatter(x=newDf.Datetime, y=newDf.EMA20, line=dict(color='blue', width=1), name="EMA50")])
    yesFig.update_layout(title="EMA Chart")
    return yesFig

def weeklyChart(dfInfo, currency):
    lstwk = datetime.today() - dTime.timedelta(days=7)
    lstwk = lstwk.strftime("%Y-%m-%d")
    weekDf = yf.download(str(currency),start=str(lstwk),interval="1h")
    weekDf = weekDf.reset_index()
    weeklyFig = px.line(weekDf, x="index", y=["Open", "High", "Adj Close"], title=f"Last Week Performance of {dfInfo['shortName']}")
    return weeklyFig

def monthlyChart(dfInfo, currency):
    lstmon = datetime.today() - dTime.timedelta(days=28)
    lstmon = lstmon.strftime("%Y-%m-%d")
    monthDf = yf.download(str(currency),start=str(lstmon))
    monthDf = monthDf.reset_index()
    monthlyFig = px.line(monthDf, x="Date", y=["Open", "High", "Adj Close"], title=f"Last Month Performance of {dfInfo['shortName']}")
    return monthlyFig