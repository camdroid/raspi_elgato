#!/usr/bin/env python3

#         Python Stream Deck Library
#      Released under the MIT license
#
#   dean [at] fourwalledcubicle [dot] com
#         www.fourwalledcubicle.com
#

# Example script showing basic library usage - updating key images with new
# tiles generated at runtime, and responding to button state change events.

import os
import threading
from PIL import Image, ImageDraw, ImageFont
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper
from key import Key


# Returns styling information for a key based on its position and state.
def get_key_style(deck, key, state):
    _key = Key(deck, key)
    _key.set_state(state)
    return _key.get_style()
    # Last button in the example application is the exit button
    exit_key_index = deck.key_count() - 1

    if key == exit_key_index:
        name = "exit"
        icon = "{}.png".format("Exit")
        font = "Roboto-Regular.ttf"
        label = "Bye" if state else "Exit"
    else:
        name = "emoji"
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Key {}".format(key)

    return {
        "name": name,
        "icon": os.path.join(ASSETS_PATH, icon),
        "font": os.path.join(ASSETS_PATH, font),
        "label": label
    }


# creates a new key image based on the key index, style and current key state
# and updates the image on the streamdeck.
def update_key_image(deck, _key, state):
    # determine what icon and label to use on the generated key
    key_style = get_key_style(deck, _key.get_index(), state)
    _key.render_image(deck, key_style["icon"], key_style["font"], key_style["label"])

    # update requested key with the generated image
    deck.set_key_image(_key.get_index(), _key.get_image())


# Prints key state change information, updates the key image and performs any
# associated actions when a key is pressed.
def key_change_callback(deck, key, state):
    _key = Key(deck, key)
    # Print new key state
    print("Deck {} Key {} = {}".format(deck.id(), _key.get_index(), state), flush=True)
    _key.update_image(state)

    # Check if the key is changing to the pressed state
    if state:
        key_style = _key.get_style(state)
        # key_style = get_key_style(deck, _key.get_index(), state)

        # When an exit button is pressed, close the application
        if key_style["name"] == "exit":
            # Reset deck, clearing all button images
            deck.reset()

            # Close deck handle, terminating internal worker threads
            deck.close()


if __name__ == "__main__":
    streamdecks = DeviceManager().enumerate()

    print("Found {} Stream Deck(s).\n".format(len(streamdecks)))

    for index, deck in enumerate(streamdecks):
        deck.open()
        deck.reset()

        print("Opened '{}' device (serial number: '{}')\n".format(deck.deck_type(), deck.get_serial_number()))

        # Set initial screen brightness to 30%
        deck.set_brightness(30)

        # Set initial key images
        for key_num in range(deck.key_count()):
            _key = Key(deck, key_num)
            update_key_image(deck, _key, False)

        # Register callback function for when a key state changes
        deck.set_key_callback(key_change_callback)

        # Wait until all application threads have terminated (for this example,
        # this is when all deck handles are closed)
        for t in threading.enumerate():
            if t is threading.currentThread():
                continue

            if t.is_alive():
                t.join()
