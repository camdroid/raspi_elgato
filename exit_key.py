from key import Key

class ExitKey(Key):
    def callback(self, deck, state):
        super().callback(deck, state)
        deck.reset()
        deck.close()
