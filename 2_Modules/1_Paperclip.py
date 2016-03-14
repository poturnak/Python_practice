#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# +++++++++ Pyperclip +++++++++
# pyperclip takes a srting as an input
# therefore, if you have a list, you must covert it to the string
# for that purpose you can use join method
# for instance, '\n'.join(list)
# ===================================================================================================

# This py file is describing how you can work with clipboard in python
# You can use pyperclip to copy and paste stuff into the clipboard
# If something was already copied into the clipboard, pyperclip.paste() will return that stuff
import pyperclip

pyperclip.copy('Hello')
print(pyperclip.paste())

