from enum import Enum

class PowerUpType(Enum):
    SPEED_BOOST = "speed"
    DOUBLE_POINTS = "points"
    INVINCIBILITY = "invincible"

POWER_UP_EFFECTS = {
    PowerUpType.SPEED_BOOST: {
        "color": "yellow",
        "shape": "triangle",
        "duration": 5,
        "symbol": "⚡"
    },
    PowerUpType.DOUBLE_POINTS: {
        "color": "purple",
        "shape": "circle",
        "duration": 7,
        "symbol": "×2"
    },
    PowerUpType.INVINCIBILITY: {
        "color": "blue",
        "shape": "square",
        "duration": 4,
        "symbol": "★"
    }
}

# Game configuration
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BOUNDS = (290, 290)
INITIAL_DELAY = 0.1
COLLISION_DISTANCE = 20