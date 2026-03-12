import plotly.graph_objects as go
import numpy as np
import streamlit as st

def render_forecast(df):

    recent = df.tail(100)

    prediction = recent["PM2_5"] + np.random.normal(0,5,len(recent))

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=recent["datetime"],
        y=recent["PM2_5"],
        name="Historical"
    ))

    fig.add_trace(go.Scatter(
        x=recent["datetime"],
        y=prediction,
        name="Forecast",
        line=dict(dash="dot")
    ))

    st.plotly_chart(fig, use_container_width=True)