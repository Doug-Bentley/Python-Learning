"""
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
    elif age >= 45 & age <= 55:
        bill = 0
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")

print("Welcome to Python Pizza Deliveries!")
size = input("What sixe pizza do you want? S, M, or L ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
print(f"Your final bill is: ${bill}.")
"""

# Treasure Island Game
print("""
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
 """)
print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice1 = input('You\'re at a Y in the road. Would you like to go left(L) or right(R)? ').upper()
if choice1 == "R" or choice1 == "right" or choice1 == "Right":
    print("You fell into a hole. Game Over.")
else:
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Would you like to swim(S) or wait(W) for a boat? ').upper()
    if choice2 == "S" or choice2 == "swim" or choice2 == "Swim":
        print("You get attacked by piranha. Game Over.")
    else:
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red(R), one yellow(Y) and one blue(B). Which colour do you choose? ").upper()
        if choice3 == "R" or choice3 == "red" or choice3 == "Red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "B" or choice3 == "blue" or choice3 == "Blue":
            print("You enter a room of beasts. Game Over.")
        elif choice3 == "Y" or choice3 == "yellow" or choice3 == "Yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")


