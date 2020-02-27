# This notebook was downloaded from...
#
# https://github.com/plotly/jupyterlab-dash/blob/master/notebooks/test_app_viewer.ipynb
#
# Resources
#
# * https://github.com/plotly/dash
# * https://github.com/plotly/plotly.py
# * https://github.com/plotly/jupyterlab-dash

# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

# +
df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'cb5392c35661370d95f300086accea51/raw/'
    '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
    'indicators.csv')

available_indicators = df['Indicator Name'].unique()
# -

# Build AppViewer 
from jupyterlab_dash import AppViewer
viewer = AppViewer()

# +
# Build App
from plotnine import *
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in [4, 6, 8]],
                value='Cylinders'
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),
    ]),

    dcc.Graph(id='indicator-graphic'),
])

# Callbacks
@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('xaxis-column', 'value')]
    )
def update_graph(val_cyl):

    from siuba.data import mtcars
    from siuba import _, filter
    import plotly.tools as tls

    p = (
        mtcars
        >> filter(_.cyl == val_cyl)
        >> ggplot(aes("hp", "mpg"))
        + geom_point()
        + ggtitle("Hp vs Mpg for cyl = %s" % val_cyl)
    )
    
    return tls.mpl_to_plotly(p.draw())

#     return {
#         'data': [go.Scatter(
#             x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
#             y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
#             text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
#             mode='markers',
#             marker={
#                 'size': 15,
#                 'opacity': 1,
#                 'color': 'blue',
#                 'line': {'width': 2}
#             }
#         )],
#         'layout': go.Layout(
#             xaxis={
#                 'title': xaxis_column_name,
#                 'type': 'linear' if xaxis_type == 'Linear' else 'log'
#             },
#             yaxis={
#                 'title': yaxis_column_name,
#                 'type': 'linear' if yaxis_type == 'Linear' else 'log'
#             },
#             margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
#             hovermode='closest',
#         )
#     }

viewer.show(app)
