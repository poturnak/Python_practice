# Opening the file is preferrable with With method. it makes sure that the file is properly closed.
# Opening the filw will create an object

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# In this example we are reading line by line
with open('pi_digits.txt') as file_object:
    for i in file_object:
        print(i.rstrip())

# In this example we will store eatch line of the file in the list
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for i in lines:
    print(i.rstrip())

# You can also be reading the file line by line

with open('pi_digits.txt') as file_to_open:
    for i in file_to_open:
        print(i.rstrip())

# Lets try to build one string off of this file

pi_string = ''
for i in lines:
    pi_string += i.strip()

print(pi_string)

string = 'Hello cat'
print(string.replace('cat', 'dog'))
print(string)

# Writing to the file requires opening the file with w parameter
# You can open file with r(read), w(write). a(append), r+(readn and write) parameters

with open('programming.txt', 'w') as file_object:
    file_object.write('\nHello python 123')

print('Hello')




