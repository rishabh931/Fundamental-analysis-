import streamlit as st
from fetch_data import fetch_stock_data
from analyze_fundamentals import analyze_stock
from generate_pdf import create_pdf_report
import base64

st.set_page_config(page_title="Minervini Stock Analyzer", layout="centered")
st.title("Mark Minervini India Stock Analyzer")

ticker = st.text_input("Enter NSE stock symbol (e.g., INFY, TCS, RELIANCE):")

if st.button("Analyze"):
    if not ticker:
        st.error("Please enter a stock symbol.")
    else:
        with st.spinner("Fetching data and analyzing..."):
            data = fetch_stock_data(ticker)
            if not data:
                st.error("Failed to fetch stock data. Please check the symbol.")
            else:
                results, charts = analyze_stock(data)
                pdf_path = create_pdf_report(ticker, results, charts)

                with open(pdf_path, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                    href = f'<a href="data:application/pdf;base64,{base64_pdf}" download="{ticker}_report.pdf">Download PDF Report</a>'
                    st.markdown(href, unsafe_allow_html=True)

                st.success("Analysis Complete. Scroll below for the download.")
