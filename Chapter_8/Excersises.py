'''
بسم الله الرحمن الرحیم
محمد سجاد شریفی پناه
'''
import re

# Functions:
def usedAnyOfTheLetters(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False
#1
def check_word(word):
    if 'e' not in word:
        return False
    
    if word[2] == 'e' or word[4] == 'e':
        return False
    
    if usedAnyOfTheLetters(word, 'spadclrk'):
        return False
    
    return True

#2
def check_word2(word):
    if not check_word(word):
        return False
    
    if word[3] == 'e':
        return False
    
    if word[4] != 'm':
        return False
    
    return True

#3
def clean_file(input_file, output_file):
    reader = open(input_file, encoding="utf-8")
    writer = open(output_file, 'w', encoding= "utf-8")

    for line in reader:
        if line.startswith('*** '):
            break

    for line in reader:
        if line.startswith('*** '):
            break
        writer.write(line)
        
    reader.close()
    writer.close()

#4
def count_matches(pattern):
    count = 0
    for line in open('Context_cleaned.txt', encoding="utf-8"):
        result = re.search(pattern, line)
        if result != None:
            count += 1
            print(line.strip())
    return count

# Use Of Functions:

for line in open('Practices\Chapter_8\words.txt'):
    word = line.strip()
    if len(word) == 5 and check_word(word):
        print(word)

for line in open('Practices\Chapter_8\words.txt'):
    word = line.strip()
    if len(word) == 5 and check_word2(word):
        print(word)
        
clean_file('Practices\Chapter_8\Context.txt', 'Context_cleaned.txt')

pattern = r'\b(pale|pales|paled|paleness|pallor)\b'
count_matches(pattern)