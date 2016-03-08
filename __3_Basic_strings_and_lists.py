#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

#  - indexing with string[0:1]
#  - check 'abs" in/not in string
#  upper(), lower(), isupper(), islower(), capitalize(), title() - check lower, upper letters
#  isalpha(), isalnum(), isdecimal(), isspace(), istitle() - check what type of string you are dealing with
#  startwiht(), endwith() - check if string ends or starts with something
#  join() and split() - combine a list of strings, split strings into a list
#  rjust(), ljust(), and center() - justify the string within the string of certain lenght
#  rstrip(), lstrip(), strip() - remove whitespaces
# pyperclip module  - for sending the text in and out of the clipboard

import os
import pyperclip

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

# additional infomration from automate with python book
# TO PRINT A STRING WITH BACKSLASHES YOU need yo create a ran string
# that can be done with r character

print(r'Hello my \man')

# sliceing a string is done using colon addresses. String numberign starts with 0

test_string = 'Hello World'
print(test_string[0:5])

# you can also use logical tests on strings
# for example lets' check if 'Hello' and 'Nikolay' are in the string

if 'Hello' in test_string:
    print('it is there')
else:
    print('it is not there')

# isupper() islower() methods will return boolean values true or false
# is islower is applied and all letters are low the value is true

# there are some other methods

 # - isalpha() returns True if the string consists only of letters and is not blank
 # - isalnum() returns True if the string consists only of letters and numbers and is not blank
 # - isdecimal() returns True if the string consists only of numeric characters and is not blank
 # - isspace() returns True if the string consists only of spaces, tabs, and new-lines and is not blank
 # - istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters

# starstwith() - pass the value and see if the string starts with that value
# endswith() - pass value and see if string ends with that value

# there is a special method to join/concatenate the strings
# this method must be called on a string. At the beginning we use the separator

string11 = 'is my love'
string22 = 'tatyana'

string22 = ' '.join([string22.lower().capitalize(), string11.lower(), '!'])
print(string22)

# join() is called on a string and it gets list of strings to join
# split() is called on a string and it returns a list of strings

print(string22.split())

# you can pass a parameter on what you need to split on. Typically that would be ' '
# however you can use \n for example to split into the list of strings that begin the new line

# you can also justify string into a string of certain length
# for example lets justofy 'hello' to the right into a string of 25 characters

print('Hello'.rjust(25))

# we can also substitute spaces for something else

print('Hello'.rjust(25, '^'))

# we have rjust(), ljust(), center()

print(' Fuck it! '.center(100, '='))

# you can also use rstrip() lstrip() and strip() to get rid of spaces on left and right sides
# the string will take care of all whitespaces at the beginning and end
# you can also specify which things you want to strip

# you can use pyperclip to copy and paste stuff into the clipboard
# ifr something was already copied into the clipboard, pyperclip.paste() will return that stuff

pyperclip.copy('Hello')
print(pyperclip.paste())
