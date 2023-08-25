import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.offline import plot

# Generate the first plot (Time series)
traffic_totals = pd.read_csv('yt_dataset/traffic_totals.csv')
traffic_totals['Date'] = pd.to_datetime(traffic_totals['Date'])
traffic_totals['7_day_Rolling_Mean'] = traffic_totals['Views'].rolling(window=7).mean()

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=traffic_totals['Date'], y=traffic_totals['Views'], mode='lines+markers', name='Actual Views'))
fig1.add_trace(go.Scatter(x=traffic_totals['Date'], y=traffic_totals['7_day_Rolling_Mean'], mode='lines', name='7-Day Rolling Mean', line=dict(dash='dash')))

fig1.update_layout(
    title='Overall View Trend with 7-Day Rolling Mean (Mondays)',
    xaxis_title='Date',
    xaxis=dict(
        tickmode='array',
        tickvals=pd.date_range(traffic_totals['Date'].min(), traffic_totals['Date'].max(), freq='W-MON')
    ),
    yaxis_title='Views',
    template='plotly_white'
)

plot(fig1, filename='Time_Series_Plot.html', auto_open=False)

# Generate the second plot (Treemap)
traffic_table_data = pd.read_csv('yt_dataset/traffic_table_data.csv')
traffic_table_data_filtered = traffic_table_data[traffic_table_data['Traffic source'] != 'Total']

fig2 = px.treemap(traffic_table_data_filtered,
                 path=[px.Constant("Traffic Sources"), 'Traffic source'],
                 values='Views',
                 color='Views',
                 hover_data=['Impressions', 'Watch time (hours)'],
                 color_continuous_scale='Viridis')

fig2.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    title='Traffic Sources by Views'
)

plot(fig2, filename='Treemap_Plot.html', auto_open=False)