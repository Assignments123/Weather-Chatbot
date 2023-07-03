from flask import Flask , render_template , request
import weatherapi
from witcode import extractinfo

chatbot = Flask(__name__)


@chatbot.route('/')
def index():
    
    return render_template('index.html')


@chatbot.route('/weatherbyname',methods=['GET','POST'])
def weatherbyname():
    '''
    The function to get temperature, humidity, winds, cloud, sunrise and sunset time of specific city
    '''
    try:
        data = request.json

        usertext = data['usertext']        
        
        response = extractinfo(usertext)



        intent = response['intents'][0]['name']

        if intent == "greet":
            data = {
                "status":"success",
                "message":"Hey...Good to see you!! How can i help you"
            }
            return data
        
        elif intent == "help":
            data = {
                "status":"success",
                "message":"Hello, I'm Weather Chatbot,\
                and I'm here to provide you with accurate weather information.\
                Please let me know the name of the city\
                for which you'd like to receive weather updates"
            }
            return data

        elif intent == "user_introduction":

            username = response['entities']['users_name:users_name'][0]['body']
            print("username is : ",username)
            data = {
                "status":"success",
                "message":f"Hello {username}, How can i Assist you today?"
            }
            return data
        
        elif intent == "appreciation":
            
            data = {
                "status":"success",
                "message":"I'm delighted to hear that I've been able to assist you!\
                Helping users like you is what I'm here for.\
                If you have any more questions or need further assistance,\
                don't hesitate to ask. I'm always here to help."
            }
            return data
        
        elif intent == "weather_question":
            
            cityname = response['entities']['city:city'][0]['body']
            print("cityname is : ",cityname)
            resp = weatherapi.weatherbyname(cityname)

            # check if getting correct response or not
            if resp.get('cod')!=200:
                data = {
                    "status":"error",
                    "message":"Please provide correct city name"
                }

            else:

                temp = resp.get('main').get('temp')
                humidity = resp.get('main').get('humidity')
                windspeed = resp.get('wind').get('speed')
                cloud = resp.get('clouds').get('all')

                data = {
                        "status":"success",
                        "message":f"temperature of {cityname} is  :\
                        {temp} ,windspeed is {windspeed} ,\
                        cloud is {cloud} and humidity is : {humidity}\
                        how can i further assist you?",
                        
                    }
                return data
            
        elif intent == "wit$check_weather_condition":
            
            cityname = response['entities']['city:city'][0]['body']
            print("cityname is : ",cityname)
            resp = weatherapi.weatherbyname(cityname)

            # check if getting correct response or not
            if resp.get('cod')!=200:
                data = {
                    "status":"error",
                    "message":"Please provide correct city name"
                }

            else:

                temp = resp.get('main').get('temp')
                humidity = resp.get('main').get('humidity')
                windspeed = resp.get('wind').get('speed')
                cloud = resp.get('clouds').get('all')

                data = {
                        "status":"success",
                        "message":f"temperature of {cityname} is  :\
                        {temp} ,windspeed is {windspeed} ,\
                        cloud is {cloud} and humidity is : {humidity}\
                        how can i further assist you?",
                        
                    }
                return data
    except Exception:
        data = {
                    "status":"error",
                    "message":f"Sorry I did not understand what you said...\
                    I can give you weather report of any city\
                    for that provide me name of city.",
                    
                }
        return data
    return data


if __name__ == '__main__':
    chatbot.run(debug=True)
