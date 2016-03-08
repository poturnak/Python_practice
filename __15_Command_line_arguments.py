#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import getopt, sys, argparse

# python getopt module helps to parse command line arguments
# python sys mode provides access to all command line arguments passed to program (sys.argv)

# sys.argv is the list of command arguments
# len(sys.argv) is the number of command line arguments
# sys.arg[0] is the name of the file, then the following numbers are arguments

print('Here are the arguments passed to the script')
print(sys.argv)
print('Here is the name of the script being executed')
print(sys.argv[0])

