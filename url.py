import requests


def initial_url():
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&units=metric&exclude=current,hourly,minutely&appid=1f170f6e926c39a5239ffa55f36a1f6d"
    r = requests.get(url.format()).json()
    return r


def find_url(find):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=metric&exclude=current,hourly,minutely&appid=1f170f6e926c39a5239ffa55f36a1f6d"

    r = requests.get(url.format(find.Longitude, find.Latitude)).json()
    print(r)
    return r


def individual_url(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=metric&exclude=current,hourly,minutely&appid=1f170f6e926c39a5239ffa55f36a1f6d"
    r = requests.get(url.format(lat, lon)).json()
    print(r)
    return r
