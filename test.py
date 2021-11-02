import cv2
import time
import mediapipe as mp
import pyautogui
from anatomicalocation import anatomical_coordinates
from usersetting import customVideoCapture, anatomyfinder, drawAll
from videosetting import vidset
from anatomicalocation import digit1x, digit1y
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
#used for drawing landmarks on hand
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

x_digit = 0
y_digit = 0
list = []
video = cv2.VideoCapture(1)
if customVideoCapture == True:
  vidset(video, cv2)

results = 0


def convertTopixel(digitx, digity):
    fingerx = 1080 * digitx * image.shape[0]
    fingery = 1920 * digity * image.shape[1]
    return fingerx, fingery

while video.isOpened():
  success, image = video.read()
    #reference to video input
  image.flags.writeable = False
  imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  #converts BGR as openCV reads BGR to RGB
  results = hands.process(image)
  image.flags.writeable = True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  # print(dir(mp_hands.HandLandmark.WRIST))
  # print(mp_hands.HandLandmark.WRIST.real)
  # print([(index, item) for index, item in enumerate(results.multi_hand_landmarks[0])])
  if results.multi_hand_landmarks:
    list2 =str(results.multi_hand_landmarks[0])
    list3=list2.split(" ")
    # print([item for item in enumerate(list3)])
    finger1x =float(list3[34]) #digit1 tip
    finger1y =float(list3[37]) #digit1 tip
    finger2x =float(list3[74]) #digit2 tip
    finger2y =float(list3[77]) #digit2 tip
    finger3x =float(list3[114]) #digit2 tip
    finger3y =float(list3[117]) #digit2 tip
    fingerlist = [finger1x,finger1y,finger2x, finger2y, finger3x, finger3y]
    movedigit1 = convertTopixel(finger1x,finger1y)
    print(finger1x)
    print(finger1y)
    # pyautogui.FAILSAFE = False
    # pyautogui.moveTo(movedigit1[0], movedigit1[1])

    # convertTopixel(fingerlist[finger],fingerlist[finger+1])
    # convertTopixel(fingerlist[finger],fingerlist[finger+1])
  # x_digit = coordinates[0]
  # newvalue_x = 1080 * x_digit/480
  # y_digit = coordinates[1]
  # newvalue_y = 1920 * y_digit/640
  # print(newvalue_x, newvalue_y)
  # if results.multi_hand_landmarks:
  #   for hand_landmarks in results.multi_hand_landmarks:
      # print(hand_landmarks)
  #     if anatomyfinder == True:
  #       list.append(mp_hands.HandLandmark)
  #       for jointName in mp_hands.HandLandmark: ##this line was placed here instead of part of function because of performance issues.
  #         if jointName == mp_hands.HandLandmark.WRIST:
  #           coordinates= mp_drawing._normalized_to_pixel_coordinates(hand_landmarks.landmark[0].x, hand_landmarks.landmark[0].y, image.shape[0], image.shape[1])
  #           x_digit = coordinates[0]
  #           newvalue_x = 1080 * x_digit/480
  #           y_digit = coordinates[1]
  #           newvalue_y = 1920 * y_digit/640
  #           print(newvalue_x, newvalue_y)
  #         # print(list)
  #         # print(jointName)
  #       pyautogui.FAILSAFE = False
  #       pyautogui.moveTo(newvalue_x, newvalue_y)
          # anatomical_coordinates(mp_drawing, hand_landmarks, image, 8) #tracking tip of digit 2
          # anatomical_coordinates(mp_drawing, hand_landmarks, image, 4) #tracking tip of digit 1
          # anatomical_coordinates(mp_drawing, hand_landmarks, image, 12) #tracking tip of digit 3
          # print(digit1x, digit1y)
    
    # print("outside", list[0])
      # if drawAll == True:  ##this will draw all the landmarks
      #   mp_drawing.draw_landmarks(
      #     image,
      #     hand_landmarks,
      #     mp_hands.HAND_CONNECTIONS, ##line here draws connections between joints.
      #     mp_drawing_styles.get_default_hand_landmarks_style(),
      #     mp_drawing_styles.get_default_hand_connections_style())
      #     # will draw lines and show landmarks.
      # """ reference https://github.com/google/mediapipe/blob/master/mediapipe/modules/hand_landmark/hand_landmark_tracking_cpu.pbtxt"""
  cv2.imshow("Hand Tracker", cv2.flip(image, 1))
    #this will flip horizontally the entire camera input
  if cv2.waitKey(5) & 0xFF == 27:
    break
video.release()
