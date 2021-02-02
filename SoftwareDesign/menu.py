import sys
import csv
from grove_rgb_lcd import *
import wStation
import testLCD
import testDHT
import testLIGHT


#sets LCD screen
setRGB(255,255,255)
setText("Initializing...")

#define main function
def main():
    menu()
     
#define menu function	 
def menu():
    print("Select an Option")
    
    choice = input("""
                        A) Run Weather Station
                        B) Test LCD Screen
                        C) Test DHT Sensor
                        D) Test Light Sensor
                        E) Exit
                        
                        Enter your choice: """)
    if choice == 'A' or choice == 'a':
        run_station()
        menu()
    elif choice == 'B' or choice == 'b':
        test_Screen()
        menu()
    elif choice == 'C' or choice == 'c':
        test_DHTSensor()
        menu()
    elif choice == 'D' or choice == 'd':
        test_lightSensor()
        menu()
    elif choice == 'e' or choice == 'e':
        setRGB(0,0,0)
        setText("Sleep Mode")
        sys.exit    
    else:
        print("Invalid Input")
        menu()

#runs weather station: imported from weatherStation.py        
def run_station():
    wStation.w_station()

#runs LCD screen test: imported from testLCD.py    
def test_Screen():
    testLCD.test_screen()

#runs DHT sensor test: imported from testDHT.py    
def test_DHTSensor():
    testDHT.test_dht()

#runs light sensor test: imported from testLIGHT.py
def test_lightSensor():
    testLIGHT.test_light()

#runs main function
main()