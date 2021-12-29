#pip install pyautogui
#pip install pynput
#pip isntall selenium

import pyautogui
import math
import time
from pynput.mouse import Button, Controller
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://vole.wtf/perfect-circle/')
driver.maximize_window()

time.sleep(2)

r = 427
x = 960
y = 587

fileOpen = open('coordinates.txt', 'r')
coords = fileOpen.readlines()
coords = [line.strip('\n') for line in coords]

pyautogui.moveTo(x, y)
pyautogui.click(button = 'left')

time.sleep(1)

mouse = Controller()
#fileWrite = open('coordinates.txt', 'w')

for i in range(370):
    #fileWrite.write(str(x+r*math.sin(math.radians(i))) + ' ' + str(y+r*math.cos(math.radians(i))+'\n'))
    coord = coords[i].split()
    if i%6 == 0:
        if i >= 120 and i <= 270:
            pyautogui.moveTo(float(coord[0])+1, float(coord[1])+2)
        elif i>= 270:
            pyautogui.moveTo(float(coord[0])-1, float(coord[1])-1)
        else:
            pyautogui.moveTo(float(coord[0])+0.5, float(coord[1]))
    if i == 0:
        mouse.press(Button.left)

mouse.release(Button.left)