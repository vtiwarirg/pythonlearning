from turtle import Turtle
import tkinter

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            self.add_segment(position)
        # Set head reference after segments are created
        self.head = self.segments[0]
        # Make the head distinctive
        self.setup_snake_appearance()

    def setup_head(self):
        """Set up the snake head with distinctive appearance"""
        self.head.shape("circle")
        self.head.color("lime green")
        self.head.shapesize(1.1, 1.1)
        
    def setup_snake_appearance(self):
        """Set up the appearance of the entire snake"""
        # Configure head
        self.head.shape("circle")
        self.head.color("lime green")
        self.head.shapesize(1.1, 1.1)
        
        # Configure body segments with alternating colors
        for i, segment in enumerate(self.segments[1:], 1):
            if i % 2 == 1:
                segment.color("forest green")
            else:
                segment.color("dark green")
            segment.shapesize(0.9, 0.9)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move off-screen
        self.segments.clear()
        self.create_snake()
        

    def extend(self):
        # Add new segment with appropriate color
        last_position = self.segments[-1].position()
        new_segment = Turtle("square")
        # Apply alternating color pattern
        segment_count = len(self.segments)
        if segment_count % 2 == 1:
            new_segment.color("forest green")
        else:
            new_segment.color("dark green")
        new_segment.shapesize(0.9, 0.9)
        new_segment.penup()
        new_segment.goto(last_position)
        self.segments.append(new_segment)

    def move(self):
        try:
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)
        except tkinter.TclError:
            # Window was closed, stop movement
            raise tkinter.TclError("Canvas destroyed")

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)