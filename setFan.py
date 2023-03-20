import gpiozero as GPIO
from time import sleep

# GPIO pins:
# GPIO 5 : Pump
# GPIO 6 : Fan
# GPIO12 : LED

motor = GPIO.Motor(6, 4)

def setpumpert(speed):
    motor.forward(speed)

n = 0
while True:

    setpumpert(1)