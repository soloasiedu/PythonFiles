import PyPDF2, os

os.chdir(r'C:\Users\SOLO\Documents\PythonFiles')
os.makedirs('CombinedPdfs', exist_ok=True)
filenames = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        filenames.append(filename)
    

#print(filenames)
filenames.sort()
#print(filenames)
pdfWriter = PyPDF2.PdfFileWriter()
for filename in filenames:
    print('Adding '+filename+' ...')
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    if pdfReader.isEncrypted == True:
        if pdfReader.decrypt('swordfish') == 1:
            for pageNum in range(1, pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
        else:
            continue
    else:
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
resultPdf = open(os.path.join('CombinedPdfs', 'allpdfs.pdf'), 'wb')
pdfWriter.write(resultPdf)
pdfFile.close()
resultPdf.close()



