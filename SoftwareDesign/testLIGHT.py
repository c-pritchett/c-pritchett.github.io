import time
import grovepi
from grovepi import *
from grove_rgb_lcd import *

#defining light sensor test as a function to use in the menu.py program
def test_light():
    light_sensor = 0   # connect light sensor to analog port 0
    threshold = 150    # threshold value fto control light sensor
    pinMode(light_sensor, "INPUT")	# setting the pin mode to input in order to take data from sensor
    
    while True:
        try:
            sensor_value = grovepi.analogRead(light_sensor)		# creating variable for value obtained from light sensor
            resistance = (float)(1023 - sensor_value) * 10 / sensor_value   # calculate resistance in sensor K

            setRGB(255,255,255)   #using lcd screen to for test info
            setText("Press CTRL + C\nwhen finished")

			# if-else loop containing dark/bright lighting conditions
            if resistance < threshold:
                print("Sensor indicates BRIGHT lighting conditions.")
            
            else:
                print("Sensor indicates DARK lighting conditions.")
            
            print("Sensor_value = %d, Resistance = %.2f" %(sensor_value, resistance))
            time.sleep(2.5)		# time delay: if sensor is read too quickly program can crash
            
        except KeyboardInterrupt:
            setText("Welcome to the\nWeather Center") #set default display message
            setRGB(255,255,255)
            break    
        
        except IOError:
            print ("Error")
            setRGB(255,255,255)
            setText("Error")