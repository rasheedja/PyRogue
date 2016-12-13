class Player:
    """Stores information on and allows you to manipulate a player"""

    def __init__(self, x, y):
        """Initializes the player.

        Args:
            x (int): The X co-ordinate.
            y (int): The Y co-ordinate.
        """
        self.x = x
        self.y = y

    def move_player(self, x, y):
        """Moves the player to the given coordinate.

        Args:
            x (int): The X co-ordinate.
            y (int): The Y co-ordinate.
        """
        self.x = x
        self.y = y

    def move_player_up(self):
        """Moves the player up."""
        self.y -= 1

    def move_player_down(self):
        """Moves the player down."""
        self.y += 1

    def move_player_left(self):
        """Moves the player left."""
        self.x -= 1

    def move_player_right(self):
        """Moves the player right."""
        self.x += 1
