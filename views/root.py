import tdl


class RootView:
    """Sets up the root console view"""

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

    def add_console(self, console, target_x, target_y, target_width,
                    target_height, source_x, source_y):
        """Blits a console to the root console

        Args:
            console (Console): The console to blit to the root
            target_x (int): The root x co-ordinate to blit to
            target_y (int): The root y co-ordinate to blit to
            target_width (int): The width of the new view area
            target_height (int): The height of the new view area
            source_x (int): The source's x co-ordinate to blit from
            source_y (int): The source's y co-ordinate to blit from
        """
        self.console.blit(console, target_x, target_y, target_width,
            target_height, source_x, source_y)
