#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================

import openpyxl

# values to change
price_updates = {
    'Celery': 1.19,
    'Garlic': 3.07,
    'Lemon': 1.27
}

# opening the file
print('Loading the workbook...\n')
wb = openpyxl.load_workbook('../2_Modules/1_working_files/produceSales.xlsx')
sheet = wb.get_sheet_by_name('Sheet')

# looping over data
print('Modifying the data...\n')
for i in range(2, sheet.max_row):
    if sheet['A'+str(i)].value in price_updates:
        sheet['B' + str(i)].value = price_updates[sheet['A' + str(i)].value]

# saving the data into the new excel file
print('Saving to the new file...\n')
wb.save('../2_Modules/1_working_files/produce_Sales_updated.xlsx')

print('Done!')
