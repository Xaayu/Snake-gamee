from turtle import Turtle
import random 

class Food (Turtle):
    def __init__(self):
        
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1,1)
        self.color("blue")
        self.speed("slow")
        self.spawn_food()
            
    def spawn_food(self):        
        rand_x=random.randint(-255,255)
        rand_y=random.randint(-255,255)
        self.goto(rand_x,rand_y)