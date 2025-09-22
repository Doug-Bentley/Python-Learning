# HANGMAN
import random

word_list = ["aardvark", "baboon", "camel", "elephant", "giraffe", "hippopotamus",
             "kangaroo", "lion", "monkey", "penguin", "zebra", "tiger", "wolf", "fox", "bear"]

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |     
 /|\  |
 / \  |
      |
=========
''']
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
print(word_length)
word_solve = ""
for position in range(word_length):
    word_solve += "_"
print(word_solve)
count = 0
print(stages[0])
while word_solve != chosen_word and count < 6:
    correct = False
    guess = input("\nGuess a letter: ").lower()
    # Replace letter in placeholder to guessed letter if guessed correctly
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            word_solve = word_solve[:position] + letter + word_solve[position + 1:]
            correct = True
    if not correct:
        count += 1
        if count == 6:
            print(f"You have {6 - count} attempts left.")
        else:
            print("You lose.")
    print(stages[count])
    print(word_solve)
if word_solve == chosen_word:
    print("You win!")
else:
    print(f"The word was {chosen_word}.")







