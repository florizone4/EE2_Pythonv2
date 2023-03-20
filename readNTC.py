from gpiozero import MCP3008
from time import sleep


def read_NTC():
    adc = MCP3008(channel=2)
    NTC_percentage = (NTC_voltage / 3.3) * 100 #rewrite this to a better code to convert voltage to TEMP
    return NTC_percentage






#NTC = MCP3008(channel=2, clock_pin=17, mosi_pin=18, miso_pin=27)