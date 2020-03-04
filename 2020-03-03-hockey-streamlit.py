import pandas as pd
from qgrid import show_grid
from siuba import _, mutate, summarize, filter, group_by, select, inner_join, distinct, count, ungroup, arrange
import altair as alt
import streamlit as st


st.sidebar.markdown("""
# Hockey goals: 700 club

## Resources

* [Tidy tuesday data](https://github.com/rfordatascience/tidytuesday/tree/master/data/2020/2020-03-03)
* [Washington Post article](https://www.washingtonpost.com/graphics/2020/sports/capitals/ovechkin-700-goals/?utm_campaign=wp_graphics&utm_medium=social&utm_source=twitter)
""")


# +
@st.cache
def data_game_goals():
    return pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-03/game_goals.csv')

@st.cache
def data_top250():
    return pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-03/top_250.csv') \
        .rename(columns = {'total_games': 'total_goals'})


# -

top250 = data_top250()
game_goals = data_game_goals()
# top250 =     pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-03/top_250.csv') \
#         .rename(columns = {'total_games': 'total_goals'})
# game_goals = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-03/game_goals.csv')

# +
# filter top 8 scorers

top8 = (
    top250
    >> mutate(dense_rank=_.total_goals.rank(method="dense", ascending=False))
    >> filter(_.dense_rank < 10)
#     >> select(_.raw_rank, _.dense_rank, _.total_goals, _.player)
)

top8_games = game_goals >> inner_join(_, top8, "player")


# +
st.write("Goals by month")

st.write("Top 8 players not in our data")
top8 >> filter(_.yr_start < 1979)

# +
from pandas.tseries.offsets import MonthBegin
from siuba.experimental.pd_groups import fast_summarize

top8_goals = (
    top8_games
    >> mutate(
        date=_.date.astype("datetime64[D]"),
        age_years = top8_games.age.str.split('-').str.get(0).astype(int)
    )
    >> arrange(_.date)
    >> group_by(_.player, month=_.date - MonthBegin(1))
    >> fast_summarize(
        ttl_goals=_.goals.sum(),
        age_years = _.age_years.min()
    )
    >> group_by(_.player)
    >> mutate(cuml_goals=_.ttl_goals.cumsum())
    >> ungroup()
)

p_goals = alt.Chart(top8_goals).mark_line().encode(y="cuml_goals:Q", color = "player")

# +
time = st.selectbox("Choose a time", ["month", "age_years"])

st.write(
    p_goals.encode(x=time)
)

# +
st.write("Goals by seasons")

@st.cache
def data_season_goals():
    return pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-03/season_goals.csv')

season_goals = data_season_goals()
top8_seasons = season_goals.merge(top8, on = "player", suffixes = ['_season', '_player'])

top8_seasons['cuml_goals'] = top8_seasons.groupby('player')['goals'].cumsum()
top8_seasons['season_start'] = top8_seasons.season.str.split('-').str.get(0)


# +
y_val = st.selectbox("Choose y axis", ["cuml_goals", "goals", "assists", "points"])
x_val = st.selectbox("Choose x axis", ["age", "season_start"])

st.write(
    alt.Chart(top8_seasons).mark_line().encode(y=y_val, color = "player", x = x_val)
)
