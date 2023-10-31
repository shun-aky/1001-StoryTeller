import cv2

cap = cv2.VideoCapture()

while True:
	ret,frame = cap.read()
	# frame = cv2.flip(frame, -1)
	
	if ret == False:
		print("Error in Getting Image")
		continue
		
	cv2.imshow("Video", frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything is done, release the capture information and stop everything
video_capture.release()
cv2.destroyAllWindows()
