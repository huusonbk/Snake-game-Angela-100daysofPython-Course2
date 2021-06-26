from turtle import Turtle, Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for turtle_index in range(0,3):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.goto(x=0-turtle_index*20, y=0)
            self.segments.append(new_turtle)

    def add_snake(self):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color('white')
        new_turtle.goto(self.segments[-1].position())
        self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
             self.head.setheading(LEFT)



    def hit_border(self):
        x = abs(self.head.xcor())
        y = abs(self.head.ycor())
        if x > 300 or y > 300:
            return True



    def hit_tail(self):
        for i in range(1, len(self.segments)):
            if self.head.distance(self.segments[i]) < 10:
                print("hit tail")
                return True
