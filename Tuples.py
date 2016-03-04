# in terms of python variables that can not change are called IMMUTABLE
# list of IMMUTABLE items in called TUPLE
# TUPLES are defined using parenthesis instead of square bracketa

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#we can not redifine the tuple on a variable basis. We can only do this on a tuple level

dimensions = (500, 750)
for i in dimensions:
    print(i)
