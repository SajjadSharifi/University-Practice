"""
بسم الله الرحمن الرحیم
محمد سجاد شریفی پناه
"""

#functions------------------------------------------------------------
def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

def shift_word(word, n):
    t = []
    for letter in word:
        index = (letter_map[letter] + n) % 26
        t.append(letters[index])
    return ''.join(t)

def second_element(t):
    return t[1]

def most_frequent_letters(string):
    counter = value_counts(string)
    pairs = sorted(counter.items(), key=second_element, reverse=True)
    for key, value in pairs:
        print(key, value)

def sort_word(word):
    return ''.join(sorted(word))

def value_length(pair):
    key, value = pair
    return len(value)

def word_distance(word1, word2):
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count

def children(word):
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res

#-------------------------------------------------------------------
memo = {}
memo[''] = ['']
def reduce_word(word):
    if word in memo:
        return memo[word]
    res = []
    for child in children(word):
        if reduce_word(child):
            res.append(child)
    memo[word] = res
    return res

def print_trail(word):
    if len(word) == 0:
        return
    print(word, end=' ')
    t = reduce_word(word)
    print_trail(t[0])

def all_reducible():
    """Checks all words in the word_dict; returns a list of reducible ones.
    """
    res = []
    for word in word_dict:
        t = reduce_word(word)
        if len(t) > 0:
            res.append(word)
    return res
#--------------------------------------------------------------------------

# use of functions:
#1
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))

print(shift_word('cheer', 7))

#2
most_frequent_letters('brontosaurus')

#3
string = open('Practices\Chapter_11\pg345.txt', encoding= "utf-8").read()
most_frequent_letters(string)

#4
word_list = open('Practices\Chapter_11\words.txt', encoding= "utf-8").read().split()
anagram_dict = {}
for word in word_list:
    key = sort_word(word)
    if key not in anagram_dict:
        anagram_dict[key] = [word]
    else:
        anagram_dict[key].append(word)

#5
anagram_items = sorted(anagram_dict.items(), key=value_length)
for key, value in anagram_items[-10:]:
    print(value)

#6
longest = 7

for key, value in anagram_items:
    if len(value) > 1:
        word_len = len(value[0])
        if word_len > longest:
            longest = word_len
            print(value)

#7
for anagrams in anagram_dict.values():
    for word1 in anagrams:
        for word2 in anagrams:
            if len(word1) >= 10 and word1 < word2 and word_distance(word1, word2) == 2:
                print(word1, word2)

#8
word_dict = {}
for word in word_list:
    word_dict[word] = 1

for word in ['a', 'i', '']:
    word_dict[word] = 1
    
words = all_reducible()
sorted_words = sorted(words, key=len)

for word in sorted_words[-10:]:
    print_trail(word)
    print('')