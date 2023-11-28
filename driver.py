import cv2
from datetime import datetime
import threading
import os
from servo import ServoComplex
from story_teller import StoryTeller
import atexit
import time

FRAME_W = 320
FRAME_H = 200
HORIZONTAL_MAX = 70 # degree
VERTICAL_MAX = 30 # degree
TIME_THRESHOLD = 10
STEPS_TO_TURN = 10
SECOND_PER_DEGREE = 1 / 90 # it takes 1 second to turn 90 degrees
# I shouldn't constant how many seconds it should take for turning
# but rather we should have a ratio (how many angles per second) and 
# use the ratio to move the face.

# also this should happen only when there are multiple faces
# if there is only one face, you can do it normally
# I think it's a good practice to do that even if there is only one face


cascPath = 'haarcascade_frontalface_default.xml'

def initialize():
	global faceCascade, cap, servos, st, current_h, current_v

	faceCascade = cv2.CascadeClassifier(cascPath)

	cap = cv2.VideoCapture(0)
	if not cap.isOpened():
		print("error in opening Video Capture")
		exit()

	cap.set(cv2.CAP_PROP_FRAME_WIDTH,  320)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)

	servos = ServoComplex()

	st = StoryTeller()
	st.get_story()
	st.make_mp3()
	
	current_h = 0
	current_v = 0
	
	print("Finished initialization")
	
def destructor():
	global cap
	# When everything is done, release the capture information and stop everything
	cap.release()
	cv2.destroyAllWindows()
	print("SEE YOU")
    
def main():
	global faceCascade, cap, servos, st, lastFaceDetected, current_h, current_v
	# in case it's forced to be quit, destructor has to be run
	atexit.register(destructor)
	initialize()
	while True:
		ret, frame = cap.read()
		
		if ret == False:
			continue

		# Convert to greyscale for easier faster accurate face detection
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.equalizeHist(gray)
		
		# Do face detection to search for faces from these captures frames
		faces = faceCascade.detectMultiScale(frame, 1.1, 3, 0, (10, 10))

		# story telling takes up power
		'''
		if len(faces) != 0 and not st.is_story_running():
			thread = threading.Thread(target=st.start_story)
			thread.start()

		if len(faces) == 0 and st.is_story_running():
			timeDiff = datetime.now() - lastFaceDetected
			if timeDiff.seconds > TIME_THRESHOLD:
				st.stop_story()
		'''

		for (x, y, w, h) in faces:
			lastFaceDetected = datetime.now()
			# Draw a green rectangle around the face (There is a lot of control to be had here, for example If you want a bigger border change 4 to 8)
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
			# Get the centre of the face
			center_x = x + (w/2)
			center_y = y + (h/2)

			# Get the percentage offset, relative to the center of image
			turn_x  = float(center_x - (FRAME_W/2)) / float(FRAME_W/2)
			turn_y  = float(center_y - (FRAME_H/2)) / float(FRAME_H/2)
			
			# Get the angles
			turn_horizontal = turn_x * HORIZONTAL_MAX
			turn_vertical = turn_y * VERTICAL_MAX
			
			diff_h = turn_horizontal - current_h
			diff_v = turn_vertical - current_v
			time_to_turn = abs(diff_h) * SECOND_PER_DEGREE
			
			for i in range(0, STEPS_TO_TURN):
				servos.move_servos(diff_h * i / STEPS_TO_TURN, diff_v * i / STEPS_TO_TURN)
				sleep_time = time_to_turn / STEPS_TO_TURN
				print(f'sleep time: {sleep_time}')
				time.sleep(sleep_time)
				
			current_h = turn_horizontal
			current_v = turn_vertical
			
			# servos.move_servos(turn_horizontal, turn_vertical)
			# stay at the position for 2 seconds
			time.sleep(1)
			
		cv2.imshow("Video", frame)
		
		if 0xFF == ord('q'):
			break
			
	destructor()


if __name__ == '__main__':
	main()
