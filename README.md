# Python Snake Game

A modern implementation of the classic Snake game using Python's Turtle graphics library, featuring power-ups and enhanced gameplay mechanics.

## Features

- Classic snake gameplay with smooth controls
- Score tracking with high score system
- Multiple power-ups:
  - ⚡ Speed Boost: Temporarily increases snake speed
  - ×2 Double Points: Doubles points earned for a limited time
  - ★ Invincibility: Temporarily prevents death from collisions
- Power-up system with:
  - Random spawning
  - Auto-despawn if not collected
  - Visual indicators
- Responsive controls using WASD keys

## Getting Started

### Clone the Repository

```bash
git clone [https://github.com/yourusername/python-snake-game.git](https://github.com/EfekanSalman/SnakeGame/)
cd python-snake-game
```

### Requirements

- Python 3.x
- Turtle graphics library (included in Python standard library)

### Running the Game

```bash
python main.py
```

## Controls

- W: Move Up
- S: Move Down
- A: Move Left
- D: Move Right

## Power-Up System

The game features three different power-ups that spawn randomly:

| Power-Up | Symbol | Effect | Duration |
|----------|--------|--------|-----------|
| Speed Boost | ⚡ | Increases snake speed | 5 seconds |
| Double Points | ×2 | Doubles score from food | 7 seconds |
| Invincibility | ★ | Prevents death from collisions | 4 seconds |

Power-ups will despawn after 7 seconds if not collected.

## Project Structure

```
├── main.py              # Game entry point
├── game_manager.py      # Main game loop and state management
├── game_objects.py      # Game entity classes (Snake, Food, etc.)
├── power_ups.py         # Power-up implementation
├── power_up_manager.py  # Power-up spawning and effect management
└── constants.py         # Game constants and configurations
```

## Game Mechanics

- Snake grows longer when eating food
- Score increases with each food item collected
- Game ends when snake hits the wall or itself (unless invincible)
- Speed gradually increases as score goes up
- High score is maintained between games
