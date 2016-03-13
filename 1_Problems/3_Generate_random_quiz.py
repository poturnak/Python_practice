#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import random

list_capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
            'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

letters = ['a', 'b', 'c', 'd']

for quiz in range (1,2):
    file_questions = open('Quiz_capitals_{}.txt'.format(quiz), 'w')
    file_answers = open('Quiz_answers_{}.txt'.format(quiz), 'w')
    file_questions.write('\t\t\tState Capitals Quiz (Form {})\n\n'.format(quiz))
    states = list(list_capitals.keys())
    capitals = list(list_capitals.values())
    random.shuffle(states)
    random.shuffle(capitals)
    for num in range(1, 51):
        counter = 3
        random_options = []
        state = states.pop()
        file_questions.write('{}. What is the capital of {}?\n'.format(num, state))
        random_options.append(list_capitals[state])
        while counter != 0:
            fake = random.sample(capitals,1)
            if (fake[0] != list_capitals[state]) and (fake[0] not in random_options):
                random_options.append(fake[0])
                counter -= 1
                fake = []
        random.shuffle(random_options)
        for i in range(4):
            file_questions.write('{}. {}\n'.format(letters[i], random_options[i]))
        file_questions.write('\n')
        file_answers.write('{}. {}\n'.format(num, letters[random_options.index(list_capitals[state])]))
    file_answers.close()
    file_questions.close()










