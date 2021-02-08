from grove_rgb_lcd import *
import random

def test_screen():
    setText("Weather Station\nLCD test")
    setRGB(255,255,255)
    time.sleep(1.5)
    
    print("Testing LCD functionality, please wait.")

    # Slowly change the colors every 0.01 seconds.
    for i in range(0,255):
        setRGB(255-i,i,0)
        time.sleep(0.01)
    
    for j in range(0,255):
        setRGB(0,255-j,j)
        time.sleep(0.01)
    
    for k in range(0,255):
        setRGB(k,0,255-k)
        time.sleep(0.01)
        
        
    setText("Random colors")
    for i in range(0,51):
        setRGB(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        time.sleep(.1)
    time.sleep(1)

    # ascii char 255 is the cursor character
    setRGB(255,255,255)
    setText(chr(255)*32)
    time.sleep(2)

    # typewriter
    setRGB(255,127,0)
    str = "Hello World"
    for i in range(0,12):
        setText(str[:i])
        time.sleep(.2)
    time.sleep(2)

    setRGB(255,0,255)
    setText("1234567890ABCDEF1234567890ABCDEF")
    time.sleep(2)

    setText("Long strings will be truncated at 32 chars")
    time.sleep(2)

    setRGB(0,255,0)
    setText("Automatic word wrapping")
    time.sleep(2)

    setText("Manual\nword wrapping")
    time.sleep(2)

    setRGB(0,255,255)
    setText("ASCII printable and extended")
    time.sleep(2)

    chars = ""
    for a in range(32,256):
        chars += chr(a)
        if len(chars) == 32:
            setText(chars)
            chars = ""
            time.sleep(2)

    setRGB(0,255,0)
    setText("Solid colors")
    time.sleep(2)

    setText("Red")
    setRGB(255,0,0)
    time.sleep(.5)

    setText("Green")
    setRGB(0,255,0)
    time.sleep(.5)

    setText("Blue")
    setRGB(0,0,255)
    time.sleep(.5)

    setText("Yellow")
    setRGB(255,255,0)
    time.sleep(.5)

    setText("Magenta")
    setRGB(255,0,255)
    time.sleep(.5)

    setText("Cyan")
    setRGB(0,255,255)
    time.sleep(.5)

    setText("White")
    setRGB(255,255,255)
    time.sleep(.5)

    setText("Black")
    setRGB(0,0,0)
    time.sleep(.5)

    setText("Grey")
    setRGB(127,127,127)
    time.sleep(.5)

    setRGB(255,255,255)
    setText("Alphanumeric characters")
    time.sleep(2)

    setText("1234567890ABCDEF1234567890ABCDEF")
    time.sleep(2)

    setText("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    time.sleep(2)

    setText("abcdefghijklmnopqrstuvwxyz")
    time.sleep(2)

    setText("1234567890")
    time.sleep(2)

    setText("Shades of red")
    for c in range(0,255):
        setRGB(255,255-c,255-c)
        time.sleep(.01)

    setText("Shades of green")
    for c in range(0,255):
        setRGB(255-c,255,255-c)
        time.sleep(.01)

    setText("Shades of blue")
    for c in range(0,255):
        setRGB(255-c,255-c,255)
        time.sleep(.01)

    setText("Shades of yellow")
    for c in range(0,255):
        setRGB(255,255,255-c)
        time.sleep(.01)

    setText("Shades of magenta")
    for c in range(0,255):
        setRGB(255,255-c,255)
        time.sleep(.01)

    setText("Shades of cyan")
    for c in range(0,255):
        setRGB(255-c,255,255)
        time.sleep(.01)

    setText("Shades of grey")
    for c in range(0,255):
        setRGB(c,c,c)
        time.sleep(.01)


    setRGB(255,255,255)
    setText("Welcome to the\nWeather Center")
