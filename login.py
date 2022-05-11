import pyautogui
import time

def login(username: str, password: str):
    time.sleep(2)
    pyautogui.click(986, 24)
    time.sleep(1)
    pyautogui.click(752, 750)

    time.sleep(4)
    pyautogui.typewrite(username)

    pyautogui.click(910, 730)

    time.sleep(6) #3
    pyautogui.typewrite(password)

    pyautogui.click(910, 680)

    time.sleep(4)
