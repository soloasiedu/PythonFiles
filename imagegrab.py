from PIL import ImageGrab


##im = ImageGrab.grab(bbox = None)
##im.show()

im2 = ImageGrab.grab(bbox = (0, 0, 300, 300))
im2.convert('L')
im2.show()
