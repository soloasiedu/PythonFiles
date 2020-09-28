from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (718,195)
    dinasaur = (485, 201)
    #510 = x cordinate to check for obstacle
    #y cordinate = 220



def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')

##def pressDown():
##    pyautogui.keyDown('down')
##    pyautogui.keyUp('down')

def imageGrab():
    box = (Cordinates.dinasaur[0]+ 70, Cordinates.dinasaur[1],
           Cordinates.dinasaur[0]+ 110, Cordinates.dinasaur[1]+25)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()


##def imageDuckGrab():
##    box = (Cordinates.dinasaur[0]+ 20, Cordinates.dinasaur[1]-25,
##           Cordinates.dinasaur[0]+ 50, Cordinates.dinasaur[1])
##    image = ImageGrab.grab(box)
##    grayImage = ImageOps.grayscale(image)
##    a = array(grayImage.getcolors())
##    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab() != 1255):
            pressSpace()
            time.sleep(0.1)

            
##        elif(imageDuckGrab() != 1005):
##            pressDown()
            #time.sleep(0.1)

main()

##restartGame()
##time.sleep(1)
##pressSpace()
