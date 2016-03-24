#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# importing the excel module and opening the file
import openpyxl, pprint
print('Opening the workbook...\n')
wb = openpyxl.load_workbook('../2_modules/1_working_files/censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')

# generating the slice to work with
counties = sheet['C2': 'C72865']
all_data = sheet['A2': 'D72865']

# create dictionary with all counties
dict = {}
print('Calculating tracts and population...\n')
for i in all_data:
    dict.setdefault(i[2].value, {})
    dict[i[2].value].setdefault('tracts', 0)
    dict[i[2].value].setdefault('population', 0)
    dict[i[2].value]['tracts'] += 1
    dict[i[2].value]['population'] += i[3].value

# counting the number of tracts and total population
for i in all_data:
    dict[i[2].value]['tracts'] += 1
    dict[i[2].value]['population'] += i[3].value

# printing final dictionary
print('County'.ljust(20), 'Tracts'.ljust(7), 'Population'.ljust(10))
for i in sorted(dict.keys()):
    print(i.ljust(20), ' ', str(dict[i]['tracts']).center(7), ' ', str(dict[i]['population']).center(10))

# now let's print this data to the python file
print('\nWriting to census_data.py file...\n')
with open('../2_modules/1_working_files/census_data.py', 'w') as file:
    file.write('all_data=' + pprint.pformat(dict))
print('Done!')