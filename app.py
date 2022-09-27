import yfinance as yf
import streamlit as st

# For more emojis code https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Stock Price", page_icon="::bar_chart:")

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Amazon!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'AMZN'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)