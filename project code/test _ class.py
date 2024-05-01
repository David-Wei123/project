#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from recognizer import AnswerRecognizer  # Import your AnswerRecognizer class

class TestAnswerRecognizer(unittest.TestCase):
    def setUp(self):
        # Initialize AnswerRecognizer with some test data
        self.answer_recognizer = AnswerRecognizer()

    def test_correct_answer(self):
        # Test a correct answer
        user_answer = "apple"
        correct_answer = "apple"
        result = self.answer_recognizer.check_answer(user_answer, correct_answer)
        self.assertTrue(result)

    def test_incorrect_answer(self):
        # Test an incorrect answer
        user_answer = "apple"
        correct_answer = "banana"
        result = self.answer_recognizer.check_answer(user_answer, correct_answer)
        self.assertFalse(result)

    # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()

