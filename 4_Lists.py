#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# ===================================================================================================
# +++++++++ Lists +++++++++
# list[1] - extract item from the list using the index; index starts at 0
# list[num] = variable - assign something to the list using index
# str(list) - turn list into a string

# list.append() - append variable to the end of the list
#               - used in the loops
# list.insert(where, what) - insert value into the list using the index position
# list.remove(what) - removing item from the list
#                   - removes by the value
# del list[index] - delete item from the list using index
# list.index(value) - get the index of certian value in the list
#                   - retunrs index number if the value exists
# list.pop(position) - pop the item from certain position in the list; 0 by default
# list.sort(reverse=True) - sort list alphabetically; use reverse if reverse sorting is needed
# list.reverse() - reverse the existing sorting in the list

# ===================================================================================================

# inserting a value at the end and in the middle
list1 = [1,2,3,4,5]
list1.insert(5, 6)
print(list1)
list1.insert(1, 'cat')
print(list1)

# removing the '4' and 'cat' items from the list
list1.remove(4)
list1.remove('cat')
print(list1)

# removing item 3 from the list using index position
del list1[2]
print(list1)

# using index() method to return the index of the position
list1.append('hello')
print(list1)
print(list1.index('hello'))

# let's pop '2 from the list
list1.pop(1)
print(list1)

# typically you use for loops to work woth lists
list3 = ['jack', 'mary', 'thomas']
for i in range(0, 3):
    print("Hello, " + list3[i].capitalize())

# sorting list using sort() method
list4 = ['bmw', 'audi', 'nissan', 'vw', 'toyota']
print(list4)
list4.sort(reverse=True)
print(list4)
