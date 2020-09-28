import os
import PyPDF2
import sys
os.chdir(r'C:\Users\SOLO\Downloads\Other')
password = ''.join(sys.argv[1:])

print(password)

os.makedirs('EncryptedPDF', exist_ok=True)

for folder, subfolder, filenames in os.walk(r'C:\Users\SOLO\Downloads\Other'):
    for filename in filenames:
            if not filename.endswith('.pdf'):
                continue
            else:
                print('Current file: '+filename)
                pdfFile = open(os.path.join(folder, filename), 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)
                newFilename = filename[0:len(filename)-4]+'_encrypted.pdf'
                print('Encrypting %s to %s ' %(filename, newFilename))
                pdfWriter.encrypt(password)
                resultedPdf = open(os.path.join('EncryptedPDF', newFilename), 'wb')
                pdfWriter.write(resultedPdf)
                resultedPdf.close()
        
        
        
