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

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(location = "Italy", name = "Caesar")