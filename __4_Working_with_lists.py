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
