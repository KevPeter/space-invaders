import pygame


class Ship:
    """A class to manage ship"""

    def __init__(self, ai_game):
        """Initialize ship and set starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start ship at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for ships horizontal position
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update ship's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw ship's location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)