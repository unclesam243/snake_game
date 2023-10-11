from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
class Snake:
    def __init__(self):
        self.segment = []
        self.new_snake()
        self.head = self.segment[0]

    def new_snake(self):

        for position in POSITION:
            self.add_segment(position)

    def reset_snake(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.new_snake()
        self.head = self.segment[0]

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segment.append(new_turtle)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for segments_n in range(len(self.segment)-1 , 0, -1):
            new_x = self.segment[segments_n-1].xcor()
            new_y = self.segment[segments_n - 1].ycor()
            self.segment[segments_n].goto(new_x, new_y)
        self.head.fd(DISTANCE)

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


