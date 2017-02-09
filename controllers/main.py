import models.player
import controllers.input
import controllers.ai
import views.main
import views.root


class GameController:
    """The main controller.

    Contains the main function and the main game loop.
    Initializes other controllers, models, and views.
    """

    def __init__(self, width, height, fps,
                 font='resources/fonts/arial10x10.png'):
        """Set up the models, views, and controllers.

        Args:
            width (int): The width of the console.
            height (int): The height of the console.
            fps (int): The amount of frames used to render the
                       console per second.
            font (str): The font used for characters on the console.
        """
        self.player_user = models.player.Player(width // 2, height // 2,
                                                '@', (255, 255, 255))
        self.player_npc = models.player.Player(width // 3, height // 3,
                                               'g', (0, 255, 0))
        self.players = [self.player_user, self.player_npc]

        self.root_view = views.root.RootView(width, height, fps, font)
        self.main_view = views.main.MainView(width, height)
        self.root_view.add_console(self.main_view.console, 0, 0,
                                   width, height, 0, 0)

        self.input_controller = controllers.input.InputController(self.player_user)
        self.ai_controller = controllers.ai.AIController(self.player_npc)

    def main(self):
        """The main loop, runs while the game is open."""
        while not self.main_view.tdl.event.is_window_closed():
            for player in self.players:
                self.main_view.draw_char(player.x, player.y, player.char,
                                         player.fg_colour, player.bg_colour)

            self.main_view.update()

            for player in self.players:
                self.main_view.clear_char(player.x, player.y)

            self.ai_controller.move_towards_target(self.player_user.x, self.player_user.y)

            exit_game = self.input_controller.handle_keys(
                self.main_view.tdl.event.key_wait())

            if exit_game:
                exit()
