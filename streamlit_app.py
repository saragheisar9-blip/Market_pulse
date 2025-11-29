import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(layout="wide")
st.title("🏛 *Market Pulse Dashboard*")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("⭐ Best", "Technology", "22.5%")
col2.metric("⚡ Riskiest", "Energy", "28.3%")
col3.metric("🛡 Safest", "Utilities", "15.2%")

st.success("✅ *Bonus Complete!*")
