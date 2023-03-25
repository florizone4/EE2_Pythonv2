import gpiozero as GPIO
from time import sleep

# GPIO pins:
# GPIO 5 : Pump
# GPIO 6 : Fan
# GPIO12 : LED

fan = GPIO.PWMLED(6)

def setpumpert(speed):
    fan.value = speed
