#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# In the python file we will explore how to work with files in python
# ===================================================================================================
# +++++++++ Working with relative and absolute paths +++++++++
# os.getcwd() - will return current working directory
# os.chdir() - change directory to something else
# os.makedir() - create new directory
# os.path.join(path, path) - you can be joining say directory and filename to create one path
# os.path.abspath(path) - easy way to convert relative path to absolute path
# os.path.isabs(path) - will return True if the argument is an absolute path
# os.path.relpath(path, start) - will return a string of a relative path from the start path to path
# os.path.dirname(full path) - returns the full directory name (before the last /)
# os.path.basename(full path) - returns the base name (after the last /)
# os.path.split(path) - returns tuple of directory name and base name
# os.path.getsize(path) - will return the file size defined by path
# os.listdir(path) - returns a list of file names in the defined directory
# os.path.exists(path) - the easiest way to check is the directory exists
# os.path.isfile() - returns true if path is a file and exists
# os.path.isdir() - returns true if path is a directory and exists
#  ./ - meaning in this folder/path
#  ../ - meaning in the parent directory
# ===================================================================================================
# +++++++++ The file writing and reading process +++++++++
# 1. use open() method to return the file object
# 2. apply read() or write() method
# 3. close the file with close() method
# open() returns the file object
#        open() can use parameters
#        'r' - read 'w' - write 'a' - append 'r+' - read/write
# file_object.read() - will read all contents of the file into a string
# file_object.readlines() - will read all lines into a list of lines
# file_object.write() - will write contents toa file
# 'r' - overwrites the file
# 'a' - adds stuff to the file
# shelve - module is used to store variables into a file
#          you create a file using open() method
#          and store variables there like in a dictionary
# pprint.pprint() - module used to pretty print the list or dictionary
# ===================================================================================================

import os
print(os.getcwd())
print(os.path.abspath('.'))
print(os.path.dirname('json.json'))
print(os.listdir('.'))

# Opening the file is preferable with 'with method'. it makes sure that the file is properly closed.
# Opening the file will create an object
# In the example below we are reading the file as a string

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# In this example we are printing file line by line
with open('pi_digits.txt') as file_object:
    for i in file_object:
        print(i.rstrip())

# In this example we will store each line of the file in the list
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for i in lines:
    print(i.rstrip())

# Lets try to build one string off of this file

pi_string = ''
for i in lines:
    pi_string += i.strip()

print(pi_string)

# Writing to the file requires opening the file with w parameter
# You can open file with r(read), w(write). a(append), r+(read and write) parameters

with open('programming.txt', 'w') as file_object:
    file_object.write('\nHello python 123')

print('Hello')

# In this example we will use shelve module to store python data there
# Shelve module stores data in a dictionary
import shelve
shelf_file = shelve.open('mydata')
cats = ['Mike', 'john']
shelf_file['cats'] = cats
shelf_file.close()

shelf_file = shelve.open('mydata')
a, b = shelf_file['cats']
print(a)
print(b)
shelf_file.close()

# In this example we will use pprint.pformat() to store python data in a text file
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
with open('cats.py', 'w') as file_object:
    file_object.write('cats = ' + pprint.pformat(cats))
