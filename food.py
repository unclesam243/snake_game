import random
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        xax = random.randint(-280, 200)
        yax = random.randint(-280, 200)
        self.goto(xax, yax)

    def refresh(self):
        yax = random.randint(-280, 200)
        xax = random.randint(-280, 200)
        self.goto(xax, yax)