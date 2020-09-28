
import shutil
import os
import send2trash

os.chdir(r'C:\Users\SOLO\Downloads\Other')
for folderName, subfolder, filenames in os.walk(r'C:\Users\SOLO\Downloads\Other'):
    for file in filenames:
        if file.endswith('.pdf') or file.endswith('.PDF'):
            newpath = r'C:\Users\SOLO\Downloads\Other\PDFFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.mp4') or file.endswith('.m4v'):
            newpath = r'C:\Users\SOLO\Downloads\Other\VideoFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.pptx'):
            newpath = r'C:\Users\SOLO\Downloads\Other\PowerPointFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.zip'):
            newpath = r'C:\Users\SOLO\Downloads\Other\ZipFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.exe'):
            newpath = r'C:\Users\SOLO\Downloads\Other\ExecutableFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.mp3') or file.endswith('.m4a'):
            newpath = r'C:\Users\SOLO\Downloads\Other\MP3Folder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.dll'):
            newpath = r'C:\Users\SOLO\Downloads\Other\DLLFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.jpg') or file.endswith('.gif') or file.endswith('.png'):
            newpath = r'C:\Users\SOLO\Downloads\Other\ImagesFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.docx'):
            newpath = r'C:\Users\SOLO\Downloads\Other\WordDocumentFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.txt'):
            newpath = r'C:\Users\SOLO\Downloads\Other\TextFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.csv'):
            newpath = r'C:\Users\SOLO\Downloads\Other\ExcelSpeadsheetsFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.enc'):
            newpath = r'C:\Users\SOLO\Downloads\Other\ENCFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.msi'):
            newpath = r'C:\Users\SOLO\Downloads\Other\InstallersFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        elif file.endswith('.jar'):
            newpath = r'C:\Users\SOLO\Downloads\Other\JarFolder'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
                shutil.move(os.path.join(folderName,file), newpath)
            else:
                shutil.move(os.path.join(folderName,file), newpath)
        else:
                    send2trash.send2trash(os.path.join(folderName,file))
                    
        
                    
                




        


