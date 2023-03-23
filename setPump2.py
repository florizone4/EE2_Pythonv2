import RPi.GPIO as GPIO

#import the RPi.GPIO library

from time import sleep

#import the sleep from time library

ledpin = 5

#declare the GPIO 18 pin for the output of LED
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin,GPIO.OUT)
#define the behaviour of the ledpin as output

GPIO.setwarnings(False)
#ignore the warnings
pwm = GPIO.PWM(ledpin,500)

#create the pwm instance with frequency 1000 Hz

pwm.start(0)

#start the pwm at 0 duty cycle

while True:

#initialise the infinite while loop

    for duty in range(0,101):

        pwm.ChangeDutyCycle(duty)

    #changing the duty cycle according to the value of for loop

        sleep(0.01)

#generated the delay of 0.01 second in every iteration of for loop

sleep(0.5)

#generated the delay of 0.5 seconds

