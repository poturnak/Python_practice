from survey import AnonymousSurvey

question = "What language did you first learn to speak?\n"
my_survey = AnonymousSurvey(question)

# Show the question and store responses to the question
my_survey.show_question()
print('Enter q at any time to quit')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

# Store survey results
print('Thanks for partici[ating in the survey\n')
my_survey.show_results()
