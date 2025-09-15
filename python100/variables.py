name = input("What is your name?")
print("Hello, " + name + "!")
print(len(name))
###########################
# create a greeting for program
# Ask the user for the city that they grew up in and store it in a variable
# Ask the user for the name of their favorite pet and store it in a variable
# Combine the name of their city and pet and store it in a new variable called band_name
print("Welcome to the Band Name Generator")
city = input("What city did you grow up in?\n")
pet = input("What is the name of your favorite pet?\n")
band_name = city + " " + pet
print("Your band name could be " + band_name)