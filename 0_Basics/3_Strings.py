#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# ===================================================================================================
# +++++++++ Strings +++++++++
# 'string1' + 'string2' - you can concatenate string just by adding them
# [0,1], [:5], [1:] - indexing strings, for example print certain symbols
# print(string[:-2]) - print string only till the -2 letter (from the end)
# print(r'') - print string in a raw format (do not interpret special symbols)
# 'word' in/not in 'string' - check if certain word is in the string or not
# len(string) - returns the length of the string
# str(variable) - turn something into a string (number, list, etc.)
# string.title() - make all word in a string to start with capital letter
# string.capitalize() - capitalize the first word in a string
# string.lstrip() - remove whitespaces on the left of string
# string.rstrip() - remove whitespaces to the right of string
# string.strip() - remove whitespaces on the left and right of string
# string.upper() - make all letters capital in the string
# string.lower - make all letter low in the string
# string.islower()/isupper() - returns true if all characters are upper/lowercase; returns boolean values
# string.isalpha() - returns True if the string consists only of letters and is not blank
# string.isalnum() - returns True if the string consists only of letters and numbers and is not blank
# string.isdecimal() - returns True if the string consists only of numeric characters and is not blank
# string.isspace() - returns True if the string consists only of spaces, tabs, and new-lines and is not blank
# string.istitle() - returns True if the string consists only of words that begin with an uppercase letter
# string.startwith()/endwith() - check if string ends or starts with something; returns boolean value
# ---------------- Joining & splitting strings ----------------
# ' '.join(['string1', 'string2']) - join in called on the set of strings that you want to merge
#                                  - start the command with 'separator'; will separate the strings
#                                  - input is the list; output is string
# string.split(separator) - split the string into multiple strings
#                - input is string; output is list
#                - enter the separator to split on; default is ' '
# ---------------- Justification --------------------
# string.rjust(total, '^') - justify string within the string
#                          - total is the new string length
#                          - symbol is what you will fill the emty symbols with; ' ' default
# string.ljust() - justify into the new string to the left
# string.center() - justify the string within the string of certain length
# ===================================================================================================

# removing whitespaces to the left in this example
white = "   python"
white = white.lstrip()
print(white)

# print string till 2 letter till the end
string1 = "hello nikolay"
print(len(string1))
print(string1[:-2])

# to print the string with special symbols and \ you need to print raw string
print(r'Hello my \man')

# slicing a string
test_string = 'Hello World'
print(test_string[0:5])

# check if 'Hello' and 'Nikolay' are in the string
if 'Hello' in test_string:
    print('it is there')
else:
    print('it is not there')

# check if the string starts with something
string = 'Tatyana is a good girl'
print(string.startswith('tatyana'))  # False
print(string.startswith('Tatyana'))  # True

# join() method is called on set of strings that you want to join with separator
string1 = 'is my love'
string2 = 'tatyana'
total = '*'.join([string2.lower().capitalize(), string1.lower(), '!'])
print(total)

# splitting the string using split method; input is a string, output is a list
print(total.split())
print(total.split('*'))

# for example lets justify 'hello' to the right into a string of 25 characters
print('Hello'.rjust(25))
print('Hello'.rjust(25, '^'))
print(' Fuck it! '.center(100, '='))

