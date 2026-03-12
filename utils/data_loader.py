import pandas as pd

def load_data():

    df = pd.read_csv("C:\\Users\\Chinmaya holla\\Desktop\\Airpollution\\Data\\Processed_data\\Final_analysis_ready.csv")

    df["datetime"] = pd.to_datetime(df["Timestamp"], dayfirst=True)

    df["AQI"] = df[["PM2_5_AQI","SO2_AQI","NO2_AQI"]].max(axis=1)

    return df