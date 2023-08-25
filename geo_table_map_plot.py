import pandas as pd
import plotly.express as px

# Read the geo_table_data.csv dataset
geo_table_data = pd.read_csv('yt_dataset/geo_table_data.csv')

# Filter out the row where Geography is 'Total' (if present)
geo_table_data = geo_table_data[geo_table_data['Geography'] != 'Total']

# Create the heatmap using Plotly
fig = px.choropleth(geo_table_data, 
                    locations='Geography', 
                    color='Views',
                    hover_name='Geography', 
                    color_continuous_scale=px.colors.sequential.Plasma,
                    labels={'Views':'Number of Views'},
                    title='World Heatmap of YouTube Views by Geography')

# Show the figure (this will also save it as an HTML file)
fig.write_html("geo_table_data_heatmap.html")
