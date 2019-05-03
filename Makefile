%.ipynb:
	# Re-runs notebook to produce output, then syncs Rmd
	jupyter nbconvert --ExecutePreprocessor.timeout=120 --to notebook --inplace --execute $@
	jupytext --sync $@
