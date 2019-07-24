# BootCampHomework08-2019-07-27

[Jupyter Notebook Solution](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/climate_starter.ipynb)<br/>
and<br/>
[Python/Flask Code](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/app.py)<br/>
to<br/>
[Data Analytics Boot Camp Homework #8](https://github.com/the-Coding-Boot-Camp-at-UT/UTAMCB201904DATA3/blob/master/10-Advanced-Data-Storage-and-Retrieval/Homework/Instructions/README.md)

# Screenshots: Jupyter Notebook
* ![Precipitation by Date](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/Precip%20by%20Date.png)
* ![Temperature Histogram](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/Temp%20Histogram.png)
* ![Trip Average Temperature](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/Trip%20Avg%20Temp.png)
* ![Bonus: Low, Avg, and High Temperatures](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/Low%2C%20Avg%2C%20and%20High%20Temps.png)

# Screenshots: Flask App
* ![Home Page](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/output/API%201.%20home.png)
* ![Precipitation Dictionary](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/output/API%202.%20precipitation.png)
* ![Station List](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/output/API%203.%20stations.png)
* ![Temperature by Day](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/output/API%204.%20tobs.png)
* ![Low, Avg, and High with Start Date Specified](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/output/API%205.%20start.png)
* ![Low, Avg, and High with Start and End Dates Specified](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/output/API%206.%20start%20end.png)

# Technical Insights

* Transforming Latitude into Distance from Equator enables running linear regressions. The **ols()** method from the **statsmodels.formula.api** library produces nicely-formatted output from plain-English parameters like **'Y~A+B'**.
* Because all four analyses are essentially the same (just with different variables and graph boundaries), I created a function to spit out the graphs.
* I was tickled to learn that [the documentation tells us](https://matplotlib.org/users/colors.html) that Matplotlib accepts [color names](https://xkcd.com/color/rgb/) as determined in a survey conducted by the great, nerdy [comic strip xkcd](https://xkcd.com): just name the color with the **xkcd:** prefix and use plain English (eg, **'xkcd:purplish pink'**).
