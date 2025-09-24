# def greet():
#     print("Hello, my name is Caesar")
#     print("It's nice to meet you!")
#     print("Please tell me your name.")
#
# greet()


# def life_in_weeks(years, months):
#     print("Let's look to the future and see how many weeks you have left to live.")
#     age_years = years   # int(input("How old are you?\nYears: "))
#     age_months = months # int(input("Months: "))
#     weeks_left = 4680 - ((age_years * 52) + age_months)
#     print(f"You have {weeks_left} weeks left to live")
#
#
# life_in_weeks(20, 0)

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
# greet_with(location = "Italy", name = "Caesar")

# def calculate_love_score(name1, name2):
#  #   word1 = "true"
#  #   word2 = "love"
#     t = 0
#     r = 0
#     u = 0
#     e1 = 0
#     l = 0
#     o = 0
#     v = 0
#     e2 = 0
#     score1 = 0
#     score2 = 0
#     name1_length = len(name1)
#     name2_length = len(name2)
#     for char in (name1  + name2):
#         if char == "t":
#             t += 1
#         elif char == "r":
#             r += 1
#         elif char == "u":
#             u += 1
#         elif char == "e":
#             e1 += 1
#     for char in (name1 + name2):
#         if char == "l":
#             l += 1
#         elif char == "o":
#             o += 1
#         elif char == "v":
#             v += 1
#         elif char == "e":
#             e2 += 1
#
#     print(f"T occurs {t} times")
#     print(f"R occurs {r} times")
#     print(f"U occurs {u} times")
#     print(f"E occurs {e1} times")
#     print(f"L occurs {l} times")
#     print(f"O occurs {o} times")
#     print(f"V occurs {v} times")
#     print(f"E occurs {e2} times")
#     score1 = t + r + u + e1
#     score2 = l + o + v + e2
#     if score2 >= 10:
#         score2 = 0
#         score1 += 1
#     if score1 > 10:
#         score1 = 10
#     print(f"Love Score = {score1}{score2}")
#
# calculate_love_score("doug bentley", "veronica holbrook")

# Caesar Cipher
def caesar(original_text, shift_amount, cipher_direction):
    if cipher_direction == "encode":
# def encrypt(original_text, shift_amount):
        cipher_text = ""
        for char in original_text.lower():
            if char in alphabet:
                position = alphabet.index(char)
                new_position =  (position + shift_amount) % 26
                cipher_text += alphabet[new_position]
            else:
                cipher_text += char
        print(f"The encoded text is {cipher_text}")
    elif cipher_direction == "decode":
# def decrypt(original_text, shift_amount):
        shift_amount = shift_amount % 26
        plain_text = ""
        for char in original_text.lower():
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position - shift_amount
                if new_position < 0:
                    new_position = new_position + 26
                plain_text += alphabet[new_position]
            else:
                plain_text += char
        print(f"The decoded text is {plain_text}")
    else:
        print("You must type 'encode' or 'decode'.")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if direction not in ["encode", "decode"]:
    print("You must type 'encode' or 'decode'.")
    exit()
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))
caesar(text, shift, direction)
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("You must type 'encode' or 'decode'.")