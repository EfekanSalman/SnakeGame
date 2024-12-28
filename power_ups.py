import turtle
import random
import time
from typing import Tuple
from constants import PowerUpType, POWER_UP_EFFECTS


class PowerUp:
    def __init__(self, bounds: Tuple[int, int]):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.hideturtle()
        self.bounds = bounds
        self.active = False
        self.type = None
        self.spawn_time = 0
        self.lifetime = 7  # Power-up will despawn after 7 seconds if not collected
        self.effects = POWER_UP_EFFECTS

    def spawn(self):
        if not self.active:
            self.type = random.choice(list(PowerUpType))
            effect = self.effects[self.type]

            self.turtle.shape(effect["shape"])
            self.turtle.color(effect["color"])

            x = random.randint(-self.bounds[0], self.bounds[0])
            y = random.randint(-self.bounds[1], self.bounds[1])
            self.turtle.goto(x, y)
            self.turtle.showturtle()
            self.active = True
            self.spawn_time = time.time()

    def should_despawn(self) -> bool:
        return self.active and (time.time() - self.spawn_time) > self.lifetime

    def despawn(self):
        self.turtle.hideturtle()
        self.active = False
        self.type = None
        self.spawn_time = 0