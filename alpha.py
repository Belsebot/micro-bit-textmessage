import radio
from microbit import *

alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','Y','V','W','X','Y','Z']
value=600
x=0
msg=""
radio.on()
while True:
    acce_x= accelerometer.get_x()
    if acce_x > value:
        x=x+1 
    if acce_x < -value:
        x=x-1

    if x>25:
        x=0
    if x<0:
        x=25

    if button_a.is_pressed():
        msg=msg+alpha[x]
        display.show(Image.SQUARE_SMALL,delay=200,wait=True,loop=False,clear=True)
    if button_b.is_pressed():
        print (msg)
        display.show(Image.HAPPY,delay=200,wait=True,loop=False,clear=True)
        radio.send(msg)
        msg=""
        
    display.show(alpha[x])
    sleep(500)
   