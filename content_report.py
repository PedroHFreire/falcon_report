import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

# Read the 'content_totals.csv' dataset
content_totals = pd.read_csv('yt_dataset/content_totals.csv')

# Convert the 'Date' column to datetime format
content_totals['Date'] = pd.to_datetime(content_totals['Date'])

# Calculate the 7-day rolling mean for 'Average percentage viewed (%)'
content_totals['7_day_Rolling_Mean'] = content_totals['Average percentage viewed (%)'].rolling(window=7).mean()

# Create the figure
fig = go.Figure()

# Add the actual data as a line
fig.add_trace(
    go.Scatter(x=content_totals['Date'], y=content_totals['Average percentage viewed (%)'], mode='lines+markers', name='Actual Data'),
)

# Add the 7-day rolling mean as a dashed line
fig.add_trace(
    go.Scatter(x=content_totals['Date'], y=content_totals['7_day_Rolling_Mean'], mode='lines', name='7-Day Rolling Mean', line=dict(dash='dash'))
)

# Update layout and axis properties
fig.update_layout(
    title='Overall Content Performance with 7-Day Rolling Mean (Mondays)',
    xaxis_title='Date',
    xaxis=dict(
        tickmode='array',
        tickvals=pd.date_range(content_totals['Date'].min(), content_totals['Date'].max(), freq='W-MON')
    ),
    yaxis_title='Average Percentage Viewed (%)',
    template='plotly_white'
)

# Save the figure as an HTML file
plot(fig, filename='Content_Totals_Plot.html', auto_open=False)