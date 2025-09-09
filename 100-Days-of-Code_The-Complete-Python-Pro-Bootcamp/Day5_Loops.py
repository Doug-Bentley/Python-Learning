student_scores = (180, 124, 165, 173, 189, 169, 146)
# high = 0
# for score in student_scores:
#     if score > high:
#         high = score
# print(f"The highest score in the class is: {high}")

# # Add all numbers from 1 to 100
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# # FizzBuzz
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# Password Generator
import random

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
symbols = ('!', '#', '$', '%', '&', '(', ')', '*', '+')

print("Welcome to the PyPassword Generator!")
letters_count = int(input("how many letters would you  like to include in your password: "))
numbers_count = int(input("how many numbers would you like to include in your password: "))
symbols_count = int(input("how many symbols would you like to include in your password: "))

password_list = []
for char in range(0, letters_count):
    password_list.append(random.choice(letters))
for char in range(0, numbers_count):
    password_list.append(random.choice(numbers))
for char in range(0, symbols_count):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
# print password_list as a string
password = ""
for char in password_list:
    password += char
print(f"\nYour password is: {password}")