import tdl


class MainView:
    """Sets up and draws the main game view"""

    def __init__(self, width, height, fps,
                 font='resources/fonts/arial10x10.png'):
        """Sets up the view using tdl.

        Args:
            width (int): The width of the console.
            height (int): The height of the console.
            fps (int): The amount of frames used to render the
                       console per second.
            font (str): The font used for characters on the console.
        """
        self.tdl = tdl
        self.tdl.set_font(font, greyscale=True, altLayout=True)
        self.tdl.set_fps(fps)
        self.console = self.tdl.init(
            width,
            height,
            title="PyRogue",
            fullscreen=False
        )

    def draw_player(self, x, y):
        """Draws the player at the given position.

        Args:
            x (int): the X co-ordinate.
            y (int): the Y co-ordinate.
        """
        self.console.draw_char(x, y, '@', (255, 255, 255), None)
        self.tdl.flush()
        self.console.draw_char(x, y, ' ', bg=None)
