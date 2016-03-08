#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# This py file is describing how you can work with clipboard in python
# You can use pyperclip to copy and paste stuff into the clipboard
# If something was already copied into the clipboard, pyperclip.paste() will return that stuff
import pyperclip

pyperclip.copy('Hello')
print(pyperclip.paste())
