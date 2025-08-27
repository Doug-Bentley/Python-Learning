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

# MODULO
numerator = input("Enter a number to be divided: ")
denominator = input("Enter a number to divide by: ")
if int(numerator) % int(denominator) == 0:
    print(f"The modulo of {numerator} divided by {denominator} is neither even nor odd.)")
elif (int(numerator) % int(denominator)) % 2 == 0:
    print(f"The modulo of {numerator} divided by {denominator} is even.")
else:
    print(f"The modulo of {numerator} divided by {denominator} is odd.")

# BMI Calculator - (weight/height)^2
height = 1.85
weight = 85
bmi = round(weight / height ** 2, 2)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")

# Amusement Ride
height = int(input("Enter your height in cm: "))
if height < 120:
    print("Sorry, you have to be at least 120cm to ride.")
else:
    print("You can ride!")
    age = int(input("Enter your age: "))
    bill = 0
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")
'''

