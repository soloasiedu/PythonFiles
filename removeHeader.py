import csv, os

os.chdir(r'C:\Users\SOLO\Documents\delicious')


os.makedirs('headerRemoved', exist_ok = True)

for csvFilename  in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    print('Removing header from '+ csvFilename + '...')
    csvRows = []
    csvFile = open(csvFilename)
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        if csvReader.line_num == 1:
            continue
        csvRows.append(row)
    csvFile.close()

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    writerFile = open(os.path.join('headerRemoved',csvFilename), 'w', newline='')
    csvWriter = csv.writer(writerFile)
    for row in csvRows:
        csvWriter.writerow(row)
    writerFile.close()
