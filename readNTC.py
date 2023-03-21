from gpiozero import MCP3008
from time import sleep
import math
impor




def read_NTC():
    adc = MCP3008(channel=2)
    resistance = ((3,3 / adc ) * 2200) - 2200

    A= -14,6337
    B= 4791,842
    C= -115334
    D= -3,730535 * 1000000
    Stijnhartje = 1 / (A * math.log(resistance) + B * (math.log(resistance) * math.log(resistance)) + C (math.log(resistance) * math.log(resistance) * math.log(resistance)))  #rewrite this to a better code to convert voltage to TEMP
    return Stijnhartje






#NTC = MCP3008(channel=2, clock_pin=17, mosi_pin=18, miso_pin=27)