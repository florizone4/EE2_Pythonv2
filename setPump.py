import gpiozero as GPIO
from time import sleep
import gpiozero.pins.rpigpio

#def close(self): pass
#gpiozero.pins.rpigpio.RPiGPIOPin.close = close

#gpiozero.LED(..., pin_factory=gpiozero.pins.rpigpio.RPiGPIOFactory())

motor = GPIO.Motor(5, 4)
#motor = GPIO.PWMOutputDevice(5)
# motor = GPIO(5,7)
print("Motor running")
def setpumpert(speed):
    n = 0.15
    #sleep(1)
    #motor.forward(speed)
    while(n < speed):
         motor.forward(n)
         n = n + 0.01
         print(n)
         sleep(0.025)
    #while True:
    motor.forward(n - 0.1)

#	 motor.forward(n - 0.01)

#setpumpert(0.9)
#while True:
    #motor.forward(pwmValue)
