from wit import Wit
import os

def extractinfo(usertext):
    access_token = os.getenv('ACCESS_TOKEN')
    print("access_token is :",access_token)
    client = Wit(access_token = access_token)
    # message_text = "what can you do for me"
    resp = client.message(usertext)
    print("resp is :",resp)
    return resp


# class WitRespos:
#     def __init__(self) -> None:
#         self._token = access_token
#         self.info = {}

#     def extractuserinfo(self, userinput):
#         inent= 
#         if itnetn == "weather":
#             self.infor.update({"city":response
#         return intern, confidence


# class WeatherBot:
#     def __init__:
#     self.name = None
#     self.wit = WitRespos()

#     def generate_response(self, userinput):
#         intent, _ = self.wit.extractinfo(userinput)
#         if self.name == None:
#             return ""