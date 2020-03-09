#! /usr/bin/python
# function for checking weather at openweathermap
def check_weather():
# import required modules 
  import requests, json 
  # vars
  weather = dict()
  api_key = "8377d8a776a8827ff27f7626dbf332fb"
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  city_name = "Aartselaar" 
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
  #request data from API
  response = requests.get(complete_url) 
  responseJson = response.json() 

  # validate response
  if responseJson["cod"] != "404": 

    responseMain = responseJson["main"] 
    weather['status'] = "ok" 
    weather['temp'] = responseMain["temp"] 
    weather['pressure'] = responseMain["pressure"]
    responseWeather = responseJson["weather"] 
    weather['description'] = responseWeather[0]["description"] 
    weather['icon'] = responseWeather[0]["icon"] 

  

  else: 
    weather['status'] = "nok"
    
  return weather



