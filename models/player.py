class Player:
    """Stores information on and allows you to manipulate a player"""

    def __init__(self, x, y, char, fg_colour, bg_colour=None):
        """Initializes the player.

        Args:
            x (int): The X co-ordinate.
            y (int): The Y co-ordinate.
            char (str): What the player looks like as a character.
            fg_colour: The colour of the player.
            bg_colour: The background colour of the player.
        """
        self.x = x
        self.y = y
        self.char = char
        self.fg_colour = fg_colour
        self.bg_colour = bg_colour

    def move(self, x, y):
        """Moves the player to the given coordinate.

        Args:
            x (int): The X co-ordinate.
            y (int): The Y co-ordinate.
        """
        self.x = x
        self.y = y

    def move_up(self):
        """Moves the player up."""
        self.y -= 1

    def move_down(self):
        """Moves the player down."""
        self.y += 1

    def move_left(self):
        """Moves the player left."""
        self.x -= 1

    def move_right(self):
        """Moves the player right."""
        self.x += 1
