Misc_ipynb
==========

A collection of ipython notebooks I've made for various projects, with nbviewer links:

Scripts to make maps of Canadian Centre for Climate Modeling and Analysis climate models to the year 2100:
[CCCma_Basemap.ipynb](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/CCCma/CCCma_Basemap.ipynb) Script to visualize one such map
[CCCma_SNC_to_2099.ipynb](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/CCCma/CCCma_SNC_to_2099.ipynb) Script to extract a feature on the same day per year and make an animated GIF

[earthquakes-jp.ipynb](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/Japan_Earthquakes/earthquakes-jp.ipynb) and [earthquakes-rest-api.py](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/earthquakes-jp.ipynb): Scripts to build an animated GIF of earthquakes in China and Japan. See the final result at http://www.prooffreader.com/2014/06/Japan_Earthquakes/animated-map-of-earthquakes-near-china.html

Scripts to analyze Billboard magazine pop charts data:
[billboard_top_words.ipynb](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/billboard_charts/billboard_top_words.ipynb) : script to find the most decade-specific words in song titles since 1890.

[monty_monte.ipyn](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/monty_monte.ipynb): A Monte Carlo simulator of the Monty Hall problem! You can choose the number of doors and of goats, and the number of iterations.

[pocket_tumblr_reddit_api.ipynb](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/pocket_tumblr_reddit_api.ipynb): A script to search the hard drive, Pocket or Tumblr for photos, then save them or upload them to Tumblr or Reddit. The Reddit posting writes to a json on an sftp server, where a cron job can run the Reddit/PRAW script once an hour.

[top_10_python_idioms.ipynb](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/top_10_python_idioms.ipynb): A notebook showing the top 10 idioms I wished I'd internalized earlier when I was first learning Python in 2012 coming from mostly Visual Basic (ugh, I know!).

Scripts to convert tree/graph files between a few formats for use in MEGA or Gephi: (1) [tree_convert_mega_to_gexf.ipynb](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/tree_convert_mega_to_gexf.ipynb); (2) [tree_convert_mega_to_json.ipynb](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/tree_convert_mega_to_json.ipynb); (3) [tree_convert_newick_to_json.py](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/tree_convert_newick_to_json.ipynb) 

[weather_ML.ipyn](http://nbviewer.ipython.org/github/Prooffreader/Misc_ipynb/blob/master/weather_MLp.ipynb)b: a script to analyze a huge (7,000,000-row) table of weather data that had lost its column identifiers and changed column order frequently. I used conservative criteria to assign unambiguous columns (e.g., only rainfall had numbers in the 0.00-0.10 range, snowfall was NULL during July), and then used machine learning (random forest classifier) to classify the rest based on a handful of metrics, like whether values were correlated with time of year or time of day, how many had a value of zero, whether they were integers or floats, their medians and standard deviations, etc. The source data is proprietary, so is not included here.
