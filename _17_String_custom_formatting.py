#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# +++++++++ String format +++++++++
# in the old python notation we used % with some parameters to generate custom strings
# new python way is to use string.format() method to generate custom strings

name = 'Nikolay'
string = 'Hello {}'.format(name)
print(string)

# the string output will be 'Hello Nikolay'
# we can specify multiple arguments with several {}
# they are names and they start with 0, 1, 2, etc.
# arguments can be positional p0, p1, p2 etc. or named name=value
# positional argument needs to be accessed by placing number in {}, {1}
# keyword parameters are used by name=value pair
print('Hey {1} how are you {0}?'.format('fucking', 'Nikolay'))
print('Hey {name} how are you {action}?'.format(action='fucking', name='Nikolay'))
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42,11))
print("various precions: {0:6.2f} or {0:6.3f}".format(1.4148))
print("Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058))

# it is possible to left or right justify the number within the alloted space
print("{0:<20s} {1:6.1f}".format('Spam & Eggs:', 6.99))  # here the number is rounded to a whole