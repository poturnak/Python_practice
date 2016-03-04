'''# When you use input method, user interprets everything as a string. In order to make an input as an integer
# you need to use int()

print("please enter your age")
age = int(input())

age += 1
print(age)

# Modulo operator does what mod in Pascal did: divides by number and returns the remainder
# Let's now practice with while loop

prompt = 'Tell me something and I will repeat. To exit, type "quit"'
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)

# Typically there may be many conditions, and if one matches you need to finish the program
# For that purpose you define that 'flag' in the program
# And your while loop is checking the flag

flag = True

prompt = 'Type something, I repeat.\nType "quit" to exit'
print(prompt)

while flag == True:
    message = input()
    if message == 'quit':
        flag = False
    else:
        print(message)

# You can also use break anywhere in the while statement to stop the program from executing
# loop with while True will run forever. That's why you need to use break

while True:
    message = input()
    if message == 'quit':
        break
    print(message)

# When using break in the loop you finish the execution of while
# sometimes you might use continuen, and that will push you to the beginning of the program
# In the example we will print only even numbers

counter = 0

while counter < 10:
    counter += 1
    if counter % 2 == 1:
        continue
    print(counter)


# in this example we will write a program that will be asking about the age and offering a ticket proce

prompt = 'Give me your age and I will tell you the ticket price\n'
print(prompt)

while True:
    age = input()
    if age == 'quit':
        break
    elif int(age) < 3:
        print('ticket s free')
    elif 3 <= int(age) <= 12:
        print('ticket price is $10')
    elif int(age) > 12:
        print('ticket price is $12')

# When you work with lists, and you use for loop, it is hard to modify the list
# When you want to modify the list, you should you while loop

unverified_users = ['alice', 'brian', 'michael', 'daniel']
verified_users = []

while unverified_users:
    current_user = unverified_users.pop()
    print('verifying user ' + current_user)
    verified_users.append(current_user)

print(sorted(verified_users))
print(verified_users)

# In this scenario we will remove all cats from the list

animals = ['dog', 'cat', 'cow', 'sheep', 'cat', 'cat']

while 'cat' in animals:
    animals.remove('cat')

print(animals)'''

# in this example we will create the polling program using dictionary
# we will create dictionary within dictionary

polling_users = {}
user_data = {}

while True:
    print('What is the persons name?')
    name = input()
    print('what is the favority city?')
    user_data['city'] = input()
    print('what is the favority food?')
    user_data['food'] = input()
    polling_users[name] = user_data
    print('Is there another user?')
    choice = input()
    if choice == 'yes':
        continue
    else:
        break
print(polling_users)








