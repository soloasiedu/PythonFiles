import pyglet
import os

os.chdir(r'C:\Users\SOLO\Documents\PythonFiles')


#file = pyglet.resource.media('clearly.mp3')
##file = pyglet.resource.media('that-was-quick.mp3')
##file.play()
##
##pyglet.app.run()
##pyglet.app.exit()


def play_mp3(filename):
    file = pyglet.resource.media(filename)
    file.play()
    pyglet.app.run()
    pyglet.app.exit()
    

play_mp3('that-was-quick.mp3')
