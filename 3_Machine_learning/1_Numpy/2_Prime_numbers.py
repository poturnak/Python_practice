#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import numpy as np

is_prime = np.ones(100)
is_prime[:2] = 0

for i in range(2, int(len(is_prime) / 2)):
    is_prime[2*i::i] = False

print(np.nonzero(is_prime))