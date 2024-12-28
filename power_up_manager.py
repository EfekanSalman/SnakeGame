import time
from power_ups import PowerUp
from constants import PowerUpType, POWER_UP_EFFECTS


class PowerUpManager:
    def __init__(self, bounds):
        self.power_up = PowerUp(bounds)
        self.spawn_interval = 10  # Spawn every 10 seconds
        self.last_spawn_time = time.time()
        self.active_effects = set()
        self.effect_start_times = {}

    def update(self, snake_head, game_manager):
        current_time = time.time()

        # Check if current power-up should despawn
        if self.power_up.should_despawn():
            self.power_up.despawn()

        # Spawn new power-up
        if not self.power_up.active and current_time - self.last_spawn_time > self.spawn_interval:
            self.power_up.spawn()
            self.last_spawn_time = current_time

        # Check collision with power-up
        if self.power_up.active and snake_head.distance(self.power_up.turtle) < 20:
            self.activate_power_up(game_manager)
            self.power_up.despawn()

        # Update active effects
        self.update_active_effects(game_manager)

    def activate_power_up(self, game_manager):
        effect_type = self.power_up.type
        self.active_effects.add(effect_type)
        self.effect_start_times[effect_type] = time.time()

        if effect_type == PowerUpType.SPEED_BOOST:
            game_manager.delay *= 0.5
        elif effect_type == PowerUpType.DOUBLE_POINTS:
            game_manager.score_multiplier = 2

    def update_active_effects(self, game_manager):
        current_time = time.time()
        effects_to_remove = set()

        for effect in self.active_effects:
            effect_duration = POWER_UP_EFFECTS[effect]["duration"]
            if current_time - self.effect_start_times[effect] > effect_duration:
                effects_to_remove.add(effect)

                # Revert effects
                if effect == PowerUpType.SPEED_BOOST:
                    game_manager.delay *= 2
                elif effect == PowerUpType.DOUBLE_POINTS:
                    game_manager.score_multiplier = 1

        self.active_effects -= effects_to_remove