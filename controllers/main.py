import models.player
import controllers.input
import views.main


class GameController:
    """The main controller.

    Contains the main function and the main game loop.
    Initializes other controllers, models, and views
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
        self.player_model = models.player.Player(width // 2, height // 2)
        self.main_view = views.main.MainView(width, height, fps, font)
        self.input_controller = \
            controllers.input.InputController(self.player_model)

    def main(self):
        """The main loop, runs while the game is open."""
        while not self.main_view.tdl.event.is_window_closed():
            self.main_view.draw_player(
                self.player_model.x,
                self.player_model.y
            )
            exit_game = self.input_controller.handle_keys(
                self.main_view.tdl.event.key_wait()
            )
            if exit_game:
                exit()

if __name__ == "__main__":
    game_controller = GameController(80, 50, 20)
    game_controller.main()
