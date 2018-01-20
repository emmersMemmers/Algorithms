"""
Word Score

Requirements:
takes up to 50 characters

takes in a string/sentence and returns a integer score that is the sum of the letter score.

all words and characters score = 0 except:
F = 3
J = 6
X = 12
T = 5
A, I, E, O = 2
"""


def word_score(sentence):
    if not sentence:
        return 0
    score_total = 0
    scores = {"F": 3, "J": 6, "X": 12, "T": 5, "A": 2, "I": 2, "E": 2, "O": 2}
    characters = list(sentence.upper())
    for char in characters:
        if char in scores:
            score_total += scores[char]
    return score_total
