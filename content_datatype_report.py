import pandas as pd

# Function to convert a DataFrame to an HTML table with CSS styling
def df_to_html_table(df, title):
    return f'<h2>{title}</h2>' + df.to_html(classes='styled-table')

# Read the data
content_table_data = pd.read_csv('yt_dataset/content_table_datatype.csv')

# Define categories for logical separation of variables
audience_engagement_vars = ['Likes', 'Dislikes', 'Comments added', 'Shares']
viewer_metrics_vars = ['Views', 'Watch time (hours)', 'Average percentage viewed (%)', 'Unique viewers']
subscriber_metrics_vars = ['Subscribers lost', 'Subscribers gained', 'Subscribers']
content_discovery_vars = ['Impressions', 'Impressions click-through rate (%)', 'Shown in feed']
video_interaction_vars = ['End screen elements shown', 'End screen element clicks', 'Average view duration']

# Create HTML tables for each category
audience_engagement_table = df_to_html_table(content_table_data[['Content type'] + audience_engagement_vars], '1. Audience Engagement Metrics')
viewer_metrics_table = df_to_html_table(content_table_data[['Content type'] + viewer_metrics_vars], '2. Viewer Metrics')
subscriber_metrics_table = df_to_html_table(content_table_data[['Content type'] + subscriber_metrics_vars], '3. Subscriber Metrics')
content_discovery_table = df_to_html_table(content_table_data[['Content type'] + content_discovery_vars], '4. Content Discovery Metrics')
video_interaction_table = df_to_html_table(content_table_data[['Content type'] + video_interaction_vars], '5. Video Interaction Metrics')

# CSS for styling the tables
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

# Combine all tables into a single HTML report
html_report = f'''
<!DOCTYPE html>
<html>
<head>
    <title>YouTube Channel Content Strategy Report</title>
    {css_style}
</head>
<body>
    <h1>YouTube Channel Content Strategy Report: Content-Type Analysis</h1>
    {audience_engagement_table}
    {viewer_metrics_table}
    {subscriber_metrics_table}
    {content_discovery_table}
    {video_interaction_table}
</body>
</html>
'''

# Save the HTML report to a file
with open('YouTube_Content_Strategy_Report.html', 'w') as f:
    f.write(html_report)