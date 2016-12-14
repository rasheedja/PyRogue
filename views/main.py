import tdl


class MainView:
    """Sets up and draws the main game view"""

    def __init__(self, width, height):
        """Sets up the view using tdl.

        Args:
            width (int): The width of the console.
            height (int): The height of the console.
        """
        self.tdl = tdl
        self.console = self.tdl.init(width, height)

    def draw_char(self, x, y, char, fg_colour, bg_colour=None):
        """Draws the player at the given position.

        Args:
            x (int): the X co-ordinate.
            y (int): the Y co-ordinate.
            char (str): Character to represent player.
            fg_colour (Tuple): Foreground colour given to the the
                              character of the player.
            bg_colour (Tuple): Background colour given to the the
                              character of the player.
        """
        self.console.draw_char(x, y, char, fg_colour, bg_colour)

    def update(self):
        """Updates the view by flushing it."""
        self.tdl.flush()

    def clear_char(self, x, y):
        """Clear the character from the given co-ordinates.

        Args:
            x (int): The X co-ordinate.
            y (int): The Y co-ordinate.
        """
        self.console.draw_char(x, y, ' ', bg=None)
