# import the opencv library
from cv2 import cv2
import time
import mediapipe as mp 


# define a video capture object
cap = cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

pTime=0
cTime=0

while(True):
	
	# Capture the video frame by frame
	ret, img = cap.read()
	imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	results=hands.process(imgRGB)
	#print(results.multi_hand_landmarks)

	if results.multi_hand_landmarks:
		for handLms in results.multi_hand_landmarks:
			for id, lm in enumerate(handLms.landmark):
				#print(id,lm)
				h, w, c=img.shape
				cx, cy = int(lm.x*w), int(lm.y*h)
				print(id,cx,cy)
				#if id==4:
				cv2.circle(img, (cx,cy),25,(255,0,255),cv2.FILLED)



			mpDraw.draw_landmarks(img,handLms, mpHands.HAND_CONNECTIONS)

	cTime=time.time()
	fps=1/(cTime-pTime)
	pTime=cTime

	cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,
	(255,0,255),3)

	# Display the resulting img
	cv2.imshow('Image', img)
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
#cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

    

