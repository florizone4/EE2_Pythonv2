import gpiozero as GPIO
from time import sleep

# GPIO pins:
# GPIO 5 : Pump
# GPIO 6 : Fan
# GPIO12 : LED

fan = GPIO.Motor(6,4)
def setpumpert(speed):
    new = speed - 0.1
    if(new > 1):
        print("Fan value is now one")
        fan.value = 1
    elif(new < 0):
        print("Fan value is now zero")
        fan.value = 0.0
        #fan.stop()
    else:
        print(speed)
        fan.value = speed

# motor = GPIO.Motor(6, 4)
#
# def setpumpert(speed):
#     motor.forward(speed)
#
# n = 0
# while True:
#
#     setpumpert(1)