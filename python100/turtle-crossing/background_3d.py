from turtle import Turtle

class Background3D(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.create_3d_background()
    
    def create_3d_background(self):
        """Create a 3D-looking background with depth effects"""
        
        # Create side barriers/curbs with 3D effect
        self.create_barrier(-290, "dark gray", "gray")
        self.create_barrier(290, "dark gray", "gray")
        
        # Add some perspective lines for depth
        self.add_perspective_lines()
    
    def create_barrier(self, x_pos, shadow_color, main_color):
        """Create a 3D barrier on the side of the road"""
        # Shadow
        self.goto(x_pos + 2, -302)
        self.color(shadow_color)
        self.pendown()
        self.pensize(8)
        self.setheading(90)
        self.forward(604)
        
        # Main barrier
        self.penup()
        self.goto(x_pos, -300)
        self.color(main_color)
        self.pendown()
        self.pensize(6)
        self.setheading(90)
        self.forward(600)
        self.penup()
    
    def add_perspective_lines(self):
        """Add subtle perspective lines for depth"""
        self.color("silver")
        self.pensize(1)
        
        # Add some diagonal lines for perspective effect
        for i in range(-250, 251, 100):
            self.goto(-300, i)
            self.pendown()
            self.goto(-295, i)
            self.penup()
            
            self.goto(295, i)
            self.pendown()
            self.goto(300, i)
            self.penup()