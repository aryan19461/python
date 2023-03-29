'''
'http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=bulk'
API key : 2cd0b6bdf3eb450b8d1145046232903 

key expires on  12 April 2023
'''
import os
import json
import requests
import win32com.client as say
city = input('Enter city name : \n')
url = f'http://api.weatherapi.com/v1/current.json?key=2cd0b6bdf3eb450b8d1145046232903&q={city}'

r =requests.get(url)
# print(r.text)
weather_dictionary = json.loads(r.text)
speak = say.Dispatch('SAPI.SpVoice')
sayitman = weather_dictionary['current']['temp_c']
speak.speak(f'Current temperature in {city} is {sayitman} degrees')

