"""
بسم الله الرحمن الرحیم
محمد سجاد شریفی پناه

"""
#functions
def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

def has_duplicates(t):
    d = {}
    for x in t:
        d[x] = True
    return len(d) < len(t)


def find_repeats(counter):
    repeats = []
    for key, count in counter.items():
        if count > 1:
            repeats.append(key)
    return repeats

def add_counters(counter1, counter2):
    result = dict(counter1)
    for letter, count in counter2.items():
        result[letter] = result.get(letter, 0) + count
    return result

def is_interlocking(word):
    first = word[0::2]
    second = word[1::2]
    return first in word_dict and second in word_dict
#--------------------------------------------------------------------------------------

# use of functions
#1
word_list = open('Practices\Chapter_10\words.txt').read().split()
no_repeats = []

for word in word_list:
    if len(word) > 12 and not has_duplicates(word):
        no_repeats.append(word)
        
print("\n",no_repeats, "end :-) \n")

#2
counter1 = value_counts('banana')
counter2 = value_counts([1, 2, 3, 2, 1])
repeats = find_repeats(counter2)
print("\n",repeats, "\n")

#3
add_counters(counter1, counter2)

word_dict = {}
for word in word_list:
    word_dict[word] = 1
    
#4
for word in word_list:
    if len(word) >= 8 and is_interlocking(word):
        first = word[0::2]
        second = word[1::2]
        print(word, first, second)