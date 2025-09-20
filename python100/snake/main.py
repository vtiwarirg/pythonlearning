from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
game_speed = 0.5  # Starting speed
while game_is_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        # # Increase speed slightly with each food eaten (optional)
        # if game_speed > 0.05:  # Minimum speed limit
        #     game_speed -= 0.005  # Speed up by reducing sleep time
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Check for collision with tail
    for segment in snake.segments[1:]: # skip the head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            break

screen.exitonclick()