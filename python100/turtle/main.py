from turtle import Turtle, Screen
timy = Turtle()  # Create a turtle object
print(timy)
timy.shape("turtle")  # Set the shape of the turtle
timy.color("blue")  # Set the color of the turtle
timy.forward(100)  # Move the turtle forward by 100 units
timy.left(90)  # Turn the turtle left by 90 degrees
# Wait for a click to exit (call on Screen object)
# timy.exitonclick()  # Wait for a click to exit


my_screen = Screen()  # Get the screen object associated with the turtle
my_screen.canvheight = 400
my_screen.canvwidth = 400
print(my_screen)
my_screen.exitonclick()  # Wait for a click to exit
print(my_screen)