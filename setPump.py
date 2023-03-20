import gpiozero as GPIO
from time import sleep

pwmValue = 0.9

motor = GPIO.Motor(5, 4)

def setpumpert(speed):
    n = 0.15
    #sleep(1)
    #motor.forward(speed)
    while(n < speed):
         motor.forward(n)
         n = n + 0.01
         print(n)
         sleep(0.025)
    while True:
    	 motor.forward(n - 0.01)

setpumpert(pwmValue)
#while True:
    #motor.forward(pwmValue)
