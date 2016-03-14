#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# ===================================================================================================
# +++++++++ Lists +++++++++
# list + list1 - for concatentaion you can just add lists
# list[1] - extract item from the list using the index; index starts at 0
# list[1:5]/[:5]/[:]/[1:] - getting/printing only certain items of the list
# list([2][2]) - if list contains a list you can double index
# list[num] = variable - assign something to the list using index
# str(list) - turn list into a string

# list.append() - append variable to the end of the list
#               - used in the loops
# list.insert(where, what) - insert value into the list using the index position
# list.remove(what) - removing item from the list
#                   - removes by the value
# del list[index] - delete item from the list using index
# list.index(value) - get the index of certain value in the list
#                   - retunrs index number if the value exists
# list.pop(position) - pop the item from certain position in the list; 0 by default
# list.sort(reverse=True) - sort list alphabetically; use reverse if reverse sorting is needed
# list.reverse() - reverse the existing sorting in the list
# list = list(range(100)) - creating list using range
# ---------------------- Copy the list ----------------------
# list = list1 - it is not copy but rather the reference assignment
#              - if list is changed then the list1 is changed as well
# list = list[:] - actual copy of the list
# copy.copy() - module will allow you to copy list and not just pass reference
#             - you need to import copy
#             - list = list1.copy()
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

# let's pop '2' from the list
list1.pop(1)
print(list1)

# typically you use for loops to work with lists
list3 = ['jack', 'mary', 'thomas']
for i in range(0, 3):
    print("Hello, " + list3[i].capitalize())

# sorting list using sort() method
list4 = ['bmw', 'audi', 'nissan', 'vw', 'toyota']
print(list4)
list4.sort(reverse=True)
print(list4)

# in this example we will multiply each integer in a list by certain number
my_list = [3, 5, 15, 16, 4, 25, 66]
multiple = 5

for i in range(0,len(my_list)):
    my_list[i] *= multiple

print("Modified list")
print(my_list)

# creating a list automatically
auto_list = list(range(1,100))
print(auto_list)

# printing only certain items in the list
listing = [i for i in range(1,11)]
print(listing)
print(listing[:5]) # print everything that is below position 5
print(listing[3:5]) # print everything that is between 3 and 5

# creating a new list from the list or a slice
total_list = listing[:] # copying one list into the other using slice
print(total_list)
print(listing)

listing.append('total')
print(listing)
print (total_list)

# there is a copy module that will allow to copy list, but not its refence
import copy

list_original = [1,2,3,4,5]
list_copy = copy.copy(list_original)

list_original.remove(3)
print(list_original)
print(list_copy)
