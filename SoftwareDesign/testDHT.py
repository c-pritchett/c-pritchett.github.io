import grovepi
import math
from grove_rgb_lcd import *

#defining DHT sensor test as a function to use in the menu.py program
def test_dht():
    sensor = 8  # The Sensor goes on digital port 8.
    # Grove Base Kit comes with the blue sensor.
    blue = 0    # The Blue colored sensor.
    
    setRGB(255,255,255)   #using lcd screen to for test info
    setText("Press CTRL + C\nwhen finished")

    while True:
        try: 
            [temp,humidity] = grovepi.dht(sensor,blue)   # The first parameter is the port, the second parameter is the type of sensor.
            temp = ((temp / 5.0) * 9) + 32
            
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                print("Temperature = %.02f F, Humidity = %.02f%%"%(temp, humidity))
                
            time.sleep(2.5)    # time delay: if sensor is read too quickly program can crash

        except KeyboardInterrupt:
            setText("Welcome to the\nWeather Center") #set default display message
            setRGB(255,255,255)
            break
            
        except IOError:
            print ("Error")
            setGRB(255,255,255)
            setText("Error")