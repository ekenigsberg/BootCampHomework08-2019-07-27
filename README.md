# BootCampHomework08-2019-07-27

[Jupyter Notebook Solution](https://nbviewer.jupyter.org/github/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/climate_starter.ipynb)<br/>
and<br/>
[Python/Flask Code](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/app.py)<br/>
to<br/>
[Data Analytics Boot Camp Homework #8](https://github.com/the-Coding-Boot-Camp-at-UT/UTAMCB201904DATA3/blob/master/10-Advanced-Data-Storage-and-Retrieval/Homework/Instructions/README.md)

# Screenshots: Jupyter Notebook
## Precipitation by Date
![Precipitation by Date](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/Precip%20by%20Date.png)
## Temperature Histogram
![Temperature Histogram](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/Temp%20Histogram.png)
## Trip Average Temperature
![Trip Average Temperature](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/Trip%20Avg%20Temp.png)
## Bonus: Low, Avg, and High Temperatures
![Bonus: Low, Avg, and High Temperatures](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/Low%2C%20Avg%2C%20and%20High%20Temps.png)

# Screenshots: Flask App
## Home Page
![Home Page](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/output/API%201.%20home.png)
## Precipitation Dictionary
![Precipitation Dictionary](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/output/API%202.%20precipitation.png)
## Station List
![Station List](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/output/API%203.%20stations.png)
## Temperature by Day
![Temperature by Day](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/output/API%204.%20tobs.png)
## Low, Avg, and High with Start Date Specified
![Low, Avg, and High with Start Date Specified](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/output/API%205.%20start.png)
## Low, Avg, and High with Start and End Dates Specified
![Low, Avg, and High with Start and End Dates Specified](https://github.com/ekenigsberg/BootCampHomework08-2019-07-27/blob/master/output/API%206.%20start%20end.png)

# Technical Insights

* I'm sure that the `connect_args={'check_same_thread': False}` line I added to my create_engine call is not something that can be done in a production environment. I don't know how to address the **"SQLite objects created in a thread can only be used in that same thread"** errors, so I'm leaving it for now.
* My Jupyter Notebook isn't previewing in GitHub, so the link above displays the GitHub file through https://nbviewer.jupyter.org instead.
