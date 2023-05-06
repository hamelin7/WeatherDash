#Greg Hamelin
#Elms - Data Structures - CIT3302
#Final Project

import os
import sys
import time
import adafruit_data
import OpenWeather_data

#use while loop to continuously check the 'zip-code-feed'
#set time.sleep to 5 seconds to not exceed the 30 data points per minute rate limit set by adafruit.io free API.
#we are sending 9 data points of weather data to our adafruit.io dashboard

def main():
  while True:
    #get the zipCode input by the user by calling the getZipCode function in adafruit_data.py
    zipCode = adafruit_data.getZipCode()
    #get current and forecast weather data by calling the getWeather function in OpenWeather_data.py
    currentWeather, forecastWeather = OpenWeather_data.getWeatherData(zipCode)
    #pass currentWeather and forecastWeather data to adafruit_data.py to be sent to our dashboard
    adafruit_data.postData(currentWeather, forecastWeather)
    
    time.sleep(20)
#end main 

main()