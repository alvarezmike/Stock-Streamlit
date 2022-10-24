import yfinance as yf
import streamlit as st
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# For more emojis code https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Stock Price", page_icon="::bar_chart:")
st.header("Amazon Stock Price Web App")

# define the ticker symbol
tickerSymbol = 'AMZN'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-10-24')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

# ticker company overview
ticker_summary = tickerData.info['longBusinessSummary']
st.info(ticker_summary)

st.write("""
Shown are the stock closing price and volume of Amazon!
""")
st.caption("Graph start=2010-5-31, end=2022-10-24")

# charts displayed
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

# table with historical data
st.header("Ticker data")
ticker_df_table = tickerDf.drop(columns=["Dividends","Stock Splits"])
st.write(ticker_df_table)

