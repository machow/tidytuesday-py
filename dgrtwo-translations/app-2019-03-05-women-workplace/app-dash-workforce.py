# This notebook was downloaded from...
#
# https://github.com/plotly/jupyterlab-dash/blob/master/notebooks/test_app_viewer.ipynb
#
# Resources
#
# * https://github.com/plotly/dash
# * https://github.com/plotly/plotly.py
# * https://github.com/plotly/jupyterlab-dash

# +
# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

from siuba import _, filter, summarize, mutate
from siuba.data import mtcars
import pandas as pd
from plotly import tools

from plotnine import *


# -

def plot_pay_gap_2016(jobs_gender, major_category):
    return (
        jobs_gender
        >> filter(_.year == 2016, _.total_workers >= 20000)
        >> filter(_.major_category == major_category)
        #     >> arrange(desc(wage_percent_of_male))
        >> mutate(
            percent_female=_.workers_female / _.total_workers,
            wage_percent_female=_.total_earnings_female / _.total_earnings_male,
        )
        >> ggplot(
            aes(
                "percent_female",
                "wage_percent_female",
                color="minor_category",
                size="total_workers",
                label="occupation",
            )
        )
        + geom_point()
        + scale_size_continuous(range=[1, 10], guide=False)
        + labs(
            x="% of workforce reported as female",
            y="% of median female salary / median male",
            title="Gender disparity and pay gap in 2016",
            subtitle="Only occupations with at least 20,000 workers total",
            color="Minor category",
        )
        #        scale_x_continuous(labels = percent_format()) +
        #        scale_y_continuous(labels = percent_format())
    )



jobs_gender = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-03-05/jobs_gender.csv")

# Build AppViewer 
from jupyterlab_dash import AppViewer
viewer = AppViewer()

# +
# Build App
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='major-column',
                options=[{'label': i, 'value': i} for i in jobs_gender.major_category.unique()],
                value='Cylinders'
            ),
            dcc.Dropdown(
                    id='minor-column',
                    options=[{'label': i, 'value': i} for i in jobs_gender.major_category.unique()],
                    value='Cylinders'
            )                        
#             html.Div(id = "input-container")
        ],
        style={'width': '48%', 'display': 'inline-block'}),
    ]),

    dcc.Graph(id='indicator-graphic'),
])

# Callbacks




@app.callback(
    dash.dependencies.Output('minor-column', 'options'),
    [dash.dependencies.Input('major-column', 'value')]
    )
def update_minor_dropdown(val_major):
    options = jobs_gender \
        .loc[lambda d: d.major_category == val_major, 'minor_category'] \
        .unique()

    return [{'label': i, 'value': i} for i in options]
    

@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [
        dash.dependencies.Input('major-column', 'value'),
        dash.dependencies.Input('minor-column', 'value')
    ]
    )
def update_graph(val_major, val_minor):
    p = plot_pay_gap_2016(jobs_gender, val_major)
    return tools.mpl_to_plotly(p.draw())


viewer.show(app)
# -




