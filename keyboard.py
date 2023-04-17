import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.radius = 20

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, arcade.color.BLUE)

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y += self.speed

    def move_down(self):
        self.y -= self.speed


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player = Player(100, 100)
        self.key_map = {
            arcade.key.LEFT: self.player.move_left,
            arcade.key.RIGHT: self.player.move_right,
            arcade.key.UP: self.player.move_up,
            arcade.key.DOWN: self.player.move_down
        }

    def on_key_press(self, key, modifiers):
        if key in self.key_map:
            self.key_map[key]()

    def on_key_release(self, key, modifiers):
        if key in self.key_map:
            self.key_map[key + 1]()

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def update(self, delta_time):
        pass

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game")
    arcade.run()

if __name__ == "__main__":
    main()
