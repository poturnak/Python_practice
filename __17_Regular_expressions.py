#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# In the python file we will explore how the regular expressions are used ofr pattern matching
# ===================================================================================================
# +++++++++ Character classes +++++++++
# \d - any numeric digit 0 to 9
# \D - any character that is NOT a numeric digit 0 to 9
# \w - any digit, letter, ot underscore
# \W - any character that is not a letter, digit, or underscore
# \s - any space, tab, or newline
# \S - ane character that is not space, tab, or newline
# . - is a wildcard, will match any 1 character
# ===================================================================================================
# +++++++++ Repetition +++++++++
# + - 1 or more occurrences to the left
# * - 0 or more occurrences to the left
# ? - 0 or 1 occurrence to the left
# ===================================================================================================
# +++++++++ Creating your own class +++++++++
# [] are used to create the class
# [asdASD] - look for letters 'a', 's', 'd', 'A', 'S', 'D'
# [a-zA-z0-9] - look for a to a, A to Z, and 0 to 9
# [asd.-] - will match letters and '.' and '-'
# [^a] - by placing the '^' at the beginning, you make a negative class (not 'a')
# ===================================================================================================
# +++++++++ Other rules +++++++++
# r'^Hello' - by placing '^' means that match must occur a the beginning of the text
# r'\d$' - indicates that the text must add with the digit; that digit will be returned
# r'^\d+$' - match any strings that consist of digits, begin and end with digit
# (.*) will match anything, except new line
# (.*) and re.DOTALL - to match all characters, including new line, pass DOTALL to compile method
# ===================================================================================================
# +++++++++ Methods +++++++++
# regex.search() -
# regex.findall() -
# ===================================================================================================


# {n} - show to repeat the previous pattern n times; \d{3} means 3 digits
# you can use {3,5} match 3,4,5 times, {,5}, {4,}
# python matching is greedy by default, (Ha){3,5} will return 5 Has
# (Ha){3,5)? will return 3 Has
# () allows you to group sections; (\d\d\d) will be a group
# to search for '(' you need to use special symbol '\(\
# | will help you to match eother or (nick|john) will match either nick or john
# pipe complex matching r'Bat(man|cat|dog) will match batman, batcat, or batdog
# if you need to match pipe character, use '|'
# ()? will allow optional matching; r'Bat(wo)?man' will match batman or batwoman
# ? will allow optional matching, or non-greedy matching if {} is used
# ()* allows for matching preceding group multiple times; r'Bat(wo)*man will match Batman, Batwoman, and Batwowoman
# ()* means match zero or more
# ()+ means match one or more
# search() method will return the first match
# findall() method will return the list of all matches
# =================================================================================================================

# To use regular expressions you need to import the re module
import re

# Path your regular expression to the method compile() in order to define regex object
# Do not forget to use 'r', since it will make the raw input where '\' will be considered as input
phone_regex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')

# search() method will look for the regex in the provided string
# search() method will not retunr the exact results, but rather the obkect will data
# search() will return <_sre.SRE_Match object; span=(13, 25), match='650-930-7604'>
# to return the number we need to use group() method on the search results object
search_result = phone_regex.search('My number is (650)-930-7604')
print('Phone number found ', search_result.group())
print('First group ', search_result.group(1))
print('Second group ', search_result.group(2))
print('All groups ', search_result.groups())
area_code, number = search_result.groups()
print(area_code)
print(number)

# Here will will try using eiter/or matching
name_regex = re.compile(r'Nick|Tatyana Poturnak')
mo = name_regex.search('Nick and Tatyana Poturnak went to school')
print(mo.group())  # returns Nick only, since retu4rns the first match; use findall() method

# Lest try to use several matches with pipe
regex = re.compile(r'Bat(man|dog|cat)')  # will match either batman, batdog, or batcat
mo1 = regex.search('Batman went to the store')√
print(mo1.group())

# regex matching wil optional area code
optional_regex = re.compile(r'(\(\d\d\d\)-)?\d\d\d-\d\d\d\d')
mo2 = optional_regex.search('My phone number is 555-6666')
print(mo2.group())

# trying the findall() method
lastname_regex = re.compile(r'((N|n)ikolay\s(P|p)oturnak)|((T|t)atyana\s(P|p)oturnak)')
lastname = lastname_regex.findall('Nikolay Poturnak and Tatyana Poturnak')
print(lastname)

# extract email addresses from the string
email_regex = re.compile(r'[\w.-_]+@[\w.-]+')
string = 'My address is npoturnak@gmail.com and t_poturnak@gmail.com'
mo3 = email_regex.findall(string)
if mo3:
    print('We found emails:')
    for i in range(len(mo3)):
        print('- ', mo3[i])

# matching all including the newline characters
newline = re.compile(r'(.*)', re.DOTALL)
string = 'Hello.\nHow are you?'
mo4 = newline.search(string)
print(mo4.group())

