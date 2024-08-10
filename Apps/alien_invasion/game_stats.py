class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initiliaze statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        # Attributes placed here get reset when a new game is started
        # instead of in __init__ since only one instance og game_stats will be
        # made.
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

