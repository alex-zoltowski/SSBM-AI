import AI.pad
from AI.Characters.character import *

class Fox(Character):

    def __init__(self):
        super().__init__()

    def logic(self, state):
        if self.compare_state(state, AI.state.ActionState.Wait) or\
                self.compare_state(state, AI.state.ActionState.Landing):
            self.double_laser()
        elif self.compare_state(state, AI.state.ActionState.RebirthWait):
            self.tilt_stick(60, 'DOWN')
            self.tilt_stick(3, None)
        elif self.compare_state(state, AI.state.ActionState.DownWaitU) or\
                self.compare_state(state, AI.state.ActionState.DownWaitD):
            self.press_button(0, AI.pad.Button.A)
            self.release_button(1, AI.pad.Button.A)

    def double_laser(self):
        self.wait(20)
        self.shorthop()
        self.press_button(3, AI.pad.Button.B)
        self.release_button(1, AI.pad.Button.B)
        self.press_button(3, AI.pad.Button.B)
        self.release_button(1, AI.pad.Button.B)
