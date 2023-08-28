import pandas as pd
import plotly.express as px

# Read the geo_table_data.csv dataset
geo_table_data = pd.read_csv('yt_dataset/geo_table_data.csv')

# Mapping of ISO 3166-1 alpha-2 to alpha-3 country codes
iso_alpha2_to_alpha3 = {
    'US': 'USA',
    'IN': 'IND',
    'IE': 'IRL',
    'AU': 'AUS',
    'CA': 'CAN',
    'GB': 'GBR',
    'PH': 'PHL',
    'BR': 'BRA',
    'DE': 'DEU',
    'PK': 'PAK'
}

# Initialize an empty set to collect unidentified country codes
unidentified_codes = set()

def map_and_check(alpha2_code):
    if alpha2_code == 'Total':
        return alpha2_code
    mapped_code = iso_alpha2_to_alpha3.get(alpha2_code)
    if mapped_code is None:
        unidentified_codes.add(alpha2_code)
        return alpha2_code
    return mapped_code

# Apply mapping and checking in one step
geo_table_data['Geography'] = geo_table_data['Geography'].apply(map_and_check)

# Raise exception if unidentified codes are found
if unidentified_codes:
    raise ValueError(f"Unidentified country codes found: {', '.join(unidentified_codes)}")

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
