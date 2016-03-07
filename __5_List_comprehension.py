# creating the list with simple line, it is called list comprehension
# what you do with varibale, then what this variable is, and then what is the range for variable
comp_list = [i for i in range(1, 11)]
print(comp_list)

comp_list1 = [i**2 for i in range(1, 11, 2)]
print(comp_list1)

multiple = 5
comp_list3 = [i*multiple for i in range(1, 11)]
print(comp_list3)

# now we are going to look at more complex examples
# 1. For a number that is in the range 0 to 10 define that list that will be comprized of squares form that range

squares = [i**2 for i in range(1, 11)]
print('\nHere is the quares list')
print(squares, '\n')

# 2. For a range of 1 to 10 defien the list that will take 2 and raise it to the power from range

power_2 = [2**i for i in range(1, 11)]
print('Here is the list fo 2 to the power of')
print(power_2, '\n')
# 3. Take all numbers from the list squares that are even and that square root of that number is less than 4

even_squares = [i for i in squares if i % 2 == 0 and i**0.5 > 4]
print(even_squares, '\n')

# 3. The goal is to create the list of Pythagorean triples in the form of a list for the numbers below 100

triples = [(x, y, z) for x in range(1, 30) for y in range(1, 30) for z in range(1, 30) if x**2 + y**2 == z**2]
print(triples)

# 4. In this case we will create the cross list of products
colors = ['red', 'blue', 'pink']
things = ['car', 'paper', 'ball']

colors_things = [(x, y) for x in colors for y in things]
print(colors_things)

# 5. Calculating prime numbers using list comprehension
num_limit = 1000
point = int(num_limit/2)

non_prime = [j for i in range(2, point) for j in range(i * 2, num_limit, i)]
print(non_prime)

print('\n')
prime = [m for m in range (2, num_limit) if m not in non_prime]
print(prime)

# generate all even numbers
even_numbers = [i for i in range(1, 100) if i % 2 == 0]
print(even_numbers)