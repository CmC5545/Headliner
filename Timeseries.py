import plotly.express as px
import datetime
import plotly.graph_objects as go
import datetime
import pandas as pd
df = pd.read_csv("abcnews-date-text.csv",parse_dates=[0], infer_datetime_format=True)

#fig = px.line(df, x='publish_date', y='headline_text')
#fig.show()
#fig2 = go.Figure([go.Scatter(x=df['publish_date'], y=df['headline_text'])])
#fig.show()

fig = go.Figure()
fig.add_trace(go.Scatter(
                x=df.publish_date,
                y=df['headline_text'],
                name="Headlines",
                line_color='deepskyblue',
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df.headline_text,
                y=df['publish_date'],
                name="Dates",
                line_color='dimgray',
                opacity=0.8))
fig.update_layout(xaxis_range=['2016-07-01','2016-12-31'],
                  title_text="Manually Set Date Range")
fig.show()               

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.publish_date, y=df['headline_text'], name="Series1",
                         line_color='deepskyblue'))

fig.add_trace(go.Scatter(x=df.headline_text, y=df['publish_date'], name="Series2",
                         line_color='dimgray'))

fig.update_layout(title_text='Time Series with Rangeslider',
                  #xaxis_rangeslider_visible=True)
#fig.show()

