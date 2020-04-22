Translation of Dave Robinson's Tidy Tuesday Analyses
=======================================================

## Translations

✅: complete
❌: missing resources
🚧: in progress

| date       | name         | links | status |
| ---------- | ------------ | ----- | ------ |
| 2019-02-19 | us_phds      | | |

## FAQ

* how do you convert videos from .mov to mp4?

``` bash
ffmpeg -i movie.mov -vcodec copy -acodec copy out.mp4
```

* how do you add tabs to your notebooks?
    
    # In notebook.Rmd add this metadata (or add it to cell metadata in .ipynb)
    # I keep separate notebooks, then merge them with: 
    #   nbtabs copy-templates templates
    #   jupyter nbconvert --to html --template templates/nbtabs-full.tpl notebook_name.ipynb
    # Eg pytabs-1 with name R, will be matched with pytabs-1 in the other notebook

    ```{python pytabs={'class': 'pytabs-1', 'name': 'R'}}
    1 + 1
    ```

    ```{python pytabs={'class': 'pytabs-2', 'name': 'R'}}
    1 + 1
    ```

    # paste this code at the bottom (will work out better solution down the road)
    ```{python}
    def javascript(*st,file=None):
        from IPython.display import display, HTML
        if len(st) == 1 and file is None:
            s = st[0]
        elif len(st) == 0 and file is not None:
            s = open(file).read()
        else:
            raise ValueError('Pass either a string or file=.')
        display(HTML("<script type='text/javascript'>" + s + "</script>"))
        
    javascript(file = "../templates/puretabs.js")
    ```
    
    ```{python}
    %%html
    <script>
      window.onload = function() {
        //pureTabs.init();
        //pureTabs.init('tabs', 'tabs--active');
        for (let ii of Array(10).keys()) {
            pureTabs.init(`pytabs-${ii+1}`, 'tabs__link--active');
        }
      }
    </script>
    ```
    

## Contributing new translations

- [ ] new folder, named `{yyyy-mm-dd}-{dgrtwo_filename}`
- [ ] three notebooks or Rmd files, one for each version (siuba, python, original R)
- [ ] README.md with links to original tidytuesday entry, screencasts if applicable
- [ ] extra data retrieved for analysis clearly documented
- [ ] top of original Rmd and some part of README.md have clear attribution back to @dgrtwo

Checklist for creating a tabbed analysis:

- [ ] add build step to Makefile
- [ ] make sure result is copied to `dist` folder
- [ ] run `gh-pages -d dist` command
