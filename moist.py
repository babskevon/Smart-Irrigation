from gpiozero import MCP3208
from time import sleep

#function to map moisture to percentage
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
#mapping function
def _outPUT(x):
    outMax = 100
    outMin = 0
    inMin = 2.275
    inMax = 0.806
    out = x - inMin
    out = out * (outMax - outMin)
    out = out/((inMax - inMin) + outMin)
    if(out > 100):
        out = 100
    if(out < 0):
        out = 0
    return int(out)


def moist(channel):
    adc_value = MCP3208(channel=channel).value
    for x in range(4):
        adc_value += MCP3208(channel=channel).value
        
    adc_value = adc_value/5
    adc_value = adc_value * 3.3
    return _outPUT(adc_value) #_map((adc_value/5),0.686,0.300,0,100)

def moisture(channel1,channel2):
    moist1 = moist(channel1)
    moist2 = moist(channel2)
    return (moist1 + moist2)/2

def light_intensity(channel):
    adc_value = MCP3208(channel=channel).value
    for x in range(4):
        adc_value += MCP3208(channel=channel).value
    adc_value = adc_value/5
    
    return adc_value * 3.3
#     print(moist(1))
#     sleep(2)
#     kkk = outPUT(MCP3208(channel=1).value*3.3)#_map((MCP3208(channel=1).value*3.3),2.262,0.8,0,100) #moist(1) # #moist(1)
#     print("moisture is {} actual value = {}".format(kkk*3.3,MCP3208(channel=1).value*3.3))
#     sleep(1)