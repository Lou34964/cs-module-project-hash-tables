from operator import itemgetter


def wordCount(s):

  words = s.lower()

  charsWhitespace = '\n\t\r'.split(" ")

  for Ws in charsWhitespace:
    words = words.replace(Ws, " ")

  IgnoreChars = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

  for char in IgnoreChars:
    words = words.replace(char, " ")
  
  words = words.split(" ")

  cache = {}

  for word in words:

    if word == "":
      continue

    if word in cache:
      cache[word] += 1
    else:
      cache[word] = 1
  
  return cache

def MkHistogram(path):

  with open(path) as file:
    text = file.read()
  
  freq = wordCount(text)

  freqArr = freq.items()
  freqArr = sorted(freqArr, key=itemgetter(1, 0), reverse=True)

  top = len(freqArr[0][0])

  for wordInfo in freqArr:
    if len(wordInfo[0]) > top:
      top = len(wordInfo[0])

  for wordInfo in freqArr:

    wordBuild = wordInfo[0] + (top - len(wordInfo[0])) * ""
    histCount = "#" * wordInfo[1]

    histLine = wordBuild + " " + histCount

    print(histLine)

MkHistogram("robin.txt")