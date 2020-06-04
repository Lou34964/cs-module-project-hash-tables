import random

with open("input.txt") as f:
    words = f.read()

characters_whitespace = '\n \t \r'.split(" ")

for whitespace in characters_whitespace:
    words = words.replace(whitespace, " ")

words = words.replace("  ", " ")

following_words = {}

start_words = {}
end_words = {}

ending_punctuation = [".", "?", "!"]

words_array = words.split(" ")

for word_id in range(len(words_array)):

    word = words_array[word_id]

    if word_id == len(words_array) - 2:
        break

    if word_id + 1 < len(words_array):

        next_word = words_array[word_id + 1]

        if word not in following_words:
            following_words[word] = []

        following_words[word].append(next_word)

        is_start_word = (word[0].isalpha() and word[0] == word[0].upper()) or (len(word) > 1 and word[0] == '"' and word[1].isalpha() and word[1] == word[1].upper())

        if is_start_word and word not in start_words:
            start_words[word] = 1

        is_end_word = (word[-1] in ending_punctuation) or (len(word) > 1 and word[-1] == '"' and word[-2:-1] in ending_punctuation)

        if is_end_word and word not in end_words:
            end_words[word] = 1


start_words_array = list(start_words)

for sentence_id in range(5):

    need_closing_double_quote = False

    next_word = random.choice(start_words_array)
    sentence = next_word
        
    if next_word[0] == '"' and next_word[-1] != '"':
        need_closing_double_quote = True

    while True:

        if next_word in end_words and not need_closing_double_quote:
            break

        next_word = random.choice(following_words[next_word])
                
        if need_closing_double_quote:
            
            if next_word[0] == '"':
                continue

            elif next_word[-1] == '"':
                need_closing_double_quote = False
         
        else:

            if next_word[-1] == '"':
                continue

            elif next_word[0] == '"' and next_word[-1] != '"':
                need_closing_double_quote = True

        sentence += " " + next_word

    print(sentence, "\n")