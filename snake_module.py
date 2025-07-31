import turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
move_d = 20
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for pos in positions:
            self.add_seg(pos)

    def add_seg(self, position):
        t = turtle.Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.turtles.append(t)

    def extend(self):
        self.add_seg(self.turtles[-1].position())

    def move(self):
        for j in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[j - 1].xcor()
            new_y = self.turtles[j - 1].ycor()
            self.turtles[j].goto(new_x, new_y)
        self.head.forward(move_d)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)