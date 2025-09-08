'''
# type checking
print(type("Hello"))
print(type(123))
print(type(123.45))
print(type(False))

print("Number of letters in your name: " + (str(len(input("Enter your name: ")))))

# Mathematical Operations order of priorities
# PEMDAS->: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

# BMI Calculator - (weight/height)^2
height = 1.85
weight = 85
bmi = weight / height ** 2
print(round(bmi, 2))

# f-Strings
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
print(f"Each person should pay: {round((bill + (bill * tip / 100)) / people, 2)}")
'''

