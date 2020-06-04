# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

def decodeCipher(fileLocation):

  knownFrequencies = {}

  knownFrequencies["E"] = 11.53
  knownFrequencies["T"] = 9.75
  knownFrequencies["A"] = 8.46
  knownFrequencies["O"] = 8.08
  knownFrequencies["H"] = 7.71
  knownFrequencies["N"] = 6.73
  knownFrequencies["R"] = 6.29
  knownFrequencies["I"] = 5.84
  knownFrequencies["S"] = 5.56
  knownFrequencies["D"] = 4.74
  knownFrequencies["L"] = 3.92
  knownFrequencies["W"] = 3.08
  knownFrequencies["U"] = 2.59
  knownFrequencies["G"] = 2.48
  knownFrequencies["F"] = 2.42
  knownFrequencies["B"] = 2.19
  knownFrequencies["M"] = 2.18
  knownFrequencies["Y"] = 2.02
  knownFrequencies["C"] = 1.58
  knownFrequencies["P"] = 1.08
  knownFrequencies["K"] = 0.84
  knownFrequencies["V"] = 0.59
  knownFrequencies["Q"] = 0.17
  knownFrequencies["J"] = 0.07
  knownFrequencies["X"] = 0.07
  knownFrequencies["Z"] = 0.03

# create a dictionary to store counts of letters
  letterCounts = {}
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  # create a second dictionary to store frequencies of letters
  letterFrequencies = {}

  for letter in alphabet:
      letterCounts[letter] = 0
      letterFrequencies[letter] = 0
  
  # store the total number of letters to calculate percentages later
  totalLetters = 0

  # store file contents into a variable
  encryptedText = ""

  # open the text file and store data into an array
  with open(fileLocation) as file:
      encryptedText = file.read()
  
  # count letter occurrences
  for character in encryptedText:

      if character in letterCounts:
          letterCounts[character] += 1
          totalLetters += 1

  # calculate letter frequencies
  for letter in alphabet:
      letterFrequencies[letter] = letterCounts[letter] / totalLetters

  # convert letter frequency dictionaries to a list of tuples to sort later
  letterFrequencies = letterFrequencies.items()
  knownFrequencies = knownFrequencies.items()

  # sort letter frequencies and known frequencies by frequency (2nd item in each tuple)
  letterFrequencies = sorted(letterFrequencies, key=lambda letter: letter[1])
  knownFrequencies = sorted(knownFrequencies, key=lambda letter: letter[1])

  # create translation table
  encrptedLettersDecFreq = "".join([letter_data[0] for letter_data in letterFrequencies])
  chacheLettersDecFreq = "".join([letter_data[0] for letter_data in knownFrequencies])

  translation_table = encryptedText.maketrans(encrptedLettersDecFreq, chacheLettersDecFreq)

  decryptedText = encryptedText.translate(translation_table)

  return decryptedText


decryptedText = decodeCipher("ciphertext.txt")

with open("decryptedtext.txt", "w") as file:
    file.write(decryptedText)