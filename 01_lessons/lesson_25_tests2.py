import unittest
import lesson_25_tests

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = lesson_25_tests.cap_test(text)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        text = "monty python"
        result = lesson_25_tests.cap_test(text)
        self.assertEqual(result, "Monty Python")

