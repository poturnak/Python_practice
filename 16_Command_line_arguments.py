#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import sys, argparse

# python sys mode provides access to all command line arguments passed to program (sys.argv)
#  - sys.argv is the list of command arguments
#  - len(sys.argv) is the number of command line arguments
#  - sys.arg[0] is the name of the file, then the following numbers are arguments

# Example:
# print('Here are the arguments passed to the script')
# print(sys.argv)
# print('Here is the name of the script being executed')
# print(sys.argv[0])

# ARGPARSE - module to parse command line arguments
# By default, argparse treats options as strings, unless we define the type

# 1. create a parser
parser = argparse.ArgumentParser(description='Introduction to argparse')

# 1.1 Optional: create mutually exclusive options
group = parser.add_mutually_exclusive_group()

# 2. add arguments to the program
#  - There are optional arguments (defined like -v), and positional/required (defined as v)
#  - Short version is -v, long version is --version
#  - action=store_true defines boolean type, if present it is true, if not it is fault
#  - by default argparse interprets parameters as strings; you can define types: int, float, file
#  - optional arguments are passed as -i filename; required integers are passed without any prepends
#  - arguments are accessible by class.command defined at the beginning (for example, here args.i)
#  - you can define your destination by dest='variable'
#  - you can also define default parameters using default key

parser.add_argument("-i", help='specify the input filename', required=True, dest='input_file')
parser.add_argument("-o", "--output", help="specify output file", default='output.php')
parser.add_argument("square", help='number of iterations', type =int)
parser.add_argument("filename", help='filename to create during execution')
parser.add_argument("-v", "--verbose", help='define the verbosity level', action="store_true")
parser.add_argument("--time", help="times to run", type=int, choices=[1,2,3,4,5])
group.add_argument("--quiet", help='quiet execution mode', action='store_true')
group.add_argument("--loud", help='loud execution mode', action='store_true')


# 3. Parse all arguments into some class. Typically that would be args.
args = parser.parse_args()

# 4. Work with variables. They are accessible through class.
print('\n')
print('These are the parameters'.center(60, '='))
print(args.square, " - this is the square the was passed to the program")
print(args.filename, " - this file will be created during execution")
print(args.input_file, ' - here is the input filename')
print(args.time, ' - number of times to run')
if args.quiet:
    print('Mode is quiet')
if args.loud:
    print('Mode is loud')
print(args.output)
print('\n')
