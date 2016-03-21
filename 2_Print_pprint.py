#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# +++++++++ Print function +++++++++
# Print() will automatically add the new string at the end
# print('text', end='') - add what you want to add at the end of the line
# print('text', sep=',') - decide what separator to use between items
# ===================================================================================================
# +++++++++ Print function +++++++++
# pprint module is used for pretty printing of python objects
# if you get json, you need to decode it into python object first
# for example, you can apply json.loads then you will pass it to pprint
# pprint only will get python object as input
# you need to import pprint
# pformat() - format a Python object into a pretty-printed representation
# pprint() - pretty-print a Python object to a stream
# ===================================================================================================
# adding space at the end while printing
print('Hello', end=' ')
print('World')

# You can also define what separator to use with print() function
print('dog', 'cat', 'cow')
print('dog', 'cat', 'cow', sep=', ')

# in this case we will use pprint
import pprint
list = ['cat', 'dog', 'mouse']
dictionary = {'A': '[65, 66, 67, 68, 69]', 'C': '[67, 68, 69, 70, 71]', 'B': '[66, 67, 68, 69, 70]', 'E': '[69, 70, 71, 72, 73]', 'D': '[68, 69, 70, 71, 72]'}
pprint.pprint(list, indent=5)
pprint.pprint(dictionary)
print(dictionary)
