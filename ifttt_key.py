from key import Key
import os


class IFTTTKey(Key):
    name = "IFTTT"
    label = "IFTTT"
    icon = "{}.png".format("IFTTT")

    def get_label(self):
        return self.label

    def callback(self, deck, state):
        print('Hi, IFTTT!')
        pass
