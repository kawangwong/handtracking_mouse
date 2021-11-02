import pyautogui
import time

def anatomical_coordinates(mp_drawing, hand_landmarks, image, jointName):
    desiredSpot = hand_landmarks.landmark[jointName]
    coordinates = mp_drawing._normalized_to_pixel_coordinates(desiredSpot.x, desiredSpot.y, image.shape[0], image.shape[1])
    # print(jointName)
    # print(desiredSpot) ##decimal spot
    x_digit = coordinates[0]
    newvalue_x = 1080 * x_digit/480
    y_digit = coordinates[1]
    newvalue_y = 1920 * y_digit/640
    # pyautogui.FAILSAFE = False
    pyautogui.moveTo(x_digit, y_digit)
    # time.sleep(1)
    # pyautogui.moveTo(500, 500)
    print(newvalue_x, newvalue_y) ##the actual pixel location
