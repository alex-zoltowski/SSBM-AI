import p3.pad
from time import sleep

class Fox:
    def __init__(self):
        self.action_list = []
        self.last_action = 0

    def advance(self, state, pad):
        while self.action_list:
            wait, func, args = self.action_list[0]
            if state.frame - self.last_action < wait:
                return
            else:
                self.action_list.pop(0)
                if func is not None:
                    func(*args)
                self.last_action = state.frame
        else:
            if state.players[2].action_state == p3.state.ActionState.Wait:
                self.dashdance(pad)

    def shinespam(self, pad):
        self.action_list.append((60, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.5, 0.0]))

        self.action_list.append((0, pad.press_button, [p3.pad.Button.B]))
        self.action_list.append((1, pad.release_button, [p3.pad.Button.B]))
        self.action_list.append((0, pad.press_button, [p3.pad.Button.X]))
        self.action_list.append((1, pad.release_button, [p3.pad.Button.X]))
        #self.action_list.append((1, None, []))
        self.action_list.append((0, pad.press_button, [p3.pad.Button.B]))
        self.action_list.append((1, pad.release_button, [p3.pad.Button.B]))

        self.action_list.append((10, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.5, 0.5]))

    def shorthop(self, pad):
        self.action_list.append((0, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.5, 1.0]))
        self.action_list.append((1, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.5, 0.5]))

    def wavedash(self, pad):
        self.action_list.append((0, pad.press_button, [p3.pad.Button.X]))
        self.action_list.append((1, pad.release_button, [p3.pad.Button.X]))
        self.action_list.append((1, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.5, 0.0]))
        self.action_list.append((2, pad.press_trigger, [p3.pad.Trigger.L, 1]))
        self.action_list.append((2, pad.press_trigger, [p3.pad.Trigger.L, 0]))
        self.action_list.append((1, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.5, 0.5]))

    def dashdance(self, pad):
        for _ in range(5):
            self.action_list.append((4, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.0, 0.5]))
            self.action_list.append((4, pad.tilt_stick, [p3.pad.Stick.MAIN, 1.0, 0.5]))

        self.action_list.append((1, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.5, 0.5]))

    def moonwalk(self, pad):
        self.action_list.append((0, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.7, 0.5]))
        self.action_list.append((30, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.0, 0.5]))
        self.action_list.append((2, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.5, 0.2]))
        self.action_list.append((1, pad.tilt_stick, [p3.pad.Stick.MAIN, 1.0, 0.5]))
        self.action_list.append((16, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.5, 0.5]))
        self.action_list.append((60, None, []))

    def firefox(self, pad):
        self.action_list.append((0, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.5, 1.0]))
        self.action_list.append((0, pad.press_button, [p3.pad.Button.B]))
        self.action_list.append((2, pad.release_button, [p3.pad.Button.B]))
        self.action_list.append((4, pad.tilt_stick, [p3.pad.Stick.MAIN, 0.25, 0.75]))
