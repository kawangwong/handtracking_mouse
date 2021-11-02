digit1x =0
digit1y = 0


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
    # pyautogui.moveTo(x_digit, y_digit)
    # time.sleep(.05)
    # pyautogui.moveTo(500, 500)
    ##note to self. the problem is the fact that this is still iterating through enumerable, so 20 values are shown and iterated through before the value changes, so we have to find a way to only
    ##go trhough the value for 8 12 and 4
    
    global digit1x
    digit1x = newvalue_x
    
    global digit1y
    digit1y = newvalue_y
    # print(newvalue_x, newvalue_y) ##the actual pixel location
