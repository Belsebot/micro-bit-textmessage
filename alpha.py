import radio
from microbit import *

alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','Y','V','W','X','Y','Z']
value=600           #accelerometer sensitivity
x=0                 #start value
msg=""              #start value
radio.on()
while True:         #main loop
    acce_x= accelerometer.get_x()       #get accelerometer x value
    if acce_x > value:          
        x=x+1                           #adding variable value by 1 if board is turned with its x axis
    if acce_x < -value:
        x=x-1                           #removing variable value by 1 if board is turned opposite direction

    if x>25:                            #if value is going over the array then start it from begining
        x=0
    if x<0:
        x=25

    if button_a.is_pressed():           #if a button is pressed save selected letter to msg variable and show square
        msg=msg+alpha[x]
        display.show(Image.SQUARE_SMALL,delay=200,wait=True,loop=False,clear=True)
    if button_b.is_pressed():           #if b button is pressed send current msg to the radio channel and reset msg variable
        print (msg)                     #debug
        display.show(Image.HAPPY,delay=200,wait=True,loop=False,clear=True)
        radio.send(msg)
        msg=""
        
    display.show(alpha[x])              #show letter which has been selected
    sleep(500)
   
