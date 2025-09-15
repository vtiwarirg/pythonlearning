print("Welcome to treasure island")
print("Your mission is to find the treasure.")
choice1 = input("Left or Right? ").lower()
if choice1 == "left":
    choice2 = input("Swim or Wait? ").lower()
    if choice2 == "wait":
        choice3 = input("Which door? Red, Blue, or Yellow? ").lower()
        if choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")