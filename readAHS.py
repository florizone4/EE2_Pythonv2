from gpiozero import MCP3008
from time import sleep

#FIXED
def read_AHSValue():
    adc = MCP3008(channel=1)
    humidity_voltage = adc.value * 3.3
    humidity_percentage = (humidity_voltage / 3.3) * 100
    return humidity_percentage




#SMS = MCP3008(channel=0, clock_pin=17, mosi_pin=18, miso_pin=27)

