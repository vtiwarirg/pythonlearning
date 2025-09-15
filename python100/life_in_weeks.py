## using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old
## This program calculates how many weeks a person has left to live if they live until 90 years old.
print("Welcome to the Life in Weeks program!")
age = int(input("Enter your current age: "))

def life_in_weeks(age):
    years_left = 90 - age
    weeks_left = years_left * 52
    
    print(f"You have {weeks_left} weeks left .")
    
life_in_weeks(age)
# This function calculates the remaining time in years, months, weeks, and days.