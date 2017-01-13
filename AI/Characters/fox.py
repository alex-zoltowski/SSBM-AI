import AI.pad
import AI.state
from AI.Characters.character import *

class Fox(Character):

    def __init__(self, pad_path):
        super().__init__(pad_path)

    def logic(self):
        if AI.state.is_spawning(self.state.players[2].action_state):
            self.tilt_stick(60, 'DOWN')
            self.tilt_stick(3, None)
        elif AI.state.can_move(self.state.players[2].action_state):
            self.shorthop_nair(1)
        elif AI.state.can_getupattack(self.state.players[0].action_state):
            self.press_button(0, AI.pad.Button.A)
            self.release_button(1, AI.pad.Button.A)

        elif AI.state.can_move(self.state.players[2].action_state) and\
                AI.state.is_dying(self.state.players[0].action_state):
            self.double_laser(1)


    '''Override methods'''
    def wavedash(self, wait, direction):
        super().wavedash(wait, direction, 4)

    def shorthop_nair(self, wait):
        super().shorthop_nair(wait, 2, 7)


    '''Fox only'''
    def double_laser(self, wait):
        self.shorthop(wait)
        self.press_button(3, AI.pad.Button.B)
        self.release_button(1, AI.pad.Button.B)
        self.press_button(3, AI.pad.Button.B)
        self.release_button(1, AI.pad.Button.B)
