"""

    Open the spreadsheet file.
    For each row, check whether the value in column A is Celery, Garlic, or Lemon.
    If it is, update the price in column B.
    Save the spreadsheet to a new file (so that you don’t lose the old spreadsheet, just in case).
"""
import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb['Sheet']
print('Updating cells...')
for row in range(2, sheet.max_row+1):
    if sheet['A'+str(row)].value == 'Celery':
        sheet['B'+str(row)] = 1.19
    elif sheet['A'+str(row)].value == 'Garlic':
        sheet['B'+str(row)] = 3.07
    elif sheet['A'+str(row)].value == 'Lemon':
        sheet['B'+str(row)] = 1.27

wb.save('produceSalesUpdated.xlsx')
print('Done.')


