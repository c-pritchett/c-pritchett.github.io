import sys
import csv
from grove_rgb_lcd import *
import wStation
import testLCD
import testDHT
import testLIGHT

setRGB(255,255,255)
setText("Initializing...")

def main():
    menu()
        
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
        
def run_station():
    wStation.w_station()
    
def test_Screen():
    testLCD.test_screen()
    
def test_DHTSensor():
    testDHT.test_dht()

def test_lightSensor():
    testLIGHT.test_light()

main()