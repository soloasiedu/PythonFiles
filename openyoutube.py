import time
import os
import pyautogui


os.chdir(r'C:\Users\SOLO\Documents\PythonFiles')

pyautogui.moveTo(456, 876, duration = 0.5)
time.sleep(2)
#pyautogui.drag(367, 771, duration = 0.5)
pyautogui.click(367,771)
time.sleep(3)
##try:
##    pyautogui.click('youtubelogo.jpg')
##except:
##    print('Image  could not be found')

if pyautogui.pixelMatchesColor(325,369, pyautogui.pixel(325,369)):
    pyautogui.click(325,369)

    

