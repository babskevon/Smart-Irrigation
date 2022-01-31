from gpiozero import MCP3208, DistanceSensor
import time

waterlevel = DistanceSensor(echo=17, trigger=18)

#function to map moisture to percentage
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def moisture(channel):
    adc_value = MCP3208(channel=channel).value
    for x in range(4):
        adc_value += MCP3208(channel=channel).value
    return _map((adc_value/5),0.686,0.300,0,100)

def light(channel):
    adc_value = MCP3208(channel=channel).value
    return adc_value * 3.3

while True:
    lights = light(3)
    moist_1 = moisture(1)
    moist_2 = moisture(2)
    moisture_avg = (moist_1 + moist_2)/2
    print(lights)
    print('Distance: ', waterlevel.distance)
    time.sleep(0.1)
    
