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

from siuba import _, filter
from plotnine import *

import os

# NOTE: needed to add this in order to test streamlit in a REPL
__file__ = os.getcwd()
# -

# ## Load Data

# +
st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Loading data... done!')
# -

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

option = st.sidebar.selectbox(
    'Which number do you like best?',
     [4, 6, 8])

# +
from siuba.data import mtcars
import plotly.tools as tls

p = mtcars >> filter(_.cyl == option) >> ggplot(aes('hp', 'mpg')) + geom_point()

st.pyplot(p.draw())

#st.plotly_chart()
