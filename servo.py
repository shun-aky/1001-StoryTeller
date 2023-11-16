#import RPi.GPIO as GPIO
import time
from gpiozero import AngularServo, Device

PIN_1 = 17
PIN_2 = 27
HORIZONTAL_MIN = 0
HORIZONTAL_MAX = 90
VERTICAL_MIN = 0
VERTICAL_MAX = 90

class ServoComplex:
	
	def __init__(self):
		self.servo_h = AngularServo(PIN_1, min_angle=HORIZONTAL_MIN, max_angle=HORIZONTAL_MAX)
		self.servo_v = AngularServo(PIN_2, min_angle=VERTICAL_MIN, max_angle=VERTICAL_MAX)
		
	def move_horizontal(self, angle_h):
		self.servo_h.angle = angle_h
		
	def move_vertical(self, angle_v):
		self.servo_v.angle = angle_v
		
	def move_servos(self, angle_h, angle_v):
		self.move_horizontal(move_h)
		self.move_vertical(move_h)


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
