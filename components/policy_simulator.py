import streamlit as st

def render_policy(df):

    traffic = st.slider("Traffic Reduction (%)",0,50,10)
    dust = st.slider("Dust Reduction (%)",0,50,10)

    sample = df.tail(1).copy()

    sample["NO2"] *= (1-traffic/100)
    sample["PM10"] *= (1-dust/100)

    new_aqi = sample[["PM2_5","PM10","NO2","SO2"]].sum(axis=1).values[0]

    st.metric("Predicted AQI After Policy", round(new_aqi,1))