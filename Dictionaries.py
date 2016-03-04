spouse = {'name': 'tatyana', 'age': '29', 'city': 'NovoSIbirsk'}

print(spouse)
print(spouse['name'].lower().capitalize())
print(spouse['city'].lower().capitalize())

print('\nTatyana actually moved')
spouse['city'] = 'SanFrancisco'
print(spouse['city'].lower().capitalize())

# Let's create a new dictionary to store data about the user

user_dict = {'username': 'partynick', 'password': 'passwd', 'time': 'day', 'agent': 'ie'}

for i, j in user_dict.items():
    print(i + ' ' + j)

# Lest try to loop through the keys now and play with the keys. Keys actually are retrieved as a set

first_last = {
    'tatyana': 'poturnak',
    'nikolay': 'poturnak',
    'elena': 'poturnak',
    'nikita': 'gorbachevskiy',
    'natasha': 'gorbachevskaya',
    }
print('Here are all the names in the dictionary')

for name in first_last.keys():
    print(name.capitalize())

looking = ['Tatyana', 'Nikolay', 'NIKITA']
# Let's look for values associated with these keys only

for i in looking:
    print('Looking for the value associated with', i.lower().capitalize())
    for j in first_last.keys():
        if i.lower() == j.lower():
            print('Username found')
            print('Associated value ', first_last[j].capitalize())

# What is the way to print out the keys in a sorted fashion
for k in sorted(first_last.keys()):
    print(k.lower().capitalize())

# Let's extract key and put them into the list
list_helper = []

for m in first_last.items():
    list_helper.append(m)

print(list_helper[0])

list_helper.sort()
print(sorted(list_helper))

# Let's print values without duplicates

for l in set(first_last.values()):
    print(l)

# In this section we will tkae a look at how we can do the nesting of dictionaries
# we can do several things
# 1. We will do the list of dictionaries. Pretty much we generate the dictionary and then append it to the list

print('\n\n')
aliens = []

for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': '5',
        'speed': 'slow'
    }
    aliens.append(new_alien)

print(aliens)

# in this example I will cahnge the value of color in the first dictionary
for helper in aliens[0:1]:
    helper['color'] = 'blue'

print(aliens)

# In here we are going to take a look at list in dictionary. We have pizza order here

toppings = ['cheese', 'ham', 'greens']

pizza_order = {
    'crust': 'thick',
    'toppings': toppings,
}

print("here is your pizza order:\ncrust - " + pizza_order['crust'])
print('toppings: ')
num = 1
for topping in toppings:
    print(num, '-', topping)
    num += 1

languages = {
    'nikolay': ['pascal', 'javascript', 'python'],
    'tatyana': ['python'],
}

print('\n')
for i, j in languages.items():
    if len(j) == 1:
        print(i.lower().capitalize() + "'s favourite language is:")
        for m in j:
            print('-', m)
    else:
        print(i.lower().capitalize() + "'s favourite languages are:")
        for m in j:
            print('-', m)

# In this example we will create dictionary wihtin the dictionary

user_info = {
    'partynick': {
        'name': 'Nikolay',
        'location': 'Palo Alto',
        'age': '30',
    },
    'tpoturnak': {
        'name': 'Tatyana',
        'location': 'Palo Alto',
        'age': '29',
    }
}

for user_id, metadata in user_info.items():
    print('Here is all the data about username ' + user_id + ':')
    for i, j in metadata.items():
        print(i + ' is ' + j)

# Now it is time for more practice

nikolay = {
    'name': 'Nikolay',
    'location': 'Palo Alto',
    'age': '30',
}

tatyana = {
    'name': 'Tatyana',
    'location': 'Palo Alto',
    'age': '29',
}

us = [nikolay, tatyana]
print('\n')

for i in us:
    print('Here is the data about user: ' + i['name'])
    for j, n in i.items():
        print('\t' + j + ' is ' + n)