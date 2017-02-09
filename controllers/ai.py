import pypaths.astar as astar


class AIController:
    """Handles AI input"""

    def __init__(self, player):
        """Sets up the models to be manipulated.

        Args:
            player (Player): The player controlled by the AI.
        """
        self.player = player

    def move_towards_target(self, target_x, target_y):
        """ Move towards the given target co-ordinates

        Args:
            target_x (int): The x position of the target
            target_y (int): The y position of the target
        """
        finder = astar.pathfinder()
        path = finder((self.player.x, self.player.y), (target_x, target_y))
        self.player.move(path[1][1][0], path[1][1][1])
