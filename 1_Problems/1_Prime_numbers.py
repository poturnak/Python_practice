# Based on the input number, generate the list of all prime numbers that are below the input number

from datetime import datetime
import numpy as np
start_time = datetime.now()

print('Please, provide the limiting number')
limit = int(input())

array_all = list(range(2, limit+1))  # Generate an array of numbers that are lower than specified
print(array_all)
array_primes = []

while len(array_all) > 0:
    counter = 2
    array_primes.append(array_all[0])

    while (array_all[0] * counter) <= array_all[-1]:
        if array_all[0] * counter in array_all:
            array_all.remove(array_all[0] * counter)
        counter += 1
    del array_all[0]

print(array_primes)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))


# in this example we will use the numpy to calculate prime numbers
is_prime = np.ones(100)
is_prime[:2] = 0

for i in range(2, int(len(is_prime) / 2)):
    is_prime[2*i::i] = False

print(np.nonzero(is_prime))
