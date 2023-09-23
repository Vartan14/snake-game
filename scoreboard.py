from turtle import Turtle
ALIGNMENT = "center"
FONT1 = ("Courier", 18, "bold")
FONT2 = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Files/data.txt") as file:
            high = file.read()
        self.high_score = int(high)

        self.color("white")
        self.penup()
        self.hideturtle()



    def show_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT1)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Files/data.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.show_score()

    def start_game(self):
        self.goto(0, 0)
        self.write(arg=f"To start game press Space", align=ALIGNMENT, font=FONT2)

    def increase_score(self):
        self.score += 1
        self.show_score()
