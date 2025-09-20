#!/usr/bin/env python3
"""
Test script to verify the improved snake visuals
"""

from turtle import Screen
from snake import Snake
from food import Food
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Improved Snake Game - Visual Test")
screen.tracer(0)

# Create snake and food
snake = Snake()
food = Food()

print("Testing improved snake visuals:")
print("✓ Snake head should be lime green circle with yellow outline")
print("✓ Snake body should have alternating green patterns")
print("✓ Food should be red/orange apple-like appearance")
print("✓ Press any key to close the test window")

# Show the initial state for a few seconds
for i in range(5):
    screen.update()
    time.sleep(1)

# Move the snake a bit to show the movement
for i in range(3):
    snake.move()
    screen.update()
    time.sleep(0.5)

# Extend the snake to show new segments
snake.extend()
snake.extend()

for i in range(3):
    snake.move()
    screen.update()
    time.sleep(0.5)

print("Visual test completed! The snake should now look more realistic.")
screen.exitonclick()