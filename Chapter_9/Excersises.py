'''
بسم الله الرحمن الرحیم 
محمد سجاد شریفی پناه
'''

import string
from doctest import run_docstring_examples

#Functions
def isAnagram(word1, word2):
    return sorted(word1) == sorted(word2)

def reverseWord(word):
    return ''.join(reversed(word))

def isPalindrome(word):
    return reverseWord(word) == word

def reverse_sentence(input_string):
    words = input_string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words.capitalize()

def totalLength(string_list):
    total = 0
    for string in string_list:
        total += len(string)
    return total

# use of functions
# testing isAnagram function:
def runDoctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

runDoctests(isAnagram)

# use of isAnagram Function
word_list = string.split()
for word in word_list:
    if isAnagram(word, 'takes'):
        print(word)
# use of isPalindrome function     
runDoctests(isPalindrome)
for word in word_list:
    if len(word) >= 7 and isPalindrome(word):
        print(word)
        
runDoctests(reverse_sentence)

# use of totalLength Function
totalLength(word_list)