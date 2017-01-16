import AI.pad
import AI.state
from AI.Characters.character import *

class Fox(Character):

    def __init__(self, pad_path):
        super().__init__(pad_path)

    def logic(self):
        super().logic()

        #recovering on yoshi's
        if self.state.players[2].pos_y <= -17.0:
            if AI.state.is_falling(self.state.players[2].action_state):
                self.side_b(1)
        if AI.state.can_move(self.state.players[2].action_state):
    #        self.wavedash(10, 'DOWN_LEFT')
    #        self.wavedash(10, 'DOWN_RIGHT')
            self.double_laser(1)
        elif AI.state.can_getupattack(self.state.players[2].action_state):
            self.press_button(0, AI.pad.Button.A)
            self.release_button(1, AI.pad.Button.A)


    '''Override methods'''
    def style(self, wait):
        self.double_laser(wait)

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
