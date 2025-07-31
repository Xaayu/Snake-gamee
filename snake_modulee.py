import time
from snake_module import Snake
from foody import Food
from solee import Scorecard
from turtle import Screen

# === Screen setup ===
s = Screen()
s.bgcolor("black")
s.setup(width=1000, height=1000)
s.tracer(0)

# === Game Objects ===
snake_obj = Snake()
food_obj = Food()
score = Scorecard()

# === Keyboard Controls ===
s.listen()
s.onkey(snake_obj.up, "Up")
s.onkey(snake_obj.down, "Down")
s.onkey(snake_obj.left, "Left")
s.onkey(snake_obj.right, "Right")


def control_by_tap(x, y):
    if abs(x) > abs(y): 
        if x > 0:
            snake_obj.right()
        else:
            snake_obj.left()
    else:  
        if y > 0:
            snake_obj.up()
        else:
            snake_obj.down()

s.onclick(control_by_tap)


gameon = True
while gameon:
    s.update()
    time.sleep(0.1)
    snake_obj.move()
    

    
    if snake_obj.head.distance(food_obj) < 20:
        food_obj.spawn_food()
        snake_obj.extend()
        score.increase_s()
        

    
    if (snake_obj.head.xcor() > 390 or snake_obj.head.xcor() < -390 or
        snake_obj.head.ycor() > 390 or snake_obj.head.ycor() < -390):
        score.game_over()
        gameon = False
        

   
    for segment in snake_obj.turtles[1:]:
        if snake_obj.head.distance(segment) < 10:
            gameon = False
            score.game_over()