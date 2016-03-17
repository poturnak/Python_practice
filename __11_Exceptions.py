#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# +++++++++ Exceptions +++++++++
# you can create your own exceptions within the program and then use try except method using your exceptions
# for example
# if x == 1:
# raise exception ('X must not be 1!)
# then further in the program you can use try except
# try xxxxx
# except Exception as err:
# xxxxx
# you can gracefully display the exception data, but at the same time get the traceback chain
# you need to import traceback
# then if there is exception, get traceback.format_ex() somewhere (for example, you can print it to file)
# you can also use assertions (assert the some condition is true or false)
# if assertion fails, an exception is generated
# assert variable == 'hello', "It is actually not hello'
# if condition is not met, the line after the comma is displayed
# ===================================================================================================

""""# In this file we will be practicing python exceptions

try:
    print(5/0)
except ZeroDivisionError:
    print('You can not divide by 0')

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You can not divide by 0')
    else:
        print(answer)

filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print('There is no such file')

# If you want to fail siliently you can use pass method
# try:
#    print()
# except FileNotFoundError:
#    pass
# else: print()

print('Please provide the first number')

while True:
    try:
        number1 = int(input())
    except ValueError:
        print('Please, enter the number and not text\n')
    else:
        break
print('Please provide the second number')

while True:
    try:
        number2 = int(input())
    except ValueError:
        print('Please, enter the number and not text\n')
    else:
        break"""

file_name = 'cats.txt'

try:
    with open(file_name) as file__object:
        file_lines = file__object.readlines()
except FileNotFoundError:
    pass
else:
    for i in file_lines:
        print(i.capitalize())


