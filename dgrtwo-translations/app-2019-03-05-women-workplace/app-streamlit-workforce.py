# # Streamlit dashboard demo
#
# Notebook based on this tutorial...
#
# https://docs.streamlit.io/tutorial/create_a_data_explorer_app.html
#
# Running: streamlit run app-streamlit.py
#
# Resources
#
# https://github.com/streamlit/streamlit

# +
import streamlit as st
import pandas as pd
import numpy as np

from plotnine import *

from siuba import _, filter, summarize, mutate
from siuba.data import mtcars
from plotly import tools

import os

# NOTE: needed to add this in order to test streamlit in a REPL
__file__ = os.getcwd()


# -

def plot_pay_gap_2016(jobs_gender):
    return (
        jobs_gender
        >> filter(_.year == 2016, _.total_workers >= 20000)
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


# ## Load Data

# +
st.title('Tidy Tuesday: women in the workforce data')

@st.cache
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-03-05/jobs_gender.csv")

data_load_state = st.text('Loading data...')
jobs_gender = load_data()
data_load_state.text('Loading data... done!')
# -

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(jobs_gender)

# +
major_category = st.sidebar.selectbox(
    'Which number do you like best?',
     jobs_gender.major_category.unique()
    )

minor_options = jobs_gender \
        .loc[lambda d: d.major_category == major_category, 'minor_category'] \
        .unique()

minor_category = st.sidebar.selectbox(
    'Minor category',
    minor_options
    )

# +

filtered_jobs = filter(
    jobs_gender,
    _.major_category == major_category,
    _.minor_category == minor_category
)

p = plot_pay_gap_2016(filtered_jobs)

st.plotly_chart(tools.mpl_to_plotly(p.draw()))
