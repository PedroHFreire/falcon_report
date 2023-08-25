import pandas as pd
import plotly.express as px

# Read the 'geo_chart_data.csv' dataset
geo_chart_data = pd.read_csv('geo_chart_data.csv')

# Convert the 'Date' column to datetime format
geo_chart_data['Date'] = pd.to_datetime(geo_chart_data['Date'])

# Pivot the data to make it suitable for an area plot
pivot_data = geo_chart_data.pivot(index='Date', columns='Geography', values='Views').fillna(0)

# Create the area plot using Plotly
fig = px.area(pivot_data.reset_index(), x='Date', y=pivot_data.columns, title='Time Series Area Plot of Views by Geography')

# Show the figure (this will also save it as an HTML file)
fig.write_html("geo_chart_data_area_plot.html")