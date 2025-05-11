sudo apt-get update
sudo apt-get install python3-picamera

import picamera
import time 
-------------
# Capturing image and send it on a connection 
mysocket = socket.socket()
mysocket = connect(('aserver', 8000))
conn = mysocket.makefile('wb')
camera.capture(conn, 'jpeg')

'''timelapse photography'''

# Take photo overtime, take one argument, a file name
# {counter} and {timestamp} can be substituted in the args 
camera.capture_continuous()
camera = picamera.PiCamera()
    for filename in
    camera.capture_continuous('img{counter}.jpg'):
        time.sleep(300)

