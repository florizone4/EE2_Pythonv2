from gpiozero import MCP3008
from time import sleep

# In table "measurements", this is "moisture"

def read_SMSValue():
    adc = MCP3008(channel=0)
    SMS_voltage = adc.value * 3.3
    SMS_percentage = (SMS_voltage / 3.3) * 100
    return SMS_percentage

#def converter(gen):
#    for value in gen:
#        yield ((1-value) * 100)


#SMS = MCP3008(channel=0, clock_pin=17, mosi_pin=18, miso_pin=27)

#for data in converter(adc.values):
#    print('Soil moisture: ', data, '%')
#    sleep(1)