import unittest
from TitleCaseAlgorithmExercise import capitalize_words


class MyTestCase(unittest.TestCase):

    def test_capitalize_words_normal_sentence(self):
        expected = "I Love Solving Problems and It Is Fun"
        actual = capitalize_words("i love solving problems and it is fun")
        self.assertEqual(expected, actual)

    def test_capitalize_words_2_wonky_sentence(self):
        expected = "Why Does a Bird Fly?"
        actual = capitalize_words("wHy DoeS A biRd Fly?")
        self.assertEqual(expected, actual)

    def test_capitalize_words_exception_words_start_and_end(self):
        expected = "A and The"
        actual = capitalize_words("a and the")
        self.assertEqual(expected, actual)

    def test_capitalize_words_one_word(self):
        expected = "Dog"
        actual = capitalize_words("dog")
        self.assertEqual(expected, actual)

    def test_capitalize_words_empty_string(self):
        expected = ""
        actual = capitalize_words("")
        self.assertEqual(expected, actual)


