print("Welcome to FizzBuzz!")
print("This program will print numbers from 1 to 100, but for multiples of three print 'Fizz' instead of the number and for the multiples of five print 'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz'.")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
        
# yppassword genrator
print("Welcome to the PyPassword generator!")
import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"
print("How many letters would you like in your password?")
nr_letters = int(input("Enter number of letters: "))
print("How many symbols would you like?")
nr_symbols = int(input("Enter number of symbols: "))
print("How many numbers would you like?")
nr_numbers = int(input("Enter number of numbers: "))
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")