#pip install pyautogui
#pip install pynput
#pip install selenium
#pip install Pillow

import pyautogui
import math
import time
from pynput.mouse import Button, Controller
from selenium import webdriver
from PIL import ImageGrab

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://vole.wtf/perfect-circle/')
driver.maximize_window()

time.sleep(2)

fileOpen = open('coordinates.txt', 'r')
coords = fileOpen.readlines()

x, y = pyautogui.size()

pyautogui.moveTo(x/2, y/2)
pyautogui.click(button = 'left')

time.sleep(1)

mouse = Controller()

for i in range(len(coords)):
    coord = coords[i].split()
    pyautogui.moveTo(float(coord[0]), float(coord[1]))
    if i == 0:
        mouse.press(Button.left)

mouse.release(Button.left)