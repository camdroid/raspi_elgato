from key import Key

class EmojiKey(Key):
    name = "emoji"
    icon = "Released.png"
    label = "Key"
    static_key = False

    def get_label(self):
        return "Pressed!" if self.get_state() else f'Key {self.get_index()}'

    def set_state_children(self):
        self.label = "Pressed!" if self.get_state() else "Key {}".format(self.get_index())
        self.icon = "{}.png".format("Pressed" if self.get_state() else "Released")

    def callback(self, deck, state):
        super().callback(deck, state)
