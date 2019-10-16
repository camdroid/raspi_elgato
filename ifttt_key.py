from key import Key
import requests

# I think IFTTT Maker is being deprecated in favor of Platform.
# TODO Will figure out how to use that later


class IFTTTKey(Key):
    name = "IFTTT"
    label = "IFTTT"
    icon = "{}.png".format("IFTTT")

    def get_label(self):
        return self.label

    def callback(self, deck, state):
        url = 'https://maker.ifttt.com/use/{master_key}'
        event = 'button_pressed'
        r = requests.post(url, data={'event': event})
        r2 = requests.post('https://maker.ifttt.com/trigger/button_pressed/with/key/{some_key}')
        print('Hi, IFTTT!')
