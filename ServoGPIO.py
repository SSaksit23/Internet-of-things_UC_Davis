from gpiozero import AngularServo
from time import sleep
 
servoDT = AngularServo(12, min_pulse_width=0.0006, max_pulse_width=0.0023)
 
while (True):
    servoDT.angle = 90
    sleep(2)
    servoDT.angle = 0
    sleep(2)
    servoDT.angle = -90
    sleep(2)