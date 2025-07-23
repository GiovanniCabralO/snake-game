from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
FONT_GAME_OVER = ("Courier", 28, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("highscore.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_GAME_OVER)

    def increase_score(self):
        self.score += 1
        self.update_score()
        