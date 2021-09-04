# sqlalchemy-challenge

The climate_starter Jupyter Notebook reflects the tables in the hawaii.sqlite database for climate analysis and exploration.

The precipitation for the last 12 months from multiple weather stations is found an plotted on a chart.

The most active station is found, along with its lowest, highest, and average temperature.  The temperature for the last 12 months for this station is plotted in a histogram.

The app.py file will create a Flask API to return:

- `/`
  * List all routes that are available.
- `/api/v1.0/precipitation`
  * Date and precipitations values

- `/api/v1.0/stations`

  * List of stations from the dataset.
- `/api/v1.0/tobs`
  * Dates and temperature observations of the most active station for the last year of data.

- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
  * Minimum, average, and maximum temperature given a start date in the format yyyy-mm-dd.  End date is optional.


#### Bonus 1

The average temperatures in June and December across all stations is found for all years in the dataset.  A t-test is performed on the results.

#### Bonus 2

A temperature analysis is performed for the month of August.  The average temperature is plotted in a bar graph.  The daily average rainfall for each station is found.  And the minimum, average, and maximum temperature is plotted for a years in the dataset.