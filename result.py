import requests
import calendar
import datetime
import math
import initialize
import os
import json


def getJson(r, find):
    i = 0
    weather = {}
    weather.update({'city': find.Place})
    weather.update({'lat': r['lat']})
    weather.update({'lon': r['lon']})
    while i < 8:
        weather.update({'min_temp' + str(i): math.ceil(r['daily'][i]['temp']['min'])})
        weather.update({'max_temp' + str(i): math.ceil(r['daily'][i]['temp']['max'])})
        weather.update({'pressure' + str(i): math.ceil(r['daily'][i]['pressure'])})
        weather.update({'humidity' + str(i): math.ceil(r['daily'][i]['humidity'])})
        weather.update({'dew_point' + str(i): math.ceil(r['daily'][i]['dew_point'])})
        weather.update({'wind_speed' + str(i): math.ceil(r['daily'][i]['wind_speed'])})
        weather.update({'clouds' + str(i): math.ceil(r['daily'][i]['clouds'])})
        weather.update({'uvi' + str(i): math.ceil(r['daily'][i]['uvi'])})
        weather.update({'weather_type' + str(i): r['daily'][i]['weather'][0]['main']})
        weather.update({'description' + str(i): r['daily'][i]['weather'][0]['description']})
        weather.update({'icon' + str(i): r['daily'][i]['weather'][0]['icon']})

        weather.update({'date' + str(i): datetime.datetime.fromtimestamp(
            int(r['daily'][i]['dt'])).strftime('%Y-%m-%d')})
        weather.update({'weekday' + str(i): calendar.day_name[datetime.datetime.fromtimestamp(
            int(r['daily'][i]['dt'])).weekday()]})
        i += 1

    print('weather::::', weather)
    return weather
