from turtle import Turtle
import  time
STARTING_LENGTH = 3
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.body = []
        self.crate_snake()
        self.head = self.body[0]

    def crate_snake(self):
        """Creates an initial snake"""
        for i in range(STARTING_LENGTH):
            self.add_segment((-20 * i, 0))

    def add_segment(self, pos):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.goto(pos)
        self.body.append(new_segment)

    def extend(self):
        new_pos = self.body[-1].pos()
        self.add_segment(new_pos)

    def move(self):
        """Moves the snake 20 paces forward"""
        for i in range(len(self.body) - 1, 0, -1):
            # get position of the previous segment
            prev_pos = self.body[i - 1].pos()
            # move the segment to the position of the previous segment
            self.body[i].setpos(prev_pos)

            # move forward the first segment
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.body:
            seg.goto(1000, 1000)
        self.body.clear()
        time.sleep(1)
        self.crate_snake()
        self.head = self.body[0]

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
