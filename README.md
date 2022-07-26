# sqlalchemy-challenge
Homework 10

### Part 1: 
In this section, Python and SQLAlchemy was used to perform basic climate analysis and data exploration of your climate database. Tthe following tasks by using SQLAlchemy ORM queries, Pandas, and Matplotlib were completed.

#### Climate Analysis and Exploration
* Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.
* Use SQLAlchemy’s create_engine to connect to your SQLite database.
* Use SQLAlchemy’s automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.
* Link Python to the database by creating a SQLAlchemy session.

#### Precipitation Analysis
* Find the most recent date in the dataset.
* Using this date, retrieve the previous 12 months of precipitation data by querying the 12 previous months of data. Note: Do not pass in the date as a variable to your query.
* Select only the date and prcp values.
* Load the query results into a Pandas DataFrame, and set the index to the date column.
* Sort the DataFrame values by date.
* Plot the results by using the DataFrame plot method.
* Use Pandas to print the summary statistics for the precipitation data.

#### Station Analysis
* Design a query to calculate the total number of stations in the dataset.
* Design a query to find the most active stations (the stations with the most rows).
* List the stations and observation counts in descending order.
* Which station id has the highest number of observations?
* Using the most active station id, calculate the lowest, highest, and average temperatures.
* Design a query to retrieve the previous 12 months of temperature observation data (TOBS).
* Filter by the station with the highest number of observations.
* Query the previous 12 months of temperature observation data for this station.
* Plot the results as a histogram with bins=12.



### Part 2: Design Your Climate App

In this section a Flask API was created based on the queries developed in Part 1.

The following routes were created:

* /
* /api/v1.0/precipitation
* /api/v1.0/stations
* /api/v1.0/tobs
