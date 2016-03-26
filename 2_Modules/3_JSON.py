# json.loads() and json.dumps() - work with json data and write it to variables
# json.load() and json.dump() - worj with json data and write it to files

import json

# json.dump() takes 2 arguments: data to work with and where to store the data

numbers = [1,2,3,4,5]

with open('json.json', 'w') as json_file:
    json.dump(numbers, json_file, indent=4)

# now we are going to read the data back from this json file and we will load it into memory

with open('json.json', 'r') as json_file:
    json_list = json.load(json_file)

print(json_list)

# Let's use json to store user data

user_data = {}
print('Enter your name\n')
username = input()
print('Enter your lastname\n')
lastname = input()

user_data['name'] = username.lower().capitalize()
user_data['lastname'] = lastname.lower().capitalize()

with open('user_data.json', 'w') as fout:
    json.dump(user_data, fout, indent=4)



