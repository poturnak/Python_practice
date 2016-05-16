#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# In this python file we will explore how to work with functions in python
# ===================================================================================================
# +++++++++ Functions +++++++++
# def function_name (arguments to pass)
# def function (x) - pass 1 variable x
# def function (*x) - pass variable number of arguments
#                   -  args will become a list here
# def function (**x) - pass variable number of arguments
#                    - you need to pass key:value pairs
#                    - x will become dictionary
# def function (x = 'default) - you need to pass x, if you do not, default value will be used
# function can return the value if you use 'return value in the end'
# when variable is passed to function it is unchanged (passed as value)
# when list is passed to the function it will be changed (passed as reference)
# if you want to change global variable in the function declare it as global
# +++++++++ Importing modules and functions +++++++++
# you can import the function in 2 ways
# 1. you can import the whole module" import module_name, then use module_name.function_name() to call function
# 2. You can import specific function 'from module_name import function_name 1, function_name 2'
# For conflicting names, you can give a function a name: from module import function_name as alias
# You can also import a module with an alias: import module_name as alias
# ===================================================================================================
# Here is a simple function

def greet_user():
    """Function to greet user"""
    print('Hello')

def greet_friend(username):
    print('Hello ' + username + '!')

greet_friend('Nikolay')

# There are other ways to pass arguments to a function. Moreover you can define the default arguments
# In the example below dog will be used by default. In case you need cat, just pass cat as an argument
# Default parameters need to be listed after the open parameters

def define_pet (pet_name, pet_type = 'dog'):
    print("My pet's name is " + pet_name)
    print("My pet's type is " + pet_type)

define_pet (pet_name = 'Tracy')

# Functions can also be returning the values. It can be one value or a set of values.

def full_name (first_name, last_name):
    formatted = (first_name.capitalize() + ' ' + last_name.capitalize())
    return formatted

i = full_name('nikolay', 'poturnak')

print(i)

# Sometime we can make some of the arguments optional. In the following example we work with optional middle names

def full_3_names (first, last, middle = ''):
    if middle:
        print(first.capitalize() + ' ' + middle.capitalize() + ' ' + last.capitalize())
    else:
        print(first.capitalize() + ' ' + last.capitalize())

print('\n')
full_3_names('Nikolay', 'Poturnak')
full_3_names('Tatyana', 'poturnak', 'Dmitrievna')

# Sometimes while passing the list to a function, you may want to preserve the contents of the list
# to do that you send a copy to the function by work(list_name[:])
# by default if you pass variable to function it is pass by value
# if you pass list it is list by reference
# to pass list by pass by value you need to use [:]

x = 500

def change (y):
    y += 1

change(x)
print(x)

# you can also create a function that will consume arbitrary number of arguments

def arbitrary (*toppings):
    """this function demonstrates arbitrary arguments"""
    for i in toppings:
        print(i + '\n')

arbitrary('low', 'high')

# you can also mix positional and arbitrary arguments function (parameter1, *parameter2)
# in this example we can provide key-value arguments to the function

def build_profile(name, id, **parameters):
    profile = {}
    profile['name'] = name
    profile['id'] = id
    for i,j in parameters.items():
        profile[i] = j
    return profile

my_profile = build_profile('Nick', '123', hometown = 'Novosibirsk')
print(my_profile)

# more exercises

def automobile(model, year, **metadata):
    print('Your model is ' + model)
    print('Your year is ' + str(year))
    for i,j in metadata.items():
        print(i, j)

automobile('vw', 2009, color = 'red')

# Sometimes you want to modify the global variable within the function
# For that you need to use 'global' within the function

testing_var = 100
def testing():
    global testing_var
    testing_var += 1

testing()
print(testing_var)
