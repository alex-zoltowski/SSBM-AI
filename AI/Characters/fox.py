import AI.pad
from AI.Characters.character import *

class Fox(Character):

    def __init__(self, pad_path):
        super().__init__(pad_path)

    def logic(self, state):
        if self.compare_state(state, AI.state.ActionState.Wait) or\
                self.compare_state(state, AI.state.ActionState.Landing):
            self.shorthop_nair(1)
        elif self.compare_state(state, AI.state.ActionState.RebirthWait):
            self.tilt_stick(60, 'DOWN')
            self.tilt_stick(3, None)
        elif self.compare_state(state, AI.state.ActionState.DownWaitU) or\
                self.compare_state(state, AI.state.ActionState.DownWaitD):
            self.press_button(0, AI.pad.Button.A)
            self.release_button(1, AI.pad.Button.A)


    """Override methods"""
    def wavedash(self, wait, direction):
        super().wavedash(wait, direction, 4)

    def shorthop_nair(self, wait):
        super().shorthop_nair(wait, 2, 7)


    """Fox only"""
    def double_laser(self, wait):
        self.shorthop(wait)
        self.press_button(3, AI.pad.Button.B)
        self.release_button(1, AI.pad.Button.B)
        self.press_button(3, AI.pad.Button.B)
        self.release_button(1, AI.pad.Button.B)
