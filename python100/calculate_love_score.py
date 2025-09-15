def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    true_count = sum(name1.count(letter) + name2.count(letter) for letter in "true")
    love_count = sum(name1.count(letter) + name2.count(letter) for letter in "love")
    love_score = int(f"{true_count}{love_count}")
    print(f"Your love score is: {love_score}")
    return love_score

name1 = input("Enter the first person's name: ").lower()
name2 = input("Enter the second person's name: ").lower()
calculate_love_score(name1, name2)