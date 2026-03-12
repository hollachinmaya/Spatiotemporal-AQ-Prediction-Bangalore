import plotly.express as px
import pandas as pd
from utils.station_coordinates import station_coords
import streamlit as st

def render_map(df):

    station_data = df.groupby("Station")["AQI"].mean().reset_index()

    lat = []
    lon = []

    for s in station_data["Station"]:

        lat.append(station_coords[s][0])
        lon.append(station_coords[s][1])

    station_data["lat"] = lat
    station_data["lon"] = lon

    fig = px.scatter_mapbox(
        station_data,
        lat="lat",
        lon="lon",
        color="AQI",
        size="AQI",
        zoom=10,
        mapbox_style="carto-darkmatter",
        hover_name="Station",
        color_continuous_scale="Turbo"
    )

    st.plotly_chart(fig, use_container_width=True)