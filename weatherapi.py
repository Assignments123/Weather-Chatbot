import os
import requests

def weatherbyname(cityname):
    city_name = cityname
    appid = os.getenv('APPID')

    # unit in metric for getting temperature in celcius
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {
        "q":city_name,
        "appid":appid,
        "units":"metric",
    }
    resp = requests.get(url,params=params).json()
    return resp