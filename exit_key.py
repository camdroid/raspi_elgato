from key import Key
import os


ASSETS_PATH = os.path.join(os.path.dirname(__file__), "Assets")


class ExitKey(Key):
    def get_style(self, state=None):
        if state:
            self.set_state(state)
        name = "exit"
        icon = "{}.png".format("Exit")
        font = "Roboto-Regular.ttf"
        label = "Exit"
        return {
            "name": name,
            "icon": os.path.join(ASSETS_PATH, icon),
            "font": os.path.join(ASSETS_PATH, font),
            "label": label
        }


    def callback(self, deck, state):
        super().callback(deck, state)
        deck.reset()
        deck.close()
