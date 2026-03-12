import plotly.express as px
import streamlit as st

def render_corr(df):

    corr = df[[
        "PM2_5","PM10","NO","NO2",
        "SO2","CO","Ozone",
        "AT_C","RH_Percent"
    ]].corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu"
    )

    st.plotly_chart(fig, use_container_width=True)