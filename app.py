import streamlit as st
import yfinance as yf
import plotly.express as px
import datetime
from datetime import date, timedelta
# For more emojis code https://www.webfx.com/tools/emoji-cheat-sheet/

# set default date to -1 of current date
today = date.today()
default_date_yesterday = today - timedelta(days=1)

# header of page
st.set_page_config(page_title="Stock Price", page_icon="::bar_chart:")
st.caption(":point_left: The left menu allows you to dynamically retrieve data by modifying the ticker, "
           "start date, and end date.")
st.header("Stock Price Analysis")


# sidebar menu options selector
ticker = st.sidebar.text_input("Ticker", "AAPL")
st.sidebar.caption("Important to utilize accurate ticker symbols and capitalize them appropriately.")
start_date = st.sidebar.date_input("Start date", datetime.date(2023, 1, 1))
end_date = st.sidebar.date_input("End date", default_date_yesterday)
data = yf.download(ticker, start=start_date, end=end_date)

fig = px.line(data, x=data.index, y=data["Adj Close"], title=ticker)
st.plotly_chart(fig)

st.markdown("""---""")
tickerData = yf.Ticker(ticker)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2023-03-20')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
Historical closing price
""")
st.caption("Graph start=2010-5-31, end=2023-03-20")

# historical closing chart displayed
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

# creating tabs fort additional information
table, news = st.tabs(["Table", "News"])

with table:
    # table with historical data
    st.header("Ticker data")
    ticker_df_table = tickerDf.drop(columns=["Dividends","Stock Splits"])
    st.write(ticker_df_table)

with news:
    st.header(f"Latest news of {ticker}")
    st.write(f"{tickerData.news[0]['title']} ")
    st.write(f":newspaper: Link to full article: {tickerData.news[0]['link']}")
