🏭 Air Quality Analysis & AQI Calculation
This project performs a comprehensive spatio-temporal analysis of air quality data (specifically for Bangalore stations like Silkboard, Bapuji Nagar, etc.). 
It moves beyond simple averages to understand how different pollutants interact and contribute to the overall Air Quality Index (AQI).

Key Features
📊 Correlation Analysis: Identifies key drivers of pollution (e.g., determining that PM2.5 is strongly linked to PM10 but independent of $SO_2$).
🧮 Custom AQI Calculator: Implements the CPCB (Central Pollution Control Board) formulas to calculate sub-indices for $SO_2$ and $NO_2$ manually.
📍 Spatio-Temporal Tracking: Analyzes pollution trends across different stations and timeframes to detect hotspots without "smoothing out" critical peak pollution events.
📉 Trend Visualization: Comparative plotting of particulate matter vs. gaseous pollutants.

Tech StackLanguage: 
PythonLibraries: Pandas, NumPy, Matplotlib, Seaborn
Standards: CPCB (India) AQI Breakpoints
