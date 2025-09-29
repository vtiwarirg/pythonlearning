# TODO: comprehensive list examples
# my_list = [1, 2, 3, 4, 5]
# my_list.append(6)  # Add an element to the end
# print("After append:", my_list)
# new_list = my_list + [7, 8]  # Concatenate lists
# print("After concatenation:", new_list)
# range_list = [num * 2 for num in new_list]  # List comprehension
# print("After list comprehension (doubled):", range_list)
# names = ["Alice", "Bob", "Charlie"]
# # for name in names:
# short_names = [name for name in names if len(name) > 4]  # Filter names shorter than 4 characters
# print("Short names:", short_names)
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# # Convert strings to integers
# numbers = [int(num) for num in list_of_strings]
# print("Converted to integers:", numbers)
# # list of even numbers
# even_numbers = [num for num in numbers if num % 2 == 0]
# print("Even numbers:", even_numbers)
# let I have two files file1.txt and file2.txt each containing a list of numbers in each number in a new line
# I want to read the numbers from both files and create a new file containing the common numbers
# with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
#     numbers1 = {int(line.strip()) for line in file1}
#     print(numbers1)
#     numbers2 = {int(line.strip()) for line in file2}
#     print(numbers2)
#     common_numbers = numbers1.intersection(numbers2)

    # cd d:\pythonlearning\python100\day-26-list; C:/Python313/python.exe main.py
# TODO: Dictionary comprehension examples
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.   
# Try Googling to find out how to convert a sentence into a list of words.  *
# *Do NOT** Create a dictionary directly.
# Try to use Dictionary Comprehension instead of a Loop. 
# To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list_of_words = sentence.split()

# result = {word: len(word) for word in list_of_words}
#TODO: Set comprehension examples
# To convert temp_c into temp_f use this formula: (temp_c * 9/5) + 32 = temp_f
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day:(temp_c* 9/5) +32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

# students_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# for (key, value) in students_dict.items():
#     print(value)

# import pandas as pd
# students_df = pd.DataFrame(students_dict)
# print(students_df)
# # for (index, row) in students_df.items():
# #     print(row)

# for (index, row) in students_df.iterrows():
#     #print(row.score)
#     if row.student == "Angela":
#         print(row.score)



