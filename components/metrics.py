import streamlit as st

def render_metrics(df):

    avg_aqi = df["AQI"].mean()
    max_aqi = df["AQI"].max()
    stations = df["Station"].nunique()

    c1,c2,c3 = st.columns(3)

    c1.metric("Average AQI", round(avg_aqi,1))
    c2.metric("Max AQI", round(max_aqi,1))
    c3.metric("Stations", stations)