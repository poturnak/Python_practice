#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
import re, sys

# Let's open the file and get the text out of it
with open('baby1990.html') as file_object:
    contents = file_object.read()

# Now we will parse the text and will get the year
year_regex = re.compile(r'Popularity\sin\s(\d{4})')
year_match = year_regex.search(contents)
if year_match:
    year = year_match.group(1)
else:
    print('Year was not found!')
    sys.exit()

# Now let's extract the names and numbers
names_regex = re.compile(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>')
names_match = names_regex.findall(contents)
if not names_match:
    print('No names were found')
    sys.exit()

final_list = []

for rank, male, female in names_match:
    if male not in final_list:
        final_list.append(male + ' ' + rank)
    else:
        print('Duplicate male name ', male)
    if female not in final_list:
        final_list.append(female + ' ' + rank)
    else:
        print('Duplicate female name ', female)

final_list.sort()
print(year + ':')
for i in final_list:
    print(i)