import cv2
import mediapipe as mp
import pyautogui
from anatomicalocation import anatomical_coordinates
from usersetting import showCamerafeed, customVideoCapture, anatomyfinder, drawAll, buttonFunction, buttonLetter
from videosetting import vidset
import keyboard

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
#used for drawing landmarks on hand
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
    #user settings for modifying based on compute power, etc

screenWidth = pyautogui.size()[0]
screenHeight = pyautogui.size()[1]
##uses pyauto to pull information on screen resolution

video = cv2.VideoCapture(1)
if customVideoCapture == True:
  vidset(video, cv2)

# y resolution of camera width etc image.shape[1]
counter = 0
results = 0

def convertTopixel(digitx, digity):
    fingerx = round(screenWidth - (screenWidth * digitx))
    fingery = round(screenHeight * digity)
    return fingerx, fingery

while video.isOpened():
  success, image = video.read()
  #reference to video input
  image.flags.writeable = False
  imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  #converts BGR as openCV reads BGR to RGB
  results = hands.process(image)
  image.flags.writeable = True
  # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  if results.multi_hand_landmarks: ##this will enumerate to list and then create a string to pull data from list.
    list2 =str(results.multi_hand_landmarks[0])
    if results.multi_hand_landmarks[0] != 0:
      pass ##ensures that program does not crash if no hand detected
    list3=list2.split(" ")
    # print([item for item in enumerate(list3)])
    # finger1x =float(list3[34]) #digit1 tip
    # finger1y =float(list3[37]) #digit1 tip
    finger2x =float(list3[84]) #digit2 tip
    finger2y =float(list3[87]) #digit2 tip
    # finger3x =float(list3[114]) #digit2 tip
    # finger3y =float(list3[117]) #digit2 tip
    # fingerlist = [finger1x,finger1y,finger2x, finger2y, finger3x, finger3y]
    movedigit2 = convertTopixel(finger2x,finger2y)
    print(movedigit2[0], movedigit2[1])
    pyautogui.FAILSAFE = False
    if counter == 0:
      counter += 1
      pyautogui.moveTo(screenWidth/2, screenHeight/2)
      ##one time counter to grab resolution size and cursor default to middle
    pyautogui.moveTo(movedigit2[0], movedigit2[1])
    if keyboard.is_pressed(buttonLetter) and buttonFunction == True:
      pyautogui.click()
    # print("outside", list[0])
    if showCamerafeed == True and drawAll == True:  ##this will draw all the landmarks if camera is on and landmark draw. Setting here to allow for CPU resource saving
      mp_drawing.draw_landmarks(
        image,
        results.multi_hand_landmarks[0],
        mp_hands.HAND_CONNECTIONS, ##line here draws connections between joints.
        mp_drawing_styles.get_default_hand_landmarks_style(),
        mp_drawing_styles.get_default_hand_connections_style())
          # will draw lines and show landmarks.
      # """ reference https://github.com/google/mediapipe/blob/master/mediapipe/modules/hand_landmark/hand_landmark_tracking_cpu.pbtxt"""
  if showCamerafeed == True:
    cv2.imshow("Hand Tracker", cv2.flip(image, 1))
    #this will flip horizontally the entire camera input
    if cv2.waitKey(5) & 0xFF == 27:
      break
video.release()
