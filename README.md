# handtracking_mouse
Project for building a HID (Human Interface Device) mouse using camera tracking of digits through machine learning model MediaPipe from Google's Tensor Flow


<h1>Purpose</h1>

The purpose of this project was to write software that can be used on a computer to control a mouse cursor through the use of hand gestures.

<h2>How it works</h2>

The software itself is written in a language called Python. The underlying core of this application uses a Python Library called [MediaPipe](https://google.github.io/mediapipe/solutions/hands). MediaPipe an organization from Google.
Google's MediaPipe framework was useed to create pre-trained machine learning models, which can be deployed in multiple applications and through different languages.
The best of all is these programs can be run locally, with the constraints only being the end user's imagination and approach.


For the end user, a camera will be used to capture data from the user. This data that the program will collect are anatomical landmarks on the hand.

![Landmarks](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png)

Once the software captures the landmarks, it input the data into another library call [pyautogui](https://pyautogui.readthedocs.io/en/latest/), which will tell the computer where to move the cursor
relative to the location it is currently in.

<h2>Use case scenario</h2>

For end users, this can be a tool to just browse the computer with the hand as if it was an air gestured movement.

For the therapy space, this can be used as a therapy tool to create treatment sessions that are task-oriented with levels of grading through resistance.
In the realm of therapy, it can certainly be used as a replacement input for human interface with the computer, especially for patients that may no longer be able to use their
hands or digits for trackpads or mouse movements.

<h2>Instructions</h2>
Coming soon, software is a work in progress.

<h1>Disclaimer</h1>
This is just a software used as a showcase and possible use in practical applications. I have not tested this as a use in a commercial setting and i take no responsibiliity for
how the end user will use this. There is no support and will be used as is.
