# in this example we will multiply each integer in a list by certain number

my_list = [3, 5, 15, 16, 4, 25, 66]
multiple = int(input('Please, enter the multiple you want\n'))
print("Original list")
print(my_list, '\n')

for i in range(0,len(my_list)):
    my_list[i] = my_list[i] * multiple

print("Modified list")
print(my_list, '\n')

print("Sorted list")
my_list.sort()
print(my_list)

# in this example we will print all items of the list
# we will use the list my_list

for i in my_list:
    print(i)

# in this example we will do multiplication as well but using simpler methodology
counter = 0

for k in my_list:
    my_list[counter] = k * multiple
    counter += 1

print(my_list)

# creating a list automatically
auto_list = list(range(1,100))
print(auto_list)

skipped_list = list(range(2,100,3))
print(skipped_list)

squares_list = []
m = 0

for i in range(1,11):
    square = i**2
    squares_list.append(square)

print(squares_list)

print(min(squares_list))
print(max(squares_list))
print(sum(squares_list))

# using a loop to print numbers from 1 to 20

millist = list(range(1,1000000))
print(millist[-1])
print(sum(millist))

multilist = [i*3 for i in range(1,10)]
print(multilist)

print('Hello')

# printing only certain items
#  in the list

listing = [i for i in range(1,11)]

print(listing)
print(listing[:5]) # print everything that is below position 5
print(listing[3:5]) # print everything that is between 3 and 5

# looping through the sliced list

new_list = []
for i in listing[-3:]:
    print(i)
    new_list.append(i)

print(new_list)

#creating a new list from the list or a slice

total_list = listing[:] # copying one list into the other using slide
print(total_list)
print(listing)

listing.append('total')
print(listing)
print (total_list)

# that means we can not just copy one list to another. We have to specify slice

list3 = [i for i in listing[:]]
print(list3)
listing.append('hello')
print(listing)
print(list3)

# If list contains a list you can use double index

alpha = [[11,12,13], 55, [11,66,77]]
print(alpha[2][2])

# For list concatenation you can just add the list to another list

alpha = alpha + [333, 444]
print(alpha)

# You can also identify the index of a certain item in the list using the index() method

index = alpha.index(55)
print(index)

# del will remove the item in the list based on the index
# del alpha[1] (with index 1)
# remove will remove the item in the list based on its value
# alpha.remove('cat')

# sort method sorts items in the list

listt = [5,6,7,3,4,5,8,12,55]
listt.sort()
print(listt)

listt.sort(reverse=True)
print(listt)

# you can use functions list() and tuple() to convert things into list or tuple
value = list('hello')
print(value)

# List are different than variables
# When you create a variable, say num = 6 you pass the value of 6 to num
# When you create a list, list = [1,2,3], list will store the reference to list [1,2,3]
# if you do list = list1, both variables will refer to the same list
# keep this in mind when you pass list to functions.
# in this case the reference will be passed, and the list will be modified as a result in the global space

# there is a copy module that will allow to copy list, but not its refence

import copy

list_original = [1,2,3,4,5]
list_copy = copy.copy(list_original)

list_original.remove(3)
print(list_original)
print(list_copy)

# In this case the list_copy is not changed because copy.copy() is used
# If multiple lists are used within the list you need to use copy.deepcopy()
# alternatively you can use list1 = list1[:]

