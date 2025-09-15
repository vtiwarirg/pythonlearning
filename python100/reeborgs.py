print("Welcome to Reeborg's World!")
print("This program will help you navigate Reeborg's world.")
print("You can use the following commands:")
print("1. move() - Move forward one step.")
print("2. turn_left() - Turn left 90 degrees.")
print("3. turn_right() - Turn right 90 degrees.")
print("4. pick_beeper() - Pick up a beeper.")
print("5. put_beeper() - Put down a beeper.")
print("6. at_goal() - Check if at the goal.")
print("7. front_is_clear() - Check if the front is clear.")
print("8. left_is_clear() - Check if the left is clear.")
print("9. right_is_clear() - Check if the right is clear.")
print("10. wall_in_front() - Check if there is a wall in front.")
print("11. wall_on_left() - Check if there is a wall on the left.")
print("12. wall_on_right() - Check if there is a wall on the right.")
print("13. beepers_present() - Check if there are beepers present.")
print("14. no_beepers_present() - Check if there are no beepers present.")
print("15. beeper_count() - Get the number of beepers.")
print("16. turn_around() - Turn around 180 degrees.")

# --- State for simulation ---
position = [0, 0]  # x, y
goal = [2, 2]
direction = 0  # 0: North, 1: East, 2: South, 3: West

def move():
    global position, direction
    print("Moving forward one step.")
    if direction == 0:
        position[1] += 1
    elif direction == 1:
        position[0] += 1
    elif direction == 2:
        position[1] -= 1
    elif direction == 3:
        position[0] -= 1
    print(f"Current position: {position}")

def turn_left():
    global direction
    print("Turning left 90 degrees.")
    direction = (direction - 1) % 4

def turn_right():
    global direction
    print("Turning right 90 degrees.")
    direction = (direction + 1) % 4

def pick_beeper():
    print("Picking up a beeper.")

def put_beeper():
    print("Putting down a beeper.")

def at_goal():
    print("Checking if at the goal.")
    return position == goal

def front_is_clear():
    print("Checking if the front is clear.")
    # For simplicity, always True
    return True

def left_is_clear():
    print("Checking if the left is clear.")
    return True

def right_is_clear():
    print("Checking if the right is clear.")
    return True

def wall_in_front():
    print("Checking if there is a wall in front.")
    return False

def wall_on_left():
    print("Checking if there is a wall on the left.")
    return False

def wall_on_right():
    print("Checking if there is a wall on the right.")
    return False

def beepers_present():
    print("Checking if there are beepers present.")
    return False

def no_beepers_present():
    print("Checking if there are no beepers present.")
    return True

def beeper_count():
    print("Getting the number of beepers.")
    return 0

def turn_around():
    print("Turning around 180 degrees.")
    turn_left()
    turn_left()

def main():
    print("Starting Reeborg's World navigation.")
    steps = 0
    while not at_goal() and steps < 20:
        if front_is_clear():
            move()
        elif left_is_clear():
            turn_left()
            move()
        elif right_is_clear():
            turn_right()
            move()
        else:
            turn_around()
        steps += 1
    if at_goal():
        print("Reached the goal!")
    else:
        print("Could not reach the goal in 20 steps.")

main()
# This code is a simulation of Reeborg's World navigation.