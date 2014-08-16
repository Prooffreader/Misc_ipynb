Misc_ipynb
==========

A collection of ipython notebooks I've made for various projects

monty_monte.ipynb: A Monte Carlo simulator of the Monty Hall problem! You can choose the number of doors and of goats, and the number of iterations.

pocket_tumblr_reddit_api.ipynb: A script to search the hard drive, Pocket or Tumblr for photos, then save them or upload them to Tumblr or Reddit. The Reddit posting writes to a json on an sftp server, where a cron job can run the Reddit/PRAW script once an hour.

weather_ML.ipynb: a script to analyze a huge (7,000,000-row) table of weather data that had lost its column identifiers and changed column order frequently. I used conservative criteria to assign unambiguous columns (e.g., only rainfall had numbers in the 0.00-0.10 range, snowfall was NULL during July), and then used machine learning (random forest classifier) to classify the rest based on a handful of metrics, like whether values were correlated with time of year or time of day, how many had a value of zero, whether they were integers or floats, their medians and standard deviations, etc. The source data is proprietary, so is not included here.
