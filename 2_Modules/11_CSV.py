#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# In this tutorial we will be working with CSV module
# ===================================================================================================
# ________________________ Reading CSV________________________
# 1. Open the file using open() method
# 2. Pass the file object to the csv.reader method
# 3. Put the data into the list by passing the object into the list() method
#    - you will get the list of strings
# 4. You can access the list items through list[0][1] for example
# --when dealing with large files use for loops when reading the files
# --read object can be looped over once; to do that again you need to call reader object again
# ________________________ Working with reader object________________________
# reader.line_num - when reading line by line you can use this attribute to get the line num
# ________________________ Writing CSV________________________
# 1. Open file with 'w' and newline='' arguments
# 2. Pass the file object to the csv.writer method
# 3. Use writer.writerow(list) = method to write to csv file; it takes list as an argument
# 4. Module will automatically escape the , with ""
# 5. As an option you can specify delimiter='_' to specify how to separate items
# 6. You can also specify how to separate lines with lineseparator='\n\n'
# ===================================================================================================

import csv

reader_file = open('1_Working_files/example.csv')
reader = csv.reader(reader_file)
csv_data = list(reader)
print(csv_data)
print(csv_data[0][0])
reader_file.close()

# dealing with large files
reader_file = open('1_Working_files/example.csv')
reader = csv.reader(reader_file)
for row in reader:
    print('Row #:', str(reader.line_num) + str(row))
reader_file.close()

# writing into the CSV file
writer_file = open('1_Working_files/output.csv', 'w', newline='')
writer = csv.writer(writer_file, delimiter='\t', lineterminator='\n\n')
writer.writerow(['spam', 'eggs', 'hello, world'])
writer.writerow([1, 1.55555, 700])
writer_file.close()

