from calendar import c
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
engine = create_engine("sqlite:///./Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)
#################################################
# Flask Setup

app = Flask(__name__)

#################################################
# Flask Routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Hawaiian Climate Analysis API <br/> "
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():

    #Query the data
    prcp_data = session.query(Measurement.date, Measurement.prcp).\
                  filter(Measurement.date >= dt.date(2016,8,23)).all()

    session.close()

# Convert the query results to a dictionary using date as the key and prcp as the value.
    precip_dict = {date: prcp for date, prcp in prcp_data}


# Return the JSON representation of your dictionary.
    return jsonify(precip_dict)    
    

# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():

    #Query the data
    station_data = session.query(Station.station).all()

    session.close()

    station_list = list(np.ravel(station_data))

    return jsonify(station_list)

# Query the dates and temperature observations of the most active station for the previous year of data.

@app.route("/api/v1.0/tobs")
def tobs():

     session = Session(engine)

     earliest_date = dt.date(2017,8,23)
     latest_date = earliest_date - dt.timedelta(days=365)

     tobs_active = session.query(Measurement.date, Measurement.tobs).filter_by(station="USC00519281").\
        filter(Measurement.date >= latest_date).all()

     session.close

# Return a JSON list of temperature observations (TOBS) for the previous year.

     tobs_list = []
     for date, tobs in tobs_active:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)

     return jsonify(tobs_list)


if __name__ == '__main__':
    app.run(debug=True)
