from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", False, align= 'center', font=("Times New Roman", 12, "normal"))

    def writing(self):
        self.score += 1
        self.update()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()


    '''def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Times New Roman", 14, "normal"))'''
