from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shadow = None
        self.create_3d_turtle()

    def create_3d_turtle(self):
        """Create a 3D-looking turtle with shadow effect"""
        # Create shadow first (behind the turtle)
        self.shadow = Turtle()
        self.shadow.shape("turtle")
        self.shadow.color("gray")
        self.shadow.shapesize(1.6, 1.6)  # Slightly larger for shadow effect
        self.shadow.penup()
        self.shadow.goto(STARTING_POSITION[0] + 3, STARTING_POSITION[1] - 3)  # Offset for shadow
        self.shadow.setheading(90)
        
        # Create main turtle (on top of shadow)
        self.shape("turtle")
        self.color("dark green", "lime green")  # Outline and fill colors
        self.shapesize(1.5, 1.5)  # Make turtle larger and more visible
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        # Move both turtle and shadow together
        self.forward(MOVE_DISTANCE)
        if self.shadow:
            self.shadow.forward(MOVE_DISTANCE)

    def reset_position(self):
        # Reset both turtle and shadow positions
        self.goto(STARTING_POSITION)
        if self.shadow:
            self.shadow.goto(STARTING_POSITION[0] + 3, STARTING_POSITION[1] - 3)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
