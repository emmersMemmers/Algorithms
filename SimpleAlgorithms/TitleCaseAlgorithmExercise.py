"""The goal is to implement the title case algorithm

RULES:
1. Take a sentence in as input
2. Upper case the first and last word in the sentence
3. Upper case all words that are not the below:
    "the", "to", 'at", "in", "with", "and", "but", "or", "a"

sample input:
"i love solving problems and it is fun"

sample output:
"I Love Solving Problems and It Is Fun"

sample input:
"wHy DoeS A biRd Fly?"

sample output:
"Why Does a Bird Fly?"

Using the above the goal is:
Take in string input
Lower case the entire string
Split string on spaces to create an array of words
iterate over the words and capitalize the first letter expect where that word is in our except_these_words collection

"""


def capitalize_words(sentence):
    except_collection = ["a", "the", "to", "at", "in", "with", "and", "but", "or"]
    sentence = sentence.lower()
    word_array = sentence.split(" ")
    capitalized_sentence = ""
    counter = 0
    for word in word_array:
        if word in except_collection and counter != 0 and counter != len(word_array) - 1:
            capitalized_sentence = capitalized_sentence + word + " "
            counter += 1
            continue
        capitalized_sentence = capitalized_sentence + word.capitalize() + " "
        counter += 1

    return capitalized_sentence.strip()  # Need to remove the trailing whitespace
