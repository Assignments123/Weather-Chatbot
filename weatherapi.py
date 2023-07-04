import os
import requests

class WeatherResponse:
    def __init__(self) -> None:
        self.appid = os.getenv('APPID')
        self.response = {}

    def weatherreport(self,city_name):
        # unit in metric for getting temperature in celcius
        url = 'https://api.openweathermap.org/data/2.5/weather?'
        params = {
            "q":city_name,
            "appid":self.appid,
            "units":"metric",
        }
        resp = requests.get(url,params=params).json()
        self.response.update(resp)
        return self.response


# def weatherreport(cityname):
#     city_name = cityname
#     appid = os.getenv('APPID')

#     # unit in metric for getting temperature in celcius
#     url = 'https://api.openweathermap.org/data/2.5/weather?'
#     params = {
#         "q":city_name,
#         "appid":appid,
#         "units":"metric",
#     }
#     resp = requests.get(url,params=params).json()
#     print("response of weather api is : ",resp)
#     # if resp.get('cod')==401:
#     #             data = {
#     #                 "status":"error",
#     #                 "message":"Please provide correct city name"
#     #             }
#     return resp