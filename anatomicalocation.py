

def anatomical_coordinates(mp_drawing, hand_landmarks, image, jointName):
    desiredSpot = hand_landmarks.landmark[jointName]
    coordinates = mp_drawing._normalized_to_pixel_coordinates(desiredSpot.x, desiredSpot.y, image.shape[0], image.shape[1])
    print(jointName)
    # print(desiredSpot) ##decimal spot
    global x_digit
    x_digit = coordinates[0]
    global y_digit
    y_digit = coordinates[1]
    # print(x_digit, y_digit) ##the actual pixel location
