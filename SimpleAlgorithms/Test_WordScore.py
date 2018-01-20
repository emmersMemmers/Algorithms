import unittest
from WordScore import word_score

class MyWordScoreTests(unittest.TestCase):

    def test_word_score_2_words(self):
        expected = 5
        actual = word_score("F A")
        self.assertEqual(expected, actual)

    def test_word_score_0_words(self):
        expected = 0
        actual = word_score("")
        self.assertEqual(expected, actual)

    def test_word_score_sentence(self):
        expected = 11
        actual = word_score("Tom and Bob ????")
        self.assertEqual(expected, actual)