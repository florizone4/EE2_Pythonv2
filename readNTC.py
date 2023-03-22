from gpiozero import MCP3008
from time import sleep
import math

# In table "measurements", this is "temperature"

def read_NTC():
    adc = MCP3008(channel=2)
    #print(adc.value*3.3)
    resistance = ((2200 / (adc.value))) - 2200 #((3.3 / (adc.value*3.3)) * 2200) - 2200
    #print(resistance)
    A= 3.354016*10**(-3)
    B= 2.569850*10**(-4)
    C= 2.620131*10**(-6)
    D= 6.383091*10**(-8)

    logValue = math.log(resistance/2200)


    #Stijnhartje = 1 / (A * math.log(resistance) + B * (math.log(resistance) * math.log(resistance)) + C (math.log(resistance) * math.log(resistance) * math.log(resistance)))  #rewrite this to a better code to convert voltage to TEMP
    Stijnhartje = (1 / (A+B*logValue+C*(logValue**2)+D*(logValue**3)))-273.15
    #print(Stijnhartje)
    return Stijnhartje


#read_NTC()



#NTC = MCP3008(channel=2, clock_pin=17, mosi_pin=18, miso_pin=27)