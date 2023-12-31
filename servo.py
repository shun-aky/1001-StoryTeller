import os
import time
from gpiozero import AngularServo, Device
from gpiozero.pins.pigpio import PiGPIOFactory

PIN_1 = 17
PIN_2 = 27
HORIZONTAL_MIN = -70
HORIZONTAL_MAX = 70
VERTICAL_MIN = -30
VERTICAL_MAX = 30

class ServoComplex:
	
	def __init__(self):
		# running the command below and using PiGPIOFactory reduce the jitter
		os.system("sudo pigpiod")
		Device.pin_factory = PiGPIOFactory()
		self.servo_h = AngularServo(PIN_2, min_angle=HORIZONTAL_MIN, max_angle=HORIZONTAL_MAX)
		self.servo_v = AngularServo(PIN_1, min_angle=VERTICAL_MIN, max_angle=VERTICAL_MAX)
		
	def move_horizontal(self, angle_h):
		if angle_h is None:
			angle_h = 0
		angle_h = min(HORIZONTAL_MAX, max(HORIZONTAL_MIN, angle_h))
		self.servo_h.angle = angle_h
		
	def move_vertical(self, angle_v):
		if angle_v is None:
			angle_v = 0
		angle_v = min(VERTICAL_MAX, max(VERTICAL_MIN, angle_v))
		self.servo_v.angle = angle_v
		
	def move_servos(self, angle_h, angle_v):
		print(f'Horizontal: {angle_h}, vertical: {angle_v}')
		self.move_horizontal(angle_h)
		self.move_vertical(angle_v)
		
	def test(self):
		print("Start Testing")
		self.servo_h.angle = HORIZONTAL_MIN
		self.servo_v.angle = VERTICAL_MIN
		time.sleep(2)
		print("Move1")
		self.servo_h.angle = (HORIZONTAL_MIN + HORIZONTAL_MAX) / 2
		self.servo_v.angle = (VERTICAL_MIN + VERTICAL_MAX) / 2
		time.sleep(2)
		print("Move2")
		self.servo_h.angle = HORIZONTAL_MAX
		self.servo_v.angle = VERTICAL_MAX
		time.sleep(2)
		print("Move3")
		self.servo_h.angle = (HORIZONTAL_MIN + HORIZONTAL_MAX) / 2
		self.servo_v.angle = (VERTICAL_MIN + VERTICAL_MAX) / 2
		time.sleep(2)
		print("Finish Testing")
		
if __name__ == '__main__':
	servos = ServoComplex()
	servos.test()
