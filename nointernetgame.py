import pyautogui
from PIL import Image, ImageGrab
import time
#pyautogui.sleep(3)
#pyautogui.countdown(4)
##width, height = pyautogui.size
#pyautogui.click(994, 526)
#pyautogui.write(['enter', 'enter'])
#X_COORDINATE = 502
##while True:
##    if pyautogui.pixel(498, 222) == (83,83,83):
##        pyautogui.write('')

##if pyautogui.pixel(498, 222) == (83,83,83):
##    print('True')
##else:
##    print('False')

def click(key):
    pyautogui.keyDown(key)
    return

def isCollision(data):
    for i in range(510, 600):
        for j in range(190, 235):
            if data[i,j] < 90:
                click("down")
                return
    for i in range(490, 540):
        for j in range(165, 185):
            if data[i,j] < 30:
                click("up")
                return
    return

if __name__ == "__main__":
    time.sleep(5)
    #pyautogui.write('enter')
    click('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollision(data)

##        for i in range(510, 600):
##            for j in range(190, 235):
##                data[i,j] = 0
##
##        for i in range(490, 510):
##            for j in range(165, 185):
##                data[i, j] = 171
##
##        image.show()
##        break
