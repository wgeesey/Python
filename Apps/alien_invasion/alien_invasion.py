# Contains tools to exit the game when user quits.
import sys

# Contains functionality to make the game
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, create game resources (background settings)
        that this game needs to function properly."""
        pygame.init()
        # Create a clock that ticks once for each pass through main loop.
        # Used to keep frame-rate stable
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        # Creates the display window that will contain graphical elements.
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create instance of ship once screen has been created.
        # self refers to current instance of the game, for access/resources.
        self.ship = Ship(self)
        # Groups to hold the bullets and aliens
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Set background color
        # self.bg_color = (0, 255, 0)

    def run_game(self):
        """Start the main loop for the game (start the game)."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            # To verify bullets are being deleted.
            # print(len(self.bullets))
            self._update_aliens()
            self._update_screen()
            # Make the clock tick (60 = frame rate per sec.)
            self.clock.tick(60)

    # Helper method, annotated by single leading _. To enable the isolation of the
    # event loop allows management of events to be separate from other aspects.
    def _check_events(self):
        """Responds to keyboard and mouse events."""
        # pygame.get allows access to events detected by Pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responds to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responds to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the bullet position and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of old bullets (reached top of screen).
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def _update_aliens(self):
        """Check if at an edge, then update the positions."""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """Create a fleet of aliens."""
        # Create an alien and keep adding until no room left.
        # Spacing between aliens is one alien (height and width).
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 7 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                # If there is 2 x the width of alien or more space, add another one
                current_x += 2 * alien_width

            # Finished a row; reset x value and increment y value.
            current_x = alien_width
            # If there is 2 x the height of alien or more space, add another row
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet down a row and change the direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw the ship
        self.ship.blitme()
        # Draw alien to the screen
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
