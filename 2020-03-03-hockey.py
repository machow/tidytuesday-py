# +
import pandas as pd
from qgrid import show_grid
from siuba import _, mutate, summarize, filter, group_by, select, inner_join, distinct, count, ungroup, arrange
import altair as alt

game_goals = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-03/game_goals.csv')
top250 = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-03/top_250.csv') \
    .rename(columns = {'total_games': 'total_goals'})


# +
from siuba.dply.vector import dense_rank

# dense_rank??

# +
# filter top 8 scorers

top8 = (
    top250
    >> mutate(dense_rank=_.total_goals.rank(method="dense", ascending=False))
    >> filter(_.dense_rank < 10)
#     >> select(_.raw_rank, _.dense_rank, _.total_goals, _.player)
)

# -

top8 >> filter(_.yr_start < 1979)

# +
# get them from game_goals

top8_games = game_goals >> inner_join(_, top8, "player")

games_per_year = (
    top8_games
#    >> filter(_.player == "Alex Ovechkin")
    >> count(_.player, year=_.date.astype("datetime64[D]").dt.year.astype(str))
    >> group_by(_.player)
    >> mutate(
        cuml_games = _.n.cumsum(),
    )
    >> ungroup()
)

alt.Chart(games_per_year).mark_line().encode(x = 'year:T', y = 'cuml_games', color = "player")
# -





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
# -

p_goals.encode(x="month")

p_goals.encode(x="age_years")

# 'Gordie Howe', 'Marcel Dionne', 'Phil Esposito'
sorted(top8.player)
