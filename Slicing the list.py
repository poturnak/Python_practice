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

