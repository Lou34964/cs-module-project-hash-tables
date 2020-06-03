import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

charWs = '\n \t \r'.split(" ")

for ws in charWs:
    words = words.replace(ws, " ")



# TODO: analyze which words can follow other words
# Your code here

cache = {}

wordArr = words.split(" ")

for wordId in range(len(wordArr)):
    word = wordArr[wordId]

    if wordId + 1 < len(wordArr):
        nextWord = wordArr[wordId + 1]

        if word not in cache:
            cache[word] = set()
        
        cache[word].add(nextWord)

for w in cache:
    print(w, cache[w])


# TODO: construct 5 random sentences
# Your code here

