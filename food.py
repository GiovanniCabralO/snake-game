from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        randon_x = randint(-280, 280)
        randon_y = randint(-280, 250)
        self.goto(randon_x, randon_y)
        