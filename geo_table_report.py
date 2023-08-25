import pandas as pd

# Function to convert a DataFrame to an HTML table with CSS styling
def df_to_html_table(df, title):
    return f'<h2>{title}</h2>' + df.to_html(classes='styled-table')

# Read the geo_table_data.csv dataset
geo_table_data = pd.read_csv('yt_dataset/geo_table_data.csv')

# Create an HTML table for the Geography Analysis
geo_analysis_table = df_to_html_table(geo_table_data, 'Geography Analysis')

# CSS for styling the table
css_style = '''
<style>
    .styled-table {
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 18px;
        text-align: left;
        width: 100%;
    }
    .styled-table th, .styled-table td {
        padding: 12px 15px;
        border-bottom: 1px solid #ddd;
    }
    .styled-table thead tr {
        background-color: #009879;
        color: #ffffff;
    }
    .styled-table tbody tr:nth-of-type(even) {
        background-color: #f3f3f3;
    }
</style>
'''

# Combine the table into a single HTML report
html_report = f'''
<!DOCTYPE html>
<html>
<head>
    <title>YouTube Channel Report: Geography Analysis</title>
    {css_style}
</head>
<body>
    <h1>YouTube Channel Report: Geography Analysis</h1>
    {geo_analysis_table}
</body>
</html>
'''

# Save the HTML report to a file
with open('YouTube_Geography_Report.html', 'w') as f:
    f.write(html_report)