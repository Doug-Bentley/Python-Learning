# HANGMAN
import random

word_list = ["aardvark", "baboon", "camel", "elephant", "giraffe", "hippopotamus",
             "kangaroo", "lion", "monkey", "penguin", "zebra", "tiger", "wolf", "fox", "bear"]
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
print(word_length)
placeholder = []
# for i in range(word_length):
#     placeholder[i] = "_"
print(placeholder)
guess = input("\nGuess a letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        placeholder += letter
    else:
        placeholder += "_"
print(placeholder)