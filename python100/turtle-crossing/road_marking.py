from turtle import Turtle

class RoadMarking(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.draw_3d_road_markings()
    
    def draw_3d_road_markings(self):
        """Draw 3D-looking road lane markings with shadow effects"""
        
        # Draw center line with 3D effect
        # Shadow layer
        self.color("dark gray")
        self.goto(-298, -2)
        self.setheading(0)
        self.pendown()
        self.pensize(5)
        
        for _ in range(12):
            self.forward(25)
            self.penup()
            self.forward(25)
            self.pendown()
        
        # Main center line
        self.penup()
        self.color("white")
        self.goto(-300, 0)
        self.setheading(0)
        self.pendown()
        self.pensize(3)
        
        for _ in range(12):
            self.forward(25)
            self.penup()
            self.forward(25)
            self.pendown()
        
        self.penup()
        
        # Draw 3D finish line at top
        # Shadow
        self.goto(-298, 278)
        self.color("dark orange")
        self.pensize(7)
        self.pendown()
        self.forward(600)
        
        # Main finish line
        self.penup()
        self.goto(-300, 280)
        self.color("yellow")
        self.pensize(5)
        self.pendown()
        self.forward(600)
        
        # Draw 3D starting line at bottom
        # Shadow
        self.penup()
        self.goto(-298, -282)
        self.color("dark green")
        self.pensize(7)
        self.pendown()
        self.forward(600)
        
        # Main starting line
        self.penup()
        self.goto(-300, -280)
        self.color("lime green")
        self.pensize(5)
        self.pendown()
        self.forward(600)
        
        self.penup()
        self.hideturtle()