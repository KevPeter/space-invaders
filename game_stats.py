import pygame

class GameStats:
    """Tracks game statistics """

    def __init__(self, ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """ initializes statistics that can change"""
        self.ships_left = self.settings.ship_limit
