import radio
from microbit import *

radio.on()
display.show("R")

while True:                 #main loop
    display.show("R")
    msg=radio.receive()     #receive message
    
    if (msg!=None):         #if message is something else than none show current message
        display.show(msg,delay=400,wait=True,loop=False,clear=True)
        print (msg)         #debug
    
    
