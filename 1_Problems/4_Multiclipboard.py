#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# In the program we will build the multi-clipboard functionality
# we will create save, list, and retrieve functionality
# also, we will use shelf module for storing the data

import pyperclip, shelve, argparse

parser = argparse.ArgumentParser(description='Multi-clipboard script functionality')
group = parser.add_mutually_exclusive_group()
group.add_argument('-s', "--save", help='save clipboard to shelf')
group.add_argument('-l', "--list", help='list all saved keys from shelf', action='store_true')
group.add_argument('-r', "--retrieve", help='retrieve data to clipboard')
args = parser.parse_args()

shelf_file = shelve.open('mcpbd')

if args.save:
    shelf_file[args.save] = pyperclip.paste()
if args.list:
    print(list(shelf_file.keys()))
if args.retrieve:
    pyperclip.copy(shelf_file[args.retrieve])