from gpiozero import MCP3008
from time import sleep

def converter(gen):
    for value in gen:
        yield (1 * 100)

adc = MCP3008(channel=2)
value = adc.values
print(value)


for data in converter(adc.values):
    print('NTC: ', data, 'ºC')
    sleep(1)

#NTC = MCP3008(channel=2, clock_pin=17, mosi_pin=18, miso_pin=27)