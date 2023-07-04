from wit import Wit
import os

class WitResponse:
    def __init__(self) -> None:
        self._token = os.getenv('ACCESS_TOKEN')
        self.client = Wit(self._token)
        self.info = {}

    def extractuserinfo(self, userinput):
        resp = self.client.message(userinput)
        self.info.update(resp)
        return self.info

# def extractinfo(usertext):
#     access_token = os.getenv('ACCESS_TOKEN')
#     print("access_token is :",access_token)
#     client = Wit(access_token = access_token)
#     resp = client.message(usertext)
#     print("resp is :",resp)
#     return resp
