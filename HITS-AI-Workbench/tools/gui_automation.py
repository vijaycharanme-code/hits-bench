import pyautogui
import pynput
from pynput.keyboard import Key, Controller
import time

def type_text(text: str):
    keyboard = Controller()
    for char in text:
        keyboard.type(char)
        time.sleep(0.01)

def click_screen(x: int, y: int):
    pyautogui.click(x, y)
