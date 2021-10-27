import cv2
import mediapipe as mp
import time
from anatomicalocation import anatomical_coordinates
from usersetting import customVideoCapture, anatomyfinder, drawAll
from videosetting import vidset
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
#used for drawing landmarks on hand
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

video = cv2.VideoCapture(1)
if customVideoCapture == True:
  vidset(video, cv2)


while video.isOpened():
  success, image = video.read()
    #reference to video input
  image.flags.writeable = False
  results = hands.process(image)
  image.flags.writeable = True
  imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  #converts BGR as openCV reads BGR to RGB
  if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
      if anatomyfinder == True:
        for jointName in mp_hands.HandLandmark: ##this line was placed here instead of part of function because of performance issues.
          anatomical_coordinates(mp_drawing, hand_landmarks, image, jointName) 
      if drawAll == True:
        mp_drawing.draw_landmarks(
          image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS, ##line here draws connections between joints.
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
          #will draw lines and show landmarks.
      """ reference https://github.com/google/mediapipe/blob/master/mediapipe/modules/hand_landmark/hand_landmark_tracking_cpu.pbtxt"""
  cv2.imshow("Hand Tracker", cv2.flip(image, 1))
    #this will flip horizontally the entire camera input
  if cv2.waitKey(5) & 0xFF == 27:
    break

video.release()
