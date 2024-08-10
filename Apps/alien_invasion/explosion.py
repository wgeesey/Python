import pygame


class Explosion(pygame.sprite.Sprite):
    """A class to manage explosions."""

    def __init__(self, ai_game, center):
        """Initialize the explosion and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the explosion image and set its rect attribute.
        self.image = pygame.image.load('images/explosion.png')  # Replace with your image path
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Store the explosion's position as a float.
        self.x = float(self.rect.x)

        # Set the timer for the explosion to disappear
        self.timer = 0

    def update(self):
        """Update the explosion's timer."""
        self.timer += 1
        if self.timer > self.settings.explosion_duration:
            self.kill()

    def draw_explosion(self):
        """Draw the explosion on the screen."""
        self.screen.blit(self.image, self.rect)
