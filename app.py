import streamlit as st
from scraper import get_product_data
from database import load_data, save_data
from analyzer import Analyzer
from logger import Logger

st.title("📊 Price Tracker App (Fixed Version)")

# logger init
logger = Logger()

# input
url = st.text_input("Enter Product URL")

# track button
if st.button("Track"):
    if url:
        data = get_product_data(url)
        save_data(data)

        logger.log(f"Scraped URL: {url}")

        st.success("Data Saved Successfully!")

# load data
df = load_data()

st.subheader("📦 Tracked Products")
st.dataframe(df)

# analyzer init (after data load)
analyzer = Analyzer(None)  # works if Analyzer internally handles DB/df

st.subheader("📊 Analytics")

if st.button("Show Insights"):
    logger.log("Analytics viewed")

    try:
        st.write("### Cheapest Product")
        st.write(analyzer.cheapest_product())

        st.write("### Highest Rated Product")
        st.write(analyzer.highest_rated())

        st.write("### Average Price")
        st.write(analyzer.avg_price())

    except Exception as e:
        st.error(f"Analytics Error: {e}")
        logger.log(f"Analytics Error: {e}")