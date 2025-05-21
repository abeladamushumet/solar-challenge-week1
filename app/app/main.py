# app/main.py
import streamlit as st
import pandas as pd
from app.utils import load_clean_data, generate_summary_table, plot_boxplots, plot_avg_ghi_bar

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")
st.title("🌞 Cross-Country Solar Potential Dashboard")

# Sidebar selections
st.sidebar.header("Dashboard Controls")
metrics = ["GHI", "DNI", "DHI"]
selected_metric = st.sidebar.selectbox("Select Metric", metrics)

# Load data
data = load_clean_data()

# Boxplots
st.subheader(f"{selected_metric} Distribution Across Countries")
fig = plot_boxplots(data, selected_metric)
st.plotly_chart(fig, use_container_width=True)

# Summary table
st.subheader("📊 Summary Statistics")
sum_table = generate_summary_table(data)
st.dataframe(sum_table.style.format("{:.2f}"))


st.subheader("🌍 Country Ranking by Average GHI")
bar_fig = plot_avg_ghi_bar(data)
st.plotly_chart(bar_fig, use_container_width=True)
