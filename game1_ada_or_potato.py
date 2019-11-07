import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"
GAME_SPEED = 1
TIMER_MAXIMUM = 100


class AdaImage(arcade.Sprite):
    timer: int

    def __init__(self):
        super().__init__("images/ada.png")
        self.timer = 0
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0

    def disappear(self):
        if self.timer % 4 == 0:
            self.alpha = 255
        else:
            self.alpha = 0

    def update(self):
        self.update_timer()
        self.disappear()


class PotatoImage(arcade.Sprite):
    timer: int

    def __init__(self):
        super().__init__("images/potato.png")
        self.timer = 0
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.alpha = 0
        self.scale = 0.15

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0

    def disappear(self):
        if self.timer % 4 == 2:
            self.alpha = 255
        else:
            self.alpha = 0

    def update(self):
        self.update_timer()
        self.disappear()


class AdaPotatoGame(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.logo_list = None
        self.set_update_rate(1/3)

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.logo_list = arcade.SpriteList()
        self.logo_list.append(AdaImage())
        self.logo_list.append(PotatoImage())

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.logo_list.draw()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.logo_list.update()


def main():
    window = AdaPotatoGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
