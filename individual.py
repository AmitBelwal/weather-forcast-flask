import requests
import calendar
import datetime
import math
import initialize
import os
import json


def first(r, place, lat, lon, i):
    weather = {}
    weather.update({'city': place})
    weather.update({'lat': lat})
    weather.update({'lon': lon})
    weather.update({'min_temp': math.ceil(r['daily'][i]['temp']['min'])})
    weather.update({'max_temp': math.ceil(r['daily'][i]['temp']['max'])})
    weather.update({'pressure': math.ceil(r['daily'][i]['pressure'])})
    weather.update({'humidity': math.ceil(r['daily'][i]['humidity'])})
    weather.update({'dew_point': math.ceil(r['daily'][i]['dew_point'])})
    weather.update({'wind_speed': math.ceil(r['daily'][i]['wind_speed'])})
    weather.update({'clouds': math.ceil(r['daily'][i]['clouds'])})
    weather.update({'uvi': math.ceil(r['daily'][i]['uvi'])})
    weather.update({'weather_type': r['daily'][i]['weather'][0]['main']})
    weather.update({'description': r['daily'][i]['weather'][0]['description']})
    weather.update({'icon': r['daily'][i]['weather'][0]['icon']})

    weather.update({'date': datetime.datetime.fromtimestamp(
        int(r['daily'][i]['dt'])).strftime('%Y-%m-%d')})
    weather.update({'weekday' + str(i): calendar.day_name[datetime.datetime.fromtimestamp(
        int(r['daily'][i]['dt'])).weekday()]})
    print('weather::::', weather)
    return weather
