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
from exit_key import ExitKey
from toggl_key import TogglKey


key_mapping = None


# Prints key state change information, updates the key image and performs any
# associated actions when a key is pressed.
def key_change_callback(deck, key_num, state):
    key = key_mapping[key_num](deck, key_num)
    key.callback(deck, state)


def create_key_mapping(deck, keys=None):
    global key_mapping
    if keys is None:
        keys = [Key]*(deck.key_count()-2)
        keys.append(TogglKey)
        keys.append(ExitKey)
    key_mapping = keys

def initialize_keys(deck):
    for key_num in range(deck.key_count()):
        _key = key_mapping[key_num](deck, key_num)

if __name__ == "__main__":
    streamdecks = DeviceManager().enumerate()

    print("Found {} Stream Deck(s).\n".format(len(streamdecks)))

    for index, deck in enumerate(streamdecks):
        deck.open()
        deck.reset()
        create_key_mapping(deck)

        print("Opened '{}' device (serial number: '{}')\n".format(deck.deck_type(), deck.get_serial_number()))

        # Set initial screen brightness to 30%
        deck.set_brightness(30)

        # Set initial key images
        initialize_keys(deck)

        # Register callback function for when a key state changes
        deck.set_key_callback(key_change_callback)

        # Wait until all application threads have terminated (for this example,
        # this is when all deck handles are closed)
        for t in threading.enumerate():
            if t is threading.currentThread():
                continue

            if t.is_alive():
                t.join()
