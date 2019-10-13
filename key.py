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

    def __init__(self, deck, index=0):
        self.deck = deck
        self.index = index

    def create_image(self, deck, icon_filename, font_filename, label_text):
        # TODO Move away from using the deck parameter, use self.deck
        if deck is None:
            deck = self.deck
        # Generate the custom key with the requested image and label
        image = utils.image_from_filename(deck, icon_filename)
        image = utils.add_text_to_image(font_filename, label_text, image)
        self.image = PILHelper.to_native_format(deck, image)

    def get_image(self):
        return self.image

    def get_index(self):
        return self.index

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    # creates a new key image based on the key index, style and current key 
    # state and updates the image on the streamdeck.
    def update_image(self, state):
        # Update the key image based on the new key state
        # determine what icon and label to use on the generated key
        # key_style = get_key_style(self.deck, self.get_index(), state)
        key_style = self.get_style(state)
        self.create_image(self.deck, key_style["icon"], key_style["font"], key_style["label"])
    
        # update requested key with the generated image
        self.deck.set_key_image(self.get_index(), self.get_image())

    def get_style(self, state=None):
        if state:
            self.set_state(state)
        # Returns styling information for a key based on its position and state
        # Last button in the example application is the exit button
        exit_key_index = self.deck.key_count() - 1
    
        if self.get_index() == exit_key_index:
            name = "exit"
            icon = "{}.png".format("Exit")
            font = "Roboto-Regular.ttf"
            label = "Exit"
        else:
            name = "emoji"
            icon = "{}.png".format("Pressed" if self.get_state() else "Released")
            font = "Roboto-Regular.ttf"
            label = "Pressed!" if self.get_state() else "Key {}".format(self.get_index())
    
        return {
            "name": name,
            "icon": os.path.join(ASSETS_PATH, icon),
            "font": os.path.join(ASSETS_PATH, font),
            "label": label
        }
