#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================

# importing the excel module and opening the file
import openpyxl
print('Opening the workbook...')
wb = openpyxl.load_workbook('../2_modules/1_working_files/censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')

# generating the slice to work with
counties = sheet['C2': 'C72865']
all_data = sheet['A2': 'D72865']

print('Calculating...\n')
# create dictionary with all counties
dict = {}
for i in counties:
    for j in i:
        if j.value not in dict.keys():
            dict[j.value] = {}
            dict[j.value]['tracts'] = 0
            dict[j.value]['population'] = 0

# counting the number of tracts and total population
for i in all_data:
    dict[i[2].value]['tracts'] += 1
    dict[i[2].value]['population'] += i[3].value

# printing final dictionary
print('County'.ljust(20), 'Tracts'.ljust(7), 'Population'.ljust(10))
for i in sorted(dict.keys()):
    print(i.ljust(20), ' ', str(dict[i]['tracts']).center(7), ' ', str(dict[i]['population']).center(10))
