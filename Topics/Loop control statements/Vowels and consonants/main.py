import string

# Set up
letters = list(input().strip(""))
VOWELS = {"a", "e", "i", "o", "u"}

for letter in letters:
    if letter.isalpha() and (letter in VOWELS):
        print("vowel")
    elif letter.isalpha():
        print("consonant")
    else:
        break

