word_without_vowels = ""

# Prompt the user to enter a word
user_word = input("Enter a word: ")

# Sign it to user word variable
user_word = user_word.upper()


for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter
print(word_without_vowels)