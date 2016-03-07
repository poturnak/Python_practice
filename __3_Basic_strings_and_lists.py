import os

cur = os.getgid()
print(cur)

import time

message= "here is the message"
simbol = ""

final = message+simbol

print(final)
print("new line")

name = "ada"
print(name.title())

message = message.upper()

print(message)

name1 = "ada"
last_name = name1.capitalize() + " " + "Poturnak"

print(last_name)

last_name1 = "Ada" + " Nikolay"
print(last_name1)

print('\tNikolay' + " \nPoturnak")

white = "   python"
print(white)
white = white.lstrip()
print(white)

m1 = "Hello, "
name2 = "david"
end = "How are you doing?"
sentence = m1 + name2.capitalize()+"! " + end
print(sentence)

num1 = 2
num2 = 3

print(num1 + num2)

p1 = "Happy "
p2 = 23
p3 = "rd Birthday"

p4 = p1 + str(p2) + p3
p5 = "happy " + str(p2) + " Birthday"

print(p4)
print(p5)
print("happy " + str(p2) + " Birthday")

print(5 + 3)

list1 = [5, 5, "hello"]
print(list1)
print(list1[2])

list1[1] = "changed"


print(str(list1[0]) + " days")
print(list1)

list1.append('once')
print(list1)

list1.insert(1, 'cool')
print(list1)

list1.remove(list1[0])
print(list1)

del list1[0]
print(list1)

print("\n\n")

print(list1)
temp = list1[1]
print(temp)
list1.remove(list1[1])
print(list1)
print(temp)

list2 = ['orange', 'tomato', 'apple']
print(list2)
list2_pop = list2.pop(1)
print(list2)
print(list2_pop)

list3 = ['jack', 'mary', 'thomas']
for i in range(0, 3):
    print("Hello, " + list3[i].capitalize())

print("\n" + list3[1].capitalize() + " will not be able to come")

popped = list3.pop(1)

for i in range(0, 2):
    print("Hello, "+list3[i].capitalize())

new_guest = "Lory"
print('\nBut now '+new_guest.upper() + " will come.")

list3.insert(1, new_guest)
print(list3)
list3.pop(-1)
print(list3)

list4 = ['bmw', 'audi', 'nissan', 'vw', 'toyota']
print(list4)
list4.sort(reverse=True)
print(list4)

print("\n\n")
print(list4)
list4.reverse()
print(list4)

print(len(list4))

string1 = "hello nikolay"
print(len(string1))
print(string1[:-2])

