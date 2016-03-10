#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# In the python file we will explore how the regular expressions are used ofr pattern matching
# ===================================================================================================
# +++++++++ Character classes +++++++++
# \d - any numeric digit 0 to 9
# \D - any character that is NOT a numeric digit 0 to 9
# \w - any digit, letter, ot underscore
# \W - any character that is not a letter, digit, or underscore
# \s - any space, tab, or newline
# \S - any character that is not space, tab, or newline
# \b - matches boundary between words
# . - is a wildcard, will match any 1 character, except the newline
# .^$*+?{[]\|() - these characters have special meaning
#                 thus you have to use \ if you want to match them
# \t\n\r - tab, newline, return
# | - called pipe, allows to match either or
#     you can use | in () to choose amongst the groups
# ===================================================================================================
# +++++++++ Repetition +++++++++
# + - 1 or more occurrences of the preceding group
# * - 0 or more occurrences of the preceding group
# ? - 0 or 1 occurrence of the preceding group
# {n} - match the exact number of the preceding group
# {1,}, {3,5}, {,5} - specifying the number of times the preceding group shoudl be matched
# {n}?, +?, *? - performs non-greedy match of the preceding group
# ? will allow optional matching, or non-greedy matching if {} is used
# ===================================================================================================
# +++++++++ Creating classes and groups +++++++++
# [] are used to create the class
# [.] - if '.' is used within the brackets, it means literally '.', not any character
# [asdASD] - look for letters 'a', 's', 'd', 'A', 'S', 'D'
# [a-zA-z0-9] - look for a to a, A to Z, and 0 to 9
# [asd.-] - will match letters and '.' and '-'
# [^a] - by placing the '^' at the beginning, you make a negative class (not 'a')
# () - used to create groups; allows to extract sections of matched text
#      also allows you to add repetition on a set of characters, (\w.)*, r'Bat(wo)?man'
# ===================================================================================================
# +++++++++ Other rules +++++++++
# r'^Hello' - by placing '^' means that match must occur a the beginning of the text
# r'\d$' - indicates that the text must add with the digit; that digit will be returned
# r'^\d+$' - match any strings that consist of digits, begin and end with digit
# (.*) will match anything, except new line
# (.*) and re.DOTALL - to match all characters, including new line, pass DOTALL to compile() method
# re.I - to ignore the case sensitivity, pass 're.I' as a second argument to the compile() method
# re.VERBOSE - pass this to compile() method to ignore whitespaces and comments inside regular expression
#              this will be used to visually create simpler expressions
#              when you do this, you need to use compile(r'''...''', re=VERBOSE)
#  - compile() method only takes one argument as a second parameter
#    to combine I, DOTALL, VERBOSE you use | in the second section
# ===================================================================================================
# +++++++++ Methods +++++++++
# regex.search() - returns only the first match, greedy be default, returns object
# regex.findall() - returns the list of all matches, greedy by default, returns list
#                   if groups () are used with findall() then findall() returns tuples
#                   each tuple will include the match split into groups
# regex.sub(arg1, arg2) - method to substitute strings within strings
#                       - arg1 is string that we need to replace with
#                       - arg2 is string where we need to replace
#                       - arg1 can include \1,\2, etc. that will allow to use groups from searched text
# object.group() - needs to be called to return the exact matched string, not the object
# ===================================================================================================
# +++++++++ Useful regular expressions +++++++++
# python matching is greedy by default, (Ha){3,5} will return 5 Has
# (Ha){3,5)? will return 3 Has
#
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?            # area code
#     (\s|-|\.)?                    # separator
#     \d{3}                         # first 3 digits
#     (\s|-|\.)                     # separator
#     \d{4}                         # last 4 digits
#     (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
#     )''', re.VERBOSE)
# ===================================================================================================
# ===================================================================================================

# 1. Import the re module
# 2. Compile regex expression, use 'r' in order to use raw_input()
# 3. Use search() or findall() method
#    search() returns object, findall() returns list
#    if used search() then use group()
# 4. If groups were used, you can get each group by number (mo.group(1))
import re
phone_regex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
search_result = phone_regex.search('My number is (650)-930-7604')
print('Phone number found ', search_result.group())
print('First group ', search_result.group(1))
print('Second group ', search_result.group(2))
print('All groups ', search_result.groups())
area_code, number = search_result.groups()
print(area_code)
print(number)

# Here we will try using eiter/or matching
name_regex = re.compile(r'Nick|Tatyana Poturnak')
mo = name_regex.search('Nick and Tatyana Poturnak went to school')
print(mo.group())  # returns Nick only, since returns the first match; use findall() method

# Lest try to use several matches with pipe
regex = re.compile(r'Bat(man|dog|cat)')  # will match either batman, batdog, or batcat
mo1 = regex.search('Batcat went to the store')
print(mo1.group())

# regex matching with optional area code
optional_regex = re.compile(r'(\(\d\d\d\)-)?\d\d\d-\d\d\d\d')
mo2 = optional_regex.search('My phone number is 555-6666')
print(mo2.group())

# trying the findall() method
lastname_regex = re.compile(r'[N,n]ikolay\s[P,p]oturnak|[T,t]atyana[P,p]oturnak')
lastname = lastname_regex.findall('Nikolay Poturnak and Tatyana Poturnak')
print(lastname)

# extract email addresses from the string
email_regex = re.compile(r'[\w.-_]+@[\w.-]+')
string = 'My address is npoturnak@gmail.com and t_poturnak@gmail.com'
mo3 = email_regex.findall(string)
if mo3:
    print('We found emails:')
    for i in mo3:
        print('- ',i)

# matching all including the newline characters
newline = re.compile(r'.*', re.DOTALL)
string = 'Hello.\nHow are you?'
mo4 = newline.search(string)
print(mo4.group())

# using sub() method to replace certain parts within the string
replacement_regex = re.compile(r'Agent \w+', re.I)
replacer = 'Agent Poturnak and agent Gorbach worked on that case'
mo5 = replacement_regex.sub('CENSORED', replacer)
print(mo5)

# here we will use sub() and keep some of the replaced text
replacement_regex = re.compile(r'Agent (\w)\w+', re.I)
replacer = 'Agent Poturnak and agent Gorbach worked on that case'
mo5 = replacement_regex.sub(r'\1*****', replacer)
print(mo5)

