'''
بسم الله الرحمن الرحیم
محمد سجاد شریفی پناه

'''
# functions
def checkYourForbbidenLetterInWord(word:str, letters: str) -> bool:
    for i in word: 
        if i in letters.lower():
            return False
    
    return True

def usedOnlyByLetters(word: str, letters: str) -> bool:
    for i in word.lower(): 
        if i not in letters.lower():
            return False
    return True

def usedAllLetterInWord(word: str, letters: str) -> bool:
    for i in letters.lower(): 
        if i not in word.lower():
            return False
    return True

def checkWord(word, available, required):
    if len(word) < 4:
        return False
    
    if not usedAllLetterInWord(word, required):
        return False
    
    return usedOnlyByLetters(word, available)

def usedAnyOfTheLetters(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

def wordScore(word, availableLetters):

    n = len(word)
    if n == 4:
        return 1
    
    if usedAllLetterInWord(word, availableLetters):
        return n + 7
    else:
        return n

# Use of functions:

print(checkYourForbbidenLetterInWord("mohsenKarimi", "wim"))
print(usedOnlyByLetters("banana", "bna"))
print(usedAllLetterInWord("karimi","kmiar"))
print(checkWord("sajjadSharifi", "sajhadrfi", "s"))

#word score function use: 
available = 'ACDLORT'
required = 'R'
total = 0

file_object = open('Practices\Chapter_7\words.txt')
for line in file_object:
    word = line.strip()    
    if checkWord(word, available, required):
        score = wordScore(word, available)
        total = total + score
        print(word, score)
        
print("Total score", total)


