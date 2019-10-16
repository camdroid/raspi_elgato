import os
import utils
from StreamDeck.ImageHelpers import PILHelper


# Folder location of image assets used by this example
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "Assets")


class Key:
    deck = None
    image = None
    font = None
    label_text = None
    index = None
    state = None
    icon = 'blank_green_button.png'
    label = 'Key'
    name = 'emoji'
    font = 'Roboto-Regular.ttf'
    static_key = True

    # TODO Need to split out EmojiKey from Key
    # Key should just be a superclass that defines methods - an interface
    def __init__(self, deck, index=0):
        self.deck = deck
        self.index = index
        key_style = self.get_style(False)
        self.create_image(deck, key_style["icon"], key_style["font"], key_style["label"])
        self.deck.set_key_image(self.get_index(), self.get_image())

    def create_image(self, deck, icon_filename, font_filename, label_text):
        # TODO Move away from using the deck parameter, use self.deck
        if deck is None:
            deck = self.deck
        # Generate the custom key with the requested image and label
        image = utils.image_from_filename(deck, icon_filename)
        image = utils.add_text_to_image(font_filename, self.get_label(), image)
        self.image = PILHelper.to_native_format(deck, image)

    def get_image(self):
        return self.image

    def get_index(self):
        return self.index

    def get_label(self):
        return self.label

    def set_state(self, state):
        self.state = state
        if not self.static_key:
            self.set_state_children()

    def set_state_children(self):
        pass

    def get_state(self):
        return self.state

    # creates a new key image based on the key index, style and current key 
    # state and updates the image on the streamdeck.
    def update_image(self, state):
        # Update the key image based on the new key state
        # determine what icon and label to use on the generated key
        # key_style = get_key_style(self.deck, self.get_index(), state)
        key_style = self.get_style(state)
        self.create_image(self.deck, key_style["icon"], key_style["font"], self.get_label())
    
        # update requested key with the generated image
        self.deck.set_key_image(self.get_index(), self.get_image())

    # Returns styling information for a key based on its state
    def get_style(self, state=None):
        if state:
            self.set_state(state)
        return {
            "name": self.name,
            "icon": os.path.join(ASSETS_PATH, self.icon),
            "font": os.path.join(ASSETS_PATH, self.font),
            "label": self.label
        }

    def callback(self, deck, state):
        self.set_state(state)
        self.update_image(state)
