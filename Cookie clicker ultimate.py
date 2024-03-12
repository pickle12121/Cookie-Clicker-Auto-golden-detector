import cv2
import numpy as np
import pyautogui
import time
import keyboard
import threading

start = False





def click_thread():
    while start:
        detect_and_click(templatelst)

# Function to find the template image in the screen image
def find_image(template, screen):
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # You can adjust the threshold based on your needs
    threshold = 0.50
    if max_val > threshold:
        print("success",max_val)
        return max_loc
    else:
        print("fail",max_val)
        return None


# Function to handle the image detection and click
def detect_and_click(templatelst):
    # Load the template imaget
    print("exited")
    match_location = None
    # Capture the screen image
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    screen_cv = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)

    # Rotate the template image for matching
    # rotated_template = rotate_image(template, rotation_angle)

    # Find the template in the screen
    for temp in templatelst:
        if match_location is None:
            match_location = find_image(temp, screen_cv)
            template = temp

    if match_location is not None:
        # Click on the center of the matched template
        print("F")
        x, y = match_location[0] + template.shape[1] // 2, match_location[1] + template.shape[0] // 2
        pyautogui.click(x, y)
    # Pause for a short duration before the next iteration
    time.sleep(1)

# Example usage
template_pathOne = r'C:\Users\Daniel\PycharmProjects\pythonProject\.venv\golden cookie storage\0bb6627fee7063a7b79fdb4742249af.png'
template_pathTwo = r'C:\Users\Daniel\PycharmProjects\pythonProject\.venv\golden cookie storage\40bf37f40ec1f61b38763e43a1817e8.png'
template_pathThree = r'C:\Users\Daniel\PycharmProjects\pythonProject\.venv\golden cookie storage\47cb7469370c0cefc0b2acce5a149d8.png'
template_pathFour = r'C:\Users\Daniel\PycharmProjects\pythonProject\.venv\golden cookie storage\62239ab9aa3f977a34c6a9b2957a80e.png'
template_pathFive = r'C:\Users\Daniel\PycharmProjects\pythonProject\.venv\golden cookie storage\c719b20826f8414435e3abb238dee55.png'
template_pathSix = r'C:\Users\Daniel\PycharmProjects\pythonProject\.venv\golden cookie storage\ea7e1c3eced72f77fb085419c563eb2.png'
template_pathSeven = r'C:\Users\Daniel\PycharmProjects\pythonProject\.venv\golden cookie storage\eb6db1858a99ffd5b54f85cf09048e5.png'
templatelst = [cv2.imread(template_pathOne),
                cv2.imread(template_pathTwo),
                cv2.imread(template_pathThree),
                cv2.imread(template_pathFour),
                cv2.imread(template_pathFive),
                cv2.imread(template_pathSix),
                cv2.imread(template_pathSeven),
               ]




def constantClicking():
    cx, cy = pyautogui.position()
    while start:
        pyautogui.click(cx, cy, clicks=30, interval=0.00001)


constantClicking = threading.Thread(target=constantClicking)
constantClicking.daemon = True



def startRun():
    global start
    start = True
    click_thread.start()
    constantClicking.start()

def ToggleRun():
    global start
    if start:
        start = False
    else:
        start = True
        # constantClicking = threading.Thread(target=constantClicking)
        # constantClicking.daemon = True
        # constantClicking.start()

click_thread = threading.Thread(target=click_thread)
click_thread.daemon = True


# Setting up the hotkey
keyboard.add_hotkey('t', startRun)
keyboard.add_hotkey('p', ToggleRun)

try:
    keyboard.wait('esc')  # Press 'esc' to exit the program
except KeyboardInterrupt:
    pass
finally:
    keyboard.remove_hotkey('t')
templatelst = [cv2.imread(template_pathOne),
                cv2.imread(template_pathTwo),
                cv2.imread(template_pathThree),
                cv2.imread(template_pathFour),
                cv2.imread(template_pathFive),
                cv2.imread(template_pathSix),
                cv2.imread(template_pathSeven),
               ]




def constantClicking():
    cx, cy = pyautogui.position()
    while start:
        pyautogui.click(cx, cy, clicks=30, interval=0.00001)


constantClicking = threading.Thread(target=constantClicking)
constantClicking.daemon = True



def startRun():
    global start
    start = True
    click_thread.start()
    constantClicking.start()

def ToggleRun():
    global start
    if start:
        start = False
    else:
        start = True