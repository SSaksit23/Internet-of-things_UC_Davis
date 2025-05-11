sudo apt-get update
sudo apt-get install python3-picamera

import picamera
import time 

# instantiate the object of the PiCamera class
camera = picamera.PiCamera()

'''Camera Function'''

# Take a picture
camera.capture("pict.jpg")

''' Changing camera setting '''
camera.hflip = True
camera.vflip = True
camera.brightness = 50
camera.sharpness = 0

# View Video on RPi Screen
camera.start_preview("vid.h264")
time.sleep(10)
camera.stop_preview()

''' Sending images through network '''

