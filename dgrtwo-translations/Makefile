#TODO: clean up using standard format <dirname>/tabbed-analysis.html, and root templates dir
#      will still need to copy in custom.css. See board games conversion

NOTEBOOKS=2019-02-19-us_phds/us_phds_siuba-tabbed.html 2019-02-26-french-trains/french-trains-siuba-tabbed.html \
		  2019-03-05-women-workplace/women-workplace-siuba-tabbed.html 2019-03-12-board-games/tabbed-analysis.html


venv:
	. ~/.virtualenvs/tidytuesday-py/bin/activate

templates:
	nbtabs copy-templates templates

2019-02-19-us_phds/us_phds_siuba-tabbed.html: 2019-02-19-us_phds
	rm -r "./$</templates"
	nbtabs copy-templates "./$</templates"
	scp "./$</templates/custom.css" "./$<"
	cd "$<" && nbtabs convert -e us_phds_siuba.ipynb us_phds.Rmd us_phds_pandas.ipynb
	jupyter nbconvert --to html --template "$</templates/nbtabs-full.tpl" "$</us_phds_siuba-tabbed.ipynb"

2019-02-26-french-trains/french-trains-siuba-tabbed.html: 2019-02-26-french-trains
	rm -rf "./$</templates"
	nbtabs copy-templates "./$</templates"
	scp "./$</templates/custom.css" "./$<"
	cd "$<" && nbtabs convert -e --out french-trains-siuba-tabbed.ipynb french-trains-siuba.Rmd french-trains.Rmd
	jupyter nbconvert --to html --template "$</templates/nbtabs-full.tpl" "$</french-trains-siuba-tabbed.ipynb"

2019-03-05-women-workplace/women-workplace-siuba-tabbed.html: 2019-03-05-women-workplace
	rm -rf "./$</templates"
	nbtabs copy-templates "./$</templates"
	scp "./$</templates/custom.css" "./$<"
	cd "$<" && nbtabs convert -e --out women-workplace-siuba-tabbed.ipynb women-workplace-siuba.Rmd women-workplace.Rmd
	jupyter nbconvert --to html --template "$</templates/nbtabs-full.tpl" "$</women-workplace-siuba-tabbed.ipynb"

2019-03-12-board-games/tabbed-analysis.html: 2019-03-12-board-games
	cd "$<" && nbtabs convert -e --out tabbed-analysis.ipynb board-games-siuba.Rmd board-games.Rmd
	jupyter nbconvert --to html --template templates/nbtabs-full.tpl "$</tabbed-analysis.ipynb"
	


build: $(NOTEBOOKS)
	scp $^ dist

publish: build
	gh-pages -d dist

