from flask import Flask
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
import numpy as np

from flask import Flask, jsonify
app = Flask(__name__)

engine = create_engine("sqlite:///Resources/hawaii.sqlite/")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

@app.route("/")
def index():
    return(
        f"SQL Alchemy Challenge Homework<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

@app.route("/api/v1.0/precipitation")
def precip():
    session = Session(engine)
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date).all()
    session.close()

    precip_list = []
    for date, precipitation in results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["precipitation"] = precipitation
        precip_list.append(precip_dict)
    
    return jsonify(precip_list)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()

    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    session = Session(engine)
    most_active = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= query_date).all()
    session.close()

    tob = list(np.ravel(most_active))
    return jsonify(tob)


session = Session(engine)
last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
session.close()

@app.route("/api/v1.0/<start>/<end>")
@app.route("/api/v1.0/<start>")

def range(start, end = last_day):
   
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start, Measurement.date <= end).all()
    session.close()

    min_temp = list(np.ravel(results))
    return jsonify(min_temp)


if __name__ == "__main__":
    app.run(debug=True)
