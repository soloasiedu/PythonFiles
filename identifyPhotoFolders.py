import os
from PIL import Image


os.chdir(r'C:\Users\SOLO\Pictures')
for foldername, subfolders, filenames in os.walk('C:\\Users\\SOLO\Pictures'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        if not (filename.endswith('.png') or filename.endswith('.PNG') or \
                filename.endswith('.jpg') or filename.endswith('.JPG')):
                numNonPhotoFiles += 1
                continue
        else:
            im = Image.open(os.path.join(foldername,filename))
            width, height = im.size
            if (width > 0 and height > 0):
                numPhotoFiles += 1
            else:
                numNonPhotoFiles += 1
    if numPhotoFiles > ((numPhotoFiles + numNonPhotoFiles)/2):
        print(os.path.abspath(filename))
    else:
        print('There are no photo folders in this directory')
        
