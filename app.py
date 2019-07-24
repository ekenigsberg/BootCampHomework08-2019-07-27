# import all needed libs
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# THE FOLLOWING CODE WAS COPIED, WITH SOME VARIATIONS, FROM THE COMPLETED JUPYTER NOTEBOOK 'CLIMATE_STARTER'
# I bet that setting 'check_same_thread' to False is unacceptable in a enterprise-
# strength, multi-threaded environment. I don't yet know enough how to avoid the 
# 'SQLite objects created in a thread can only be used in that same thread' errors
eng = create_engine('sqlite:///Resources/hawaii.sqlite', connect_args={'check_same_thread': False})
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(eng, reflect=True)
# Save references to each table
clsMes = Base.classes.measurement
clsSta = Base.classes.station
# Create our session (link) from Python to the DB
ses = Session(eng)
# Create a connection to the DB
conn=eng.connect()

# SOME COMMON QUERIES ARE KEPT IN THE BODY OF APP.PY INSTEAD OF WITHIN FUNCTIONS
# Perform a query to retrieve the data and precipitation scores
# "LTM" = "Last Twelve Months"
strSQL_LTM = 'SELECT m.id, m.date, m.prcp, m.tobs, s.station, s.name, s.latitude, s.longitude, s.elevation ' + \
			 'FROM measurement m ' + \
			 'INNER JOIN station s on m.station = s.station ' + \
			 'WHERE date >= "2016-08-23"'
# Save the query results as a Pandas DataFrame and set the index to the date column
dfLTM = pd.read_sql(strSQL_LTM, conn)
# Sort the dataframe by date
dfLTM = dfLTM.sort_values('date')
# Drop precipitation column NaNs
dfLTM = dfLTM.dropna(subset=['prcp'], thresh=1)

# Design a query to show how many stations are available in this dataset
strSQL_Stn = 'SELECT station, count(id) AS stncount ' + \
			 'FROM measurement m ' +\
			 'GROUP BY station ' + \
			 'ORDER BY stncount DESC'
lstStn = eng.execute(strSQL_Stn).fetchall()
lstStnClean = [row[0] for row in lstStn]

# This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates
def calc_temps(start_date, end_date='2017-08-23'):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return ses.query(func.min(clsMes.tobs), func.avg(clsMes.tobs), func.max(clsMes.tobs)).\
           filter(clsMes.date >= start_date).filter(clsMes.date <= end_date).all()


#################################################
# Flask Setup
#################################################
app=Flask(__name__)
#################################################
# Flask Routes
#################################################
@app.route('/')
def home():
    print('Server received request for Home page')
    return 'The following pages are set up on this server:<br/>' + \
		   '<a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a><br/>' + \
		   '<a href="/api/v1.0/stations">/api/v1.0/stations</a><br/>' + \
		   '<a href="/api/v1.0/tobs">/api/v1.0/tobs</a><br/>' + \
		   '<a href="/api/v1.0/&lt;start&gt;">/api/v1.0/&lt;start&gt;</a><br/>' + \
		   '<a href="/api/v1.0/&lt;start&gt;/&lt;end&gt;">/api/v1.0/&lt;start&gt;/&lt;end&gt;</a>'

@app.route('/api/v1.0/precipitation')
def precipitation():
	print('Server received request for precipitation page (JSON)')
	# Summarize the LTM data for a cleaner graph
	# "LTMSumm" = "Last Twelve Months Summary"
	dfLTMSumm = dfLTM.filter(items=['date', 'prcp'])
	grpLTMSumm = dfLTMSumm.groupby('date')
	dfLTMSumm = grpLTMSumm.mean()
	# create dict from dfLTMSumm
	dictLTMSumm = dfLTMSumm.to_dict(orient='dict')
	return jsonify(dictLTMSumm['prcp'])

@app.route('/api/v1.0/stations')
def stations():
	print('Server received request for stations page (JSON)')
	return jsonify(lstStnClean)

@app.route('/api/v1.0/tobs')
def tobs():
	print('Server received request for tobs page (JSON)')
	# store the Most Active Station as a variable
	# "MAS" = "Most Active Station"
	strMAS = lstStn[0][0]
	# Choose the station with the highest number of temperature observations.
	# Query the last 12 months of temperature observation data for this station and plot the results as a histogram
	# "LTMMAS" = "Last Twelve Months, Most Active Station"
	dfLTMMAS = dfLTM[dfLTM['station'] == strMAS]
	# create average tobs for each date
	grpLTMMAS = dfLTMMAS.groupby('date')
	dfLTMMAS = grpLTMMAS.mean()
	# chop LTMMAS down to date and tobs
	dfLTMMAS = dfLTMMAS.filter(items=['date', 'tobs'])
	# create dict from dfLTMMAS
	dictLTMMAS = dfLTMMAS.to_dict(orient='dict')
	return jsonify(dictLTMMAS['tobs'])

@app.route('/api/v1.0/<start>')
def startdate(start):
	print('Server received request for startdate page (JSON)')
	# When given the start only, calculate TMIN, TAVG, and TMAX for all 
	# dates greater than and equal to the start date.
	if start <= '2017-08-23' and start >= '2010-01-01':
		lstTmp = calc_temps(start)
		return jsonify(lstTmp)
	else:
		return jsonify({'error': 'your start date should be between 2010-01-01 and 2017-08-23.'}), 404

@app.route('/api/v1.0/<start>/<end>')
def startenddate(start, end):
	print('Server received request for startenddate page (JSON)')
	# When given the start and the end date, calculate the TMIN, TAVG, 
	# and TMAX for dates between the start and end date inclusive.
	if start <= '2017-08-23' and start >= '2010-01-01' and \
	   end <= '2017-08-23' and end >= '2010-01-01':
		lstTmp = calc_temps(start, end)
		return jsonify(lstTmp)
	else:
		return jsonify({'error': 'all dates should be between 2010-01-01 and 2017-08-23.'}), 404

if __name__ == "__main__":
    app.run(debug=True)	