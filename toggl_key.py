from key import Key
from toggl.TogglPy import Toggl
from secrets import TOGGL_API_KEY

class TogglKey(Key):
    name = 'toggl'
    label = 'Toggl'
    icon = 'toggl.png'
    toggl = None

    def __init__(self, deck, index):
        super().__init__(deck, index)
        self.toggl = Toggl()
        self.toggl.setAPIKey(TOGGL_API_KEY)

    def callback(self, deck, state):
        self.toggl.startTimeEntry('test from Elgato')
