from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FILENAME = "data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open(FILENAME, "r") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILENAME, "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over.", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.write_score()
