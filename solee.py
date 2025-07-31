from turtle import Turtle

class Scorecard(Turtle): 
    def __init__(self):            
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)            
        self.update_s()
        self.hideturtle()
            
    def update_s(self):
        self.clear()             
        self.write(f"Score = {self.score}" , align="center", font=("Arial", 24, "normal"))

    def increase_s(self):
        self.score += 1            
        self.update_s()
         
        
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 32, "bold"))