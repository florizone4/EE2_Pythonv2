from gpiozero import MCP3008
from time import sleep
from gpiozero import LightSensor

# In table "measurements", this is "light"

def get_lightValue():
    adc = MCP3008(channel=3)
    lightIntensity = adc.value * 100
    return lightIntensity

# def converter(gen):
#     for value in gen:
#         yield ((1-value) * 100)


#SMS = MCP3008(channel=0, clock_pin=17, mosi_pin=18, miso_pin=27)


#LDR = MCP3008(channel=3, clock_pin=17, mosi_pin=18, miso_pin=27)
