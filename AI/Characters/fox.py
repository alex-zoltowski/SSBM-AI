import AI.pad
from AI.Characters.character import *

class Fox(Character):

    def __init__(self):
        super().__init__()

    def _logic(self, state, pad):
        if self.compare_state(state, AI.state.ActionState.Wait):
            self.dashdance(pad)
        elif self.compare_state(state, AI.state.ActionState.RebirthWait):
            self.action_list.append((60, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 0.0]))
            self.action_list.append((3, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 0.5]))
        elif self.compare_state(AI.state.ActionState.DownWaitU) or\
                self.compare_state(AI.state.ActionState.DownWaitD):
            self.action_list.append((0, pad.press_button, [AI.pad.Button.A]))
            self.action_list.append((1, pad.release_button, [AI.pad.Button.A]))


#     def shorthop(self, pad):
#         self.action_list.append((0, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 1.0]))
#         self.action_list.append((1, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 0.5]))
#
#     def wavedash(self, pad):
#         self.action_list.append((0, pad.press_button, [AI.pad.Button.X]))
#         self.action_list.append((1, pad.release_button, [AI.pad.Button.X]))
#         self.action_list.append((1, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 0.0]))
#         self.action_list.append((2, pad.press_trigger, [AI.pad.Trigger.L, 1]))
#         self.action_list.append((2, pad.press_trigger, [AI.pad.Trigger.L, 0]))
#         self.action_list.append((1, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 0.5]))
#
#     def dashdance(self, pad):
#         for _ in range(5):
#             self.action_list.append((4, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.0, 0.5]))
#             self.action_list.append((4, pad.tilt_stick, [AI.pad.Stick.MAIN, 1.0, 0.5]))
#
#         self.action_list.append((1, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 0.5]))
#
#     def moonwalk(self, pad):
#         self.action_list.append((0, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.7, 0.5]))
#         self.action_list.append((30, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.0, 0.5]))
#         self.action_list.append((2, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 0.2]))
#         self.action_list.append((1, pad.tilt_stick, [AI.pad.Stick.MAIN, 1.0, 0.5]))
#         self.action_list.append((16, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 0.5]))
#         self.action_list.append((60, None, []))
#
#     def firefox(self, pad):
#         self.action_list.append((0, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 1.0]))
#         self.action_list.append((0, pad.press_button, [AI.pad.Button.B]))
#         self.action_list.append((2, pad.release_button, [AI.pad.Button.B]))
#         self.action_list.append((4, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.25, 0.75]))
