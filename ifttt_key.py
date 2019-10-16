from key import Key
import os


ASSETS_PATH = os.path.join(os.path.dirname(__file__), "Assets")


class IFTTTKey(Key):
    name = "IFTTT"
    label = "IFTTT"
    font = "Roboto-Regular.ttf"
    icon = "{}.png".format("IFTTT")

    def get_style(self, state=None):
        if state:
            self.set_state(state)
        return {
            'name': self.name,
            'icon': os.path.join(ASSETS_PATH, self.icon),
            'font': os.path.join(ASSETS_PATH, self.font),
            'label': self.label,
        }

    def callback(self, deck, state):
        print('Hi, IFTTT!')
        pass
