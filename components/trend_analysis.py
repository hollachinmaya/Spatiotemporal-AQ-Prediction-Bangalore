import plotly.express as px
import streamlit as st

def render_trend(df):

    station = st.selectbox("Select Station", df["Station"].unique())

    sdf = df[df["Station"] == station]

    fig = px.line(
        sdf,
        x="datetime",
        y="PM2_5",
        title="PM2.5 Temporal Trend"
    )

    st.plotly_chart(fig, use_container_width=True)