import PyPDF2, os, textMyself

os.chdir(r'C:\Users\SOLO\Documents\PythonFiles')

pdfFile = open('encryptedminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

textFile = open('dictionary.txt', 'r')
words = []

for line in textFile.readlines():
    words.append(line.strip())
    words.append(line.strip().lower())

if pdfReader.isEncrypted == True:
    for word in words:
        if pdfReader.decrypt(word) == 1:
            print('Password is '+ word)
            print('Pdf accessed')
            #textMyself.textmyself('Password is '+word)
            pageObj = pdfReader.getPage(1)
            print('The first of the pdf contains\n'+pageObj.extractText())
            break
        else:
            print('Searching ...')
            continue
        
