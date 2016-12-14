class InputController:
    """Handles all user input"""

    def __init__(self, player):
        """Sets up the models to be manipulated.

        Args:
            player (Player): The player controlled by the user input.
        """
        self.player = player

    def handle_keys(self, user_input) -> bool:
        """Manipulates models based on key pressed by user

        Args:
            user_input (KeyDown): tdl object which stores information on
                                  the keys pressed by the user.
        Returns:
            True if the user has entered the 'Exit Game' command
        """
        if user_input.key == 'UP' or user_input.char == 'w':
            self.player.move_up()
        elif user_input.key == 'DOWN' or user_input.char == 's':
            self.player.move_down()
        elif user_input.key == 'LEFT' or user_input.char == 'a':
            self.player.move_left()
        elif user_input.key == 'RIGHT' or user_input.char == 'd':
            self.player.move_right()
        elif user_input.key == 'ESCAPE':
            return True
