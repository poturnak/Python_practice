class AnonymousSurvey():
    """Collect anonymous answers to survey question"""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """Show survey question"""
        print(self.question)

    def store_response(self, new_response):
        """Store single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """Show all responses that have been given"""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
