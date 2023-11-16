#import RPi.GPIO as GPIO
import time
from gpiozero import AngularServo, Device
from gpiozero.pins.native import NativeFactory

myFact= NativeFactory()

PIN_1 = 17
PIN_2 = 13
PULS_FREQ = 50

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(PIN_1, GPIO.OUT)

# servo_1 = GPIO.PWM(PIN_1, PULS_FREQ)

servo_1 = AngularServo(17,min_angle=0,max_angle=90)
servo_2 = AngularServo(27,min_angle=0,max_angle=90)

print("start")
servo_1.angle = 0
servo_2.angle = 90
time.sleep(2)
print("move1")
servo_1.angle = 30
servo_2.angle = 60
time.sleep(2)
print("move2")
servo_1.angle = 60
servo_2.angle = 30
time.sleep(2)
print("move3")
servo_1.angle = 30
servo_2.angle = 60
time.sleep(2)
print("end")

#servo_1.start(5)
#time.sleep(2)
#servo_1.ChangeDutyCycle(10)
#time.sleep(2)
#servo_1.ChangeDutyCycle(15)

#servo_1.stop()
#GPIO.cleanup()
