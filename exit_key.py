from key import Key

class ExitKey(Key):
    def callback(self, deck, _state):
        deck.reset()
        deck.close()
