from cmath import pi
import pyautogui
from time import sleep
with open("pi.txt") as file:
    pi_txt = file.read()

sleep(5)

for i in range(4, len(pi_txt)):
    sleep(0.5)
    sleep(i*0.5)
    pyautogui.typewrite(pi_txt[:i])