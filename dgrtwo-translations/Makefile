venv:
	. ~/.virtualenvs/tidytuesday-py/bin/activate

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

build: 2019-02-19-us_phds/us_phds_siuba-tabbed.html 2019-02-26-french-trains/french-trains-siuba-tabbed.html
	scp $^ dist

publish: build
	gh-pages -d dist

