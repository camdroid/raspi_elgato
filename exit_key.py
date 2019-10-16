from key import Key
import os


class ExitKey(Key):
    name = "exit"
    icon = "{}.png".format("Exit")
    label = "Exit"

    def get_label(self):
        return self.label

    def callback(self, deck, state):
        super().callback(deck, state)
        deck.reset()
        deck.close()
