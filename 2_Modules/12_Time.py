#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# ______________________ Time module ______________________
# time.time() - get current time
#             - can be used to calculate how long the program is running
# time.sleep(# of seconds) - will pause the program for a while
# ===================================================================================================

import time

def calculate(length):
    product = 1
    for i in range(1, length):
        product = product * i
    return product

start_time = time.time()
prod = calculate(10)
end_time = time.time()
print('Took {} to calculate'.format(end_time-start_time))
