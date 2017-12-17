import radio
from microbit import *

radio.on()
display.show("R")

while True:
    display.show("R")
    msg=radio.receive()
    
    if (msg!=None):
        display.show(msg,delay=400,wait=True,loop=False,clear=True)
        print (msg)
    
    