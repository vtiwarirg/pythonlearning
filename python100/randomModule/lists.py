import random
state_of_america = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa"
]

state_of_america.append("Kansas")
state_of_america.append("Kentucky")
print(state_of_america)

fruits = [
    "Apple",
    "Banana",
    "Cherry",
    "Date",
    "Elderberry",
    "Fig",
    "Grape",
    "Honeydew",
    "Kiwi",
    "Lemon",
    "Mango",
    "Nectarine",
    "Orange",
    "Papaya",
    "Quince",
]

# print(random.choice(fruits))  # Banana

random_index = random.randint(0, len(fruits) - 1)  # Generates a random index between 0 and the length of the list - 1
print(fruits[random_index])  # This will print a random fruit from the list

