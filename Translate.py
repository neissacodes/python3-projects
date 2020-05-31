"""Using json package to  search words' definition"""
import json
"""Using get_close_matches from difflib"""
from difflib import get_close_matches

"""Load the data in an array"""
data = json.load(open("076 data.json"))

"""Function that will ask for words"""
def definition(word):
    """Makes sure the word is lower case because the data is all in lowercase"""
    word = word.lower()
    """Checks if the word is in the data"""
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        """Prompt the user to enter the correct word"""
        yn = input("Did you mean %s instead? Enter Y for yes or N for no: " % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please check your entry."
        else:
            return "We did not understand your entry."
    else:
        return "This word does not exist"

"""Ask for word"""
word = input("Enter a word: ")
"""Print definition"""
output = definition(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
