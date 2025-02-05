import pyautogui
import time
import random

# Sleep for a few seconds to give you time to focus the Discord window
time.sleep(5)

# Commands and options

# Main loop
while True:

    # Other commands
    pyautogui.typewrite("pls hunt")
    pyautogui.press("enter")
    time.sleep(random.uniform(2, 4))

    pyautogui.typewrite("pls beg")
    pyautogui.press("enter")
    time.sleep(random.uniform(2, 4))

    pyautogui.typewrite("pls dig")
    pyautogui.press("enter")
    time.sleep(random.uniform(2, 4))


    # Deposit all money
    pyautogui.typewrite("pls dep all")
    pyautogui.press("enter")
    time.sleep(random.uniform(2, 4))
