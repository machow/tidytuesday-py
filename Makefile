%.ipynb:
	# Re-runs notebook to produce output, then syncs Rmd
	jupyter nbconvert --to notebook --inplace --execute $@
	jupytext --sync $@
