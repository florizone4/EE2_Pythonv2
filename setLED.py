import gpiozero as GPIO
from time import sleep

# GPIO pins:
# GPIO 5 : Pump
# GPIO 6 : Fan
# GPIO12 : LED

led = GPIO.PWMLED(12)

def setpumpert(speed):
    led.value(speed)


n = 0
while True:

    setpumpert(1)