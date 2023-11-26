import cv2
from datetime import datetime
import threading
import os
from servo import ServoComplex
from story_teller import StoryTeller

FRAME_W = 320
FRAME_H = 200
HORIZONTAL_MAX = 70 # degree
VERTICAL_MAX = 30 # degree

cascPath = 'haarcascade_frontalface_default.xml'

def initialize():
	global faceCascade, cap, servos, st

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
    
	if len(faces) != 0:
		thread = threading.Thread(target=st.start_story, args=(1,))
	for (x, y, w, h) in faces:
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
		
		servos.move_servos(turn_horizontal, turn_vertical)
		
	cv2.imshow("Video", frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything is done, release the capture information and stop everything
cap.release()
cv2.destroyAllWindows()
print("SEE YOU")
