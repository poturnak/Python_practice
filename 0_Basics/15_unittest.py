import unittest

from Working_files.name_function import get_formatted_name
from Working_files.survey import AnonymousSurvey


class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        self.assertEqual(get_formatted_name('janis', 'joplin'), 'Janis Joplin', "Test for 2 names failed")

    def test_first_middle_last_name(self):
        """Do names like 'Janis Alexis Joplin' work?"""
        self.assertEqual(get_formatted_name('janis', 'joplin', 'alexis'), 'Janis Alexis Joplin', "Test for 3 names failed")

if __name__ == '__main__':
    unittest.main()

# There are multiple ways to use unittest module
#
#  - assertEqual(a, b)        Verify that a == b
#  - assertNotEqual(a, b)     Verify that a != b
#  - assertTrue(x)            Verify that x is True
#  - assertFalse(x)           Verify that x is False
#  - assertIn(item, list)     Verify that item is in list
#  - assertNotIn(item, list)  Verify that item is not in list

# In unittest you can create the objects you need once and then use those objects in all methods
# for that you will use setUp() method

class TestSurvey(unittest.TestCase):
    """Testing survey class"""

    def setUp(self):
        """Create the object for the survey so that we can use it in every method"""
        question = "What language did you first learn to speak?"
        self. my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_responses(self):
        """Test that a single response is stored properly"""

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
