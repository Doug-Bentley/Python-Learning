# Hello World syntax
print("Hello world!")
print('Hello world!')
print("'Hello world!'")
print('"Hello world!"')

# Recipe
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# Fix the code below 👇
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")

# Chapter 8 Challenges
name = input("what is your name? ")
# print("Hello " + input("what is your name? ") + "!")
print("hello " + name + "!")
print(name + " is " + str(len(name)) + " characters long.")
print(len(input("Input your name to see how many characters are in it: ")))

# Write 3 lines of code to switch the contents of the variables
glass1 = "milk"
glass2 = "juice"

temp = glass1
glass1 = glass2
glass2 = temp
print("glass1 contains: " + glass1 + ", glass2 contains: " + glass2)

# Day 1 Project: Band Name Generator
print("Welcome to the Band Name Generator.")
city = input("What city did you grow up in?")
pet = input("What is your pet's name?")
print("Your band name could be " + name + " " + pet)