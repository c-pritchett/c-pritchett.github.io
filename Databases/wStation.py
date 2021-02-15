import grovepi
import math
import time
import json
import datetime
from grove_rgb_lcd import *
from grovepi import *


def w_station():
    sensor = 8   # DHT sensor connected to port d4 on grovepi
    blue = 0     # The Blue DHT sensor
    
    data = {}    # Create data structure outside loop
    data2 = {}
    data['DAYtime'] = []    # storage for daylight values
    data2['NIGHTtime'] = []   # Storage for dark values
    
    light_sensor = 0   # light sensor attached to analog 0
    threshold = 150     # light sensor threshold for ambient light
    pinMode(light_sensor, "INPUT")   # setting light sensor to input

    setRGB(255,255,255)   # set starting LCD light color to white
    setText("Starting Weather\nStation...")   # set starting message
    time.sleep(1.5)   #small delay, grovepi modules can fail to respond when program loads too quickly

    while True:
        try:
            timestamp = (time.time() * 1000)   #to convert python datetime to JS date time, you must multiply by 1000
            
            [temp,humidity] = grovepi.dht(sensor,blue)   #Get the temperature and Humidity from the DHT Sensor.
            sensor_value = grovepi.analogRead(light_sensor)   # acquire value from light sensor
            
            temp = ((temp * 9) / 5.0) + 32   #Conversion from Celsius to Fahrenheit 
            resistance = (float)(1023 - sensor_value) * 10 / sensor_value   # calculate resistance in sensor K
        
            t = str(temp)
            h = str(humidity)
        
            setText("Temp: " + t + " F\n" + "Humidity: " + h + "%") # Displaying all the data to the backlight.
    
            
            if resistance < threshold:
                print("Currently day light hours.")
                print("Temperature = %.02f F, Humidity = %.02f%%"%(temp, humidity))
                
                data['DAYtime'].append([temp, humidity, timestamp])
                
                with open('day.json', 'w') as outfile:
                    json.dump(data['DAYtime'], outfile)
            
            else:
                print("Not day light hours.")
                print("Temperature = %.02f F, Humidity = %.02f%%"%(temp, humidity))
                
                data2['NIGHTtime'].append([temp, humidity, timestamp])
                
                with open('night.json', 'w') as outfile:
                    json.dump(data2['NIGHTtime'], outfile)
                    
            #if-else loop for temp and humidity data illuminating the LEDs
            if (temp > 60 and temp < 85) and humidity < 80:
                setRGB(0,255,0)
            
            elif (temp > 85 and temp < 95) and humidity < 80:
                setRGB(255,255,0)
            
            elif temp > 95:
                setRGB(255,0,0)
            
            elif temp < 60:
                setRGB(0,0,255)
            
            elif humidity > 80:
                setRGB(255,0,255)
        
            time.sleep(2.5) 
        
        except KeyboardInterrupt:
            setRGB(255,255,255)     #set LCD screen to default white
            setText("Welcome to the\nWeather Center") #set default display message
            break    
        
        except IOError:
            print ("Error")
            setRGB(255,255,255)
            setText("Error")
