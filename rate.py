import RPi.GPIO as GPIO
from time import sleep, time
import sys
from lcd import irrig
FLOW_SENSOR_GPIO13 = 13
FLOW_SENSOR_GPIO12 = 12
servoPIN = 25
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR_GPIO13, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(FLOW_SENSOR_GPIO12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
#GPIO.output(RELAY, GPIO.LOW)
#GPIO.cleanup()
global start
start = 0
global count
count = 0

global count1
count1 = 0
global times1
global times2

def countPulse(channel):
    global start
    global count
    global times1
    times1 = time()
    if(start == 0):
        start = time()
    if((time() - start) > 300):
        GPIO.output(servoPIN, GPIO.LOW)
        start = 0
        sleep(2)
    if start_counter == 1:
        count = count+1



def countPulse1(channel):
    global count1
    global times2
    times2 = time()
    if start_counter1 == 1:
        count1 = count1+1
        
GPIO.add_event_detect(FLOW_SENSOR_GPIO13, GPIO.FALLING, callback=countPulse)
GPIO.add_event_detect(FLOW_SENSOR_GPIO12, GPIO.FALLING, callback=countPulse1)

def sensorone():
    global count
    global times1
    times = time() - times1
    start_counter = 1
    time.sleep(1)
    start_counter = 0
    flow = (count / 7.5)
    count = 0
    
    return flow * (times/60)
#sensorone()
def sensortwo():
    global count1
    global times2
    times = time() - times2
    start_counter1 = 1
    time.sleep(1)
    start_counter1 = 0
    flow = (count1 / 7.5)
    count1 = 0
    return flow * (times/60)
    
#ensortwo()
#function to irrigate
#irrig()
def valve(moist,cmd,light):
    p.ChangeDutyCycle(2.5)
    if(moist < 30.0 and light < 1.5):
        irrig()
        p.ChangeDutyCycle(7.5)
    elif(cmd == True):
        irrig()
        p.ChangeDutyCycle(7.5)
    else:
        p.ChangeDutyCycle(2.5)