# handtracking_mouse
Project for building a HID (Human Interface Device) mouse using camera tracking of digits through machine learning model MediaPipe from Google.


<h1>Purpose</h1>

The purpose of this project was to write software that can be used on a computer to control a mouse cursor through the use of hand gestures. In doing so, I wanted learn how just how powerful these machine learning models are, how effective they can be used, and learn more about writing code in Python.

<h2>How it works</h2>

The software itself is written in a language called Python. The underlying core of this application uses a Python Library called [MediaPipe](https://google.github.io/mediapipe/solutions/hands). MediaPipe an organization from Google.
Google's MediaPipe framework was used to create pre-trained machine learning models, which can be deployed in multiple applications and through different languages.
In this case, Google trained a machine learning model that can be used to track 21 anatomiical landmarks.
The best of all is these programs can be run locally, with the constraints only being the end user's imagination and approach.


For the end user, a camera will be used to capture data from the user. This data that the program will collect are anatomical landmarks on the hand. The library called [cv2](https://opencv.org/) is what the python script utilizes for camera access.

![Landmarks](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png)

Once the software captures the landmarks, it input the data into another library call [pyautogui](https://pyautogui.readthedocs.io/en/latest/), which will tell the computer where to move the cursor relative to the location it is currently in.

Last, a function for clicking was written in using a library called [keyboard](https://pypi.org/project/keyboard/)

See demo [here](https://github.com/kawangwong/handtracking_mouse/blob/main/demo.mp4) Download button is on the right.

<h2>Use case scenario</h2>

For end users, this can be a tool to just browse the computer with the hand as if it was an air gestured movement.

For the therapy space, this can be used as a therapy tool to create treatment sessions that are task-oriented with levels of grading through resistance.
In the realm of therapy, it can certainly be used as a replacement input for human interface with the computer, especially for patients that may no longer be able to use their
hands or digits for trackpads or mouse movements.

<h2>Instructions</h2>

<h3>Installation</h3>

This program was written using Python3. Installation Instructions can be found [here](https://www.python.org/downloads/).

[Download](https://www.alphr.com/download-files-github/) the code or clone this repo, or even fork it.

Open up the terminal and `python` or `python3` should be a command that is readily available to you. Troubleshooting for installation will not be covered here, but generally if they can not be invoked, it is most likely a issue with a [Path environment](https://docs.python.org/3/using/windows.html).

Once python is installed, you need to use `pip` command to install the required libraries that this program needs. Usually that command is `pip install -r requirements.txt`

Once that is done, just run the program in the terminal of your using `python script.py` or `python3 script.py`

<h3>How to use</h3>

The program has a user setting file, which can be used to toggle on and off various functions. The way this program works will be that the camera will see the hand, then take an input from that location relative to how your camera sees the image, and then convert that data into coordinates that are relative to the size of your screen. The program will also listen to inputs from the keyboard for the keyboard input for the letter "e" which will then invoke the left click function of a mouse.

I have added custom settings to this to allow for also programmable keys to be used for left click mapping. For now, it will only take in letters and numbers as special characters can get a little too complex.

<h3>Anticipated changes</h3>

For now, I want to improve on some of the smoothness of the mouse movements as the program detects changes on a pixel level that can affect user experience since the detection of the data is converted from a small number to larger number in resolution. You can see in the code that the base camera input is 640x480 and upscaled to a higher resolution when used with a higher resolution screen.

I also wanted to do gesture based digit tracking button clicks, but due to the jumpiness already and the high level of resource intense, I tried to lean down the use of as many resources as possible.

<h2>Learned</h2>

From this, I learned more about data manipulation through the use of converting enumerables to string and string iteration. I've learned new built in methods such as `dir` to help debut and further understand libraries that have little documentation available. Last I've learned how to utilize return statements in a more efficient manner, which can help with future projects.

<h2>Thanks</h2>

I wanted to thank my classmate [Hector](https://www.linkedin.com/in/hector6921) for helping me troubleshoot some of the issues that I ran into regarding enumerable classes that are exist in this library and how data is placed. Hector is also exploring some of these applications now in the browser space as a result of looking at this project, so you should definitely check out his [work](https://github.com/hector6921).

<h1>Disclaimer</h1>

This is just a software used as a showcase and possible use in practical applications. I have not tested this as a use in a commercial setting and i take no responsibiliity for
how the end user will use this. There is no support and will be used as is.
