from turtle import Turtle
import random


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 8, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 24, "normal"))

    def gain_score(self):
        self.clear()
        self.score += 1
        self.update_score()


