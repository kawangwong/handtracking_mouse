def anatomical_coordinates(mp_drawing, hand_landmarks, image, jointName):
    desiredSpot = hand_landmarks.landmark[jointName]
    coordinates = mp_drawing._normalized_to_pixel_coordinates(desiredSpot.x, desiredSpot.y, image.shape[0], image.shape[1])
    # print(jointName)
    # print(desiredSpot) ##decimal spot
    print(coordinates) ##the actual pixel location