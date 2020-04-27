[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/machow/tidytuesday-py/master)

## Tidy Tuesday: Translations from R to Python

| date | name | links |
| ---- | ---- | ------ |
| 2019-02-19 <a name="toc-us-phds"></a> | US Phds | [notebook](https://mchow.com/tidytuesday-py/us_phds_siuba-tabbed.html) \|  [folder](/dgrtwo-translations/2019-02-19-us_phds) |
| 2019-02-26 <a name="toc-trains"></a> | French Trains | [notebook](https://machow.github.io/tidytuesday-py/french-trains-siuba-tabbed.html) \| [screencast](https://youtu.be/jP_WXc9GV4k) \| [folder](/dgrtwo-translations/2019-02-26-french-trains) | 
| 2019-03-05 <a name="toc-women-workforce"></a> | Women in the Workforce | [notebook](https://mchow.com/tidytuesday-py/women-workplace-siuba-tabbed.html) \| [screencast](https://youtu.be/zjRTpYK9TRk) \| \| [folder](/dgrtwo-translations/app-2019-03-05-women-workplace) \| [folder (app)](/dgrtwo-translations/app-2019-03-05-women-workplace) | 
| 2019-03-12 <a name="toc-board-games"></a> | Board Games | [notebook](https://mchow.com/tidytuesday-py/2019-03-12-board-games-tabbed.html) \| [screencast](https://youtu.be/UXjaRB9pJ8o) \| \| [folder](/dgrtwo-translations/2019-03-12-board-games) | 

## Tidy Tuesday: Hour-long Python Analyses

| date | name | links |
| ---- | ---- | ------ |
| 2020-03-03 <a name="toc-hockey"></a> | Hockey Goals | [notebook](https://github.com/machow/tidytuesday-py/blob/master/2020-03-03-hockey.py) \| [dashboard](https://github.com/machow/tidytuesday-py/blob/master/2020-03-03-hockey-streamlit.py) \| [screencast](https://youtu.be/rXuAVLltD3I) |
| 2020-04-21 <a name="toc-gdpr"></a> | GDPR fines | [notebook](https://github.com/machow/tidytuesday-py/blob/master/2020-04-21-gdpr.ipynb) |

## Frequently Asked Questions

### How do you create tabbed notebooks?

I made a quick library called nbtabs! https://github.com/machow/nbtabs. It haven't put much into documenting and sharing it, but if you're interested in using it, let me know.

### Why screencast?

Screencasting is very similar to a method used in expertise research called the [think-aloud method](https://en.wikipedia.org/wiki/Think_aloud_protocol). This method is very helpful for understanding how novices and experts approach different problems. With written tutorials, learners don't get to see all the effort people put into figuring out the final code. This is very different from the real world, where data scientists are constantly dealing with surprising and unexpected aspects of their data!

dependencies
------------

Generally, most notebooks use...

* `qgrid` (requires manual step)
* `ipywidgets` (requires manual step)
* `pandas`
* `plotnine`

However, all dependencies can be found in `requirements.txt`, and installed using...

```
pip install -r requirements.txt
```
