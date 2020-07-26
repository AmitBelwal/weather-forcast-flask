from flask import Flask, render_template, redirect, session, request
from flask_sqlalchemy import SQLAlchemy
import _cffi_backend
import individual
import result
import url
import requests
import calendar
import datetime
import math
import initialize
import os
import json

cwd = os.getcwd()

with open(f'{cwd}/templates/config.json', 'r') as file:
    params = json.load(file)['parameters']
local_server = params['local_server']
app = Flask(__name__)
app.config['DEBUG'] = True

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
db = SQLAlchemy(app)


class Location(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Place = db.Column(db.String, nullable=False)
    Longitude = db.Column(db.String, nullable=True)
    Latitude = db.Column(db.String, nullable=True)


@app.route('/')
def index():
    r = url.initial_url()
    print(r)
    weather = initialize.init(r)
    return render_template("index.html", params=params, weather=weather)


@app.route('/location', methods=['GET', 'POST'])
def location():
    loc = request.form.get('location')
    find = Location.query.filter_by(Place=loc).first()
    r = url.find_url(find)
    weather = result.getJson(r, find)
    return render_template("index.html", params=params, weather=weather)


@app.route('/individual/<string:lat>/<string:lon>/<string:place>/<string:i>', methods=['GET', 'POST'])
def first(lat, lon, place, i):
    i = int(i)
    r = url.individual_url(lat, lon)
    weather = individual.first(r, place, lat, lon, i)
    return render_template("first.html", params=params, weather=weather)


if __name__ == '__main__':
    app.run(host=’0.0.0.0′,port=8080, debug=True)
