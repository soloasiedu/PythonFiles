#! python3
import os
import send2trash
import re


for folderName, subfolders, filenames in os.walk(r'C:\Users\SOLO\Documents\delicious'):
    for name in filenames:
        if name.endswith('.txt'):
            path = os.path.join(folderName, name)
            #print(os.path.join(folderName, name))
            send2trash.send2trash(path) 
    for name in subfolders:
        if name.find('food') != -1:
            path = os.path.join(folderName, name)
            #print(os.path.join(folderName, name))
            send2trash.send2trash(path)




               



    
    

        





            

