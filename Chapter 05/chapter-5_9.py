# Interactive plot

import plotly.express as px

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

fig = px.scatter(x=x, y=y1, labels={"x": "X-axis Label", "y": "Y-axis Label"}, title="Interactive Scatter Plot")

fig.update_traces(hovertemplate="X: %{x}<br>Y: %{y}")

fig.update_layout(
    font_family="Arial",
    font_size=14,
    title_font=dict(size=24, color='blue'),
    plot_bgcolor='rgba(230, 230, 230, 0.8)',
    xaxis_title="X-axis Label",
    yaxis_title="Y-axis Label"
)

fig.update_traces(
    marker=dict(size=12, color='red', symbol='star'),
    selector=dict(mode='markers')
)

fig.show()