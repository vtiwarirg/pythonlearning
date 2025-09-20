from turtle import Turtle
import random

# Enhanced 3D car colors with shadow combinations
CAR_3D_COLORS = [
    {"main": ("red", "dark red"), "shadow": "maroon", "highlight": "pink"},
    {"main": ("blue", "navy"), "shadow": "midnight blue", "highlight": "light blue"},
    {"main": ("yellow", "orange"), "shadow": "dark orange", "highlight": "light yellow"},
    {"main": ("green", "dark green"), "shadow": "forest green", "highlight": "light green"},
    {"main": ("purple", "indigo"), "shadow": "dark violet", "highlight": "violet"},
    {"main": ("orange", "red"), "shadow": "dark red", "highlight": "light coral"},
    {"main": ("cyan", "blue"), "shadow": "dark blue", "highlight": "light cyan"},
    {"main": ("magenta", "purple"), "shadow": "dark magenta", "highlight": "pink"}
]

class Car3D:
    def __init__(self, x, y, car_type):
        self.car_type = car_type
        self.shadow = None
        self.main_body = None
        self.highlight = None
        self.speed = 0
        self.create_3d_car(x, y)
    
    def create_3d_car(self, x, y):
        """Create a 3D-looking car with shadow, main body, and highlight"""
        # Get car dimensions based on type
        if self.car_type == 1:  # Regular car
            width = random.uniform(1.0, 1.3)
            length = random.uniform(2.0, 2.5)
        elif self.car_type == 2:  # Sports car
            width = random.uniform(0.8, 1.0)
            length = random.uniform(2.2, 2.8)
        elif self.car_type == 3:  # SUV/Truck
            width = random.uniform(1.3, 1.6)
            length = random.uniform(2.5, 3.2)
        else:  # Compact car
            width = random.uniform(0.9, 1.1)
            length = random.uniform(1.8, 2.2)
        
        car_colors = random.choice(CAR_3D_COLORS)
        
        # Create shadow (bottom layer)
        self.shadow = Turtle("square")
        self.shadow.shapesize(stretch_wid=width + 0.1, stretch_len=length + 0.1)
        self.shadow.penup()
        self.shadow.color(car_colors["shadow"])
        self.shadow.goto(x + 2, y - 2)  # Offset for shadow effect
        
        # Create main car body (middle layer)
        self.main_body = Turtle("square")
        self.main_body.shapesize(stretch_wid=width, stretch_len=length)
        self.main_body.penup()
        self.main_body.color(car_colors["main"][0], car_colors["main"][1])
        self.main_body.goto(x, y)
        
        # Create highlight (top layer for 3D effect)
        self.highlight = Turtle("square")
        self.highlight.shapesize(stretch_wid=width * 0.6, stretch_len=length * 0.8)
        self.highlight.penup()
        self.highlight.color(car_colors["highlight"])
        self.highlight.goto(x - 1, y + 1)  # Offset for highlight effect
        
    def move_backward(self, speed):
        """Move all car components backward together"""
        if self.shadow:
            self.shadow.backward(speed)
        if self.main_body:
            self.main_body.backward(speed)
        if self.highlight:
            self.highlight.backward(speed)
    
    def get_position(self):
        """Get the main body position for collision detection"""
        if self.main_body:
            return self.main_body.position()
        return (0, 0)
    
    def distance(self, other_turtle):
        """Calculate distance from main body to another turtle"""
        if self.main_body:
            return self.main_body.distance(other_turtle)
        return float('inf')
    
    def is_off_screen(self):
        """Check if car is off the left side of screen"""
        if self.main_body:
            return self.main_body.xcor() < -350
        return True
    
    def cleanup(self):
        """Remove all car components from screen"""
        if self.shadow:
            self.shadow.hideturtle()
        if self.main_body:
            self.main_body.hideturtle()
        if self.highlight:
            self.highlight.hideturtle()