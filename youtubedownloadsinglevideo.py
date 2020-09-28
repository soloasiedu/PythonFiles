import os
import pyperclip
from pytube import YouTube
import textMyself

os.chdir(r'C:\Users\SOLO\Downloads')

link = pyperclip.paste() #'https://www.youtube.com/watch?v=fN017XSZN44'

try:
    yt = YouTube(link)
    print(yt.title)
    stream = yt.streams.first()
    stream.download()
    print('Task Completed!')
    textMyself.textmyself(str(yt.title)+'Video from youtube just finished downloading')
except:
    print("Connection Error")




    
    
        
