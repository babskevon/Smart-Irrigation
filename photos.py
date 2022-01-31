from picamera import PiCamera
from time import sleep, time

def photo():
    camera = PiCamera()
    camera.start_preview()
    name = str(int(time())) + ".jpg"
    camera.capture(name)
    sleep(2)
    camera.stop_preview()
    return name

#print(photo())

# from gpiozero import MCP3208
# import time
# moist = MCP3208(channel=1)
# while True:
#     print(moist)
#     time.sleep(1)
import requests
name = photo()
print(name)
url = 'https://robinah.pythonanywhere.com/photo/'

f = open(name,'rb')

tt = requests.post(url,files={'name':f})
print(tt.text)