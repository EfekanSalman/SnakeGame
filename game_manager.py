import turtle
from game_objects import SnakeHead, Food, Scoreboard, SnakeBody
from power_up_manager import PowerUpManager
import time

from power_ups import PowerUpType


class GameManager:
    def __init__(self):
        self.setup_screen()
        self.head = SnakeHead()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.body = SnakeBody()
        self.delay = 0.1
        self.is_running = True
        self.bounds = (290, 290)
        self.score_multiplier = 1
        self.power_up_manager = PowerUpManager(self.bounds)
        self.setup_controls()

    def setup_screen(self):
        self.screen = turtle.Screen()
        self.screen.title("Snake Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkeypress(lambda: self.head.set_direction("up"), "w")
        self.screen.onkeypress(lambda: self.head.set_direction("down"), "s")
        self.screen.onkeypress(lambda: self.head.set_direction("left"), "a")
        self.screen.onkeypress(lambda: self.head.set_direction("right"), "d")

    def check_collision_with_food(self):
        if self.head.turtle.distance(self.food.turtle) < 20:
            self.food.random_position(self.bounds)
            self.body.add_segment()
            self.delay -= 0.001
            self.scoreboard.score += 10 * self.score_multiplier
            self.scoreboard.update()

    def check_collision_with_walls(self):
        x, y = self.head.turtle.xcor(), self.head.turtle.ycor()
        if abs(x) > self.bounds[0] or abs(y) > self.bounds[1]:
            if PowerUpType.INVINCIBILITY not in self.power_up_manager.active_effects:
                self.reset_game()

    def check_collision_with_body(self):
        for segment in self.body.segments:
            if segment.distance(self.head.turtle) < 20:
                if PowerUpType.INVINCIBILITY not in self.power_up_manager.active_effects:
                    self.reset_game()

    def reset_game(self):
        self.scoreboard.show_game_over()
        time.sleep(1)
        self.head.turtle.goto(0, 0)
        self.head.direction = "stop"
        self.body.reset()
        self.scoreboard.reset()
        self.delay = 0.1
        self.score_multiplier = 1

    def run(self):
        while self.is_running:
            self.screen.update()
            self.power_up_manager.update(self.head.turtle, self)
            self.check_collision_with_walls()
            self.check_collision_with_food()
            self.check_collision_with_body()
            self.body.move_segments(self.head)
            self.head.move()
            time.sleep(self.delay)

        self.screen.mainloop()