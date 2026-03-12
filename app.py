import streamlit as st

from utils.data_loader import load_data

from components.header import render_header
from components.metrics import render_metrics
from components.map_view import render_map
from components.trend_analysis import render_trend
from components.correlation_analysis import render_corr
from components.forecast_view import render_forecast
from components.policy_simulator import render_policy

st.set_page_config(layout="wide")

df = load_data()

render_header()

render_metrics(df)

st.divider()

st.subheader("City Pollution Heatmap")
render_map(df)

st.divider()

st.subheader("Pollution Trends")
render_trend(df)

st.divider()

st.subheader("Pollution Drivers")
render_corr(df)

st.divider()

st.subheader("Forecast Engine")
render_forecast(df)

st.divider()

st.subheader("Policy Simulation")
render_policy(df)