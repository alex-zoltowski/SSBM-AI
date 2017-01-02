import AI.pad

class Character:

    def __init__(self):
        self.action_list = []
        self.last_action = 0
        self.pad = None

    def set_pad(self, pad):
        self.pad = pad

    def logic(self, state):
        pass

    def advance(self, state):
        #if state.frame % 4 == 0:
        #    print(state.players[2].action_state)
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
            self.logic(state)

    def press_button(self, wait, button):
        self.action_list.append((wait, self.pad.press_button, [button]))

    def release_button(self, wait, button):
        self.action_list.append((wait, self.pad.release_button, [button]))

    def tilt_stick(self, wait, direction):
        if direction is 'UP':
            self.action_list.append((wait, self.pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 1.0]))
        elif direction is 'DOWN':
            self.action_list.append((wait, self.pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 0.0]))
        elif direction is 'DOWN_LEFT':
            self.action_list.append((wait, self.pad.tilt_stick, [AI.pad.Stick.MAIN, 0.25, 0.25]))
        elif direction is 'DOWN_RIGHT':
            self.action_list.append((wait, self.pad.tilt_stick, [AI.pad.Stick.MAIN, 0.75, 0.25]))
        elif direction is 'RIGHT':
            self.action_list.append((wait, self.pad.tilt_stick, [AI.pad.Stick.MAIN, 1.0, 0.5]))
        elif direction is 'LEFT':
            self.action_list.append((wait, self.pad.tilt_stick, [AI.pad.Stick.MAIN, 0.0, 0.5]))
        elif direction is None:
            self.action_list.append((wait, self.pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 0.5]))

    def tilt_c_stick(self, wait, direction):
        if direction is 'UP':
            self.action_list.append((wait, self.pad.tilt_stick, [AI.pad.Stick.C, 0.5, 1.0]))
        elif direction is 'DOWN':
            self.action_list.append((wait, self.pad.tilt_stick, [AI.pad.Stick.C, 0.5, 0.0]))
        elif direction is 'RIGHT':
            self.action_list.append((wait, self.pad.tilt_stick, [AI.pad.Stick.C, 1.0, 0.5]))
        elif direction is 'LEFT':
            self.action_list.append((wait, self.pad.tilt_stick, [AI.pad.Stick.C, 0.0, 0.5]))
        elif direction is None:
            self.action_list.append((wait, self.pad.tilt_stick, [AI.pad.Stick.C, 0.5, 0.5]))

    def press_trigger(self, wait, amount):
        self.action_list.append((wait, self.pad.press_trigger, [AI.pad.Trigger.L, amount]))

    def wait(self, wait):
        self.action_list.append((wait, None, []))

    def compare_state(self, state, current_state):
        return state.players[2].action_state is current_state

    def dashdance(self):
        for _ in range(10):
            self.tilt_stick(3, 'LEFT')
            self.tilt_stick(3, 'RIGHT')

        self.tilt_stick(1, None)

    def shorthop(self):
        self.press_button(0, AI.pad.Button.X)
        self.release_button(1, AI.pad.Button.X)

    def wavedash(self, direction):
        self.tilt_stick(15, direction)
        self.shorthop()
        self.press_button(4 , AI.pad.Button.L)
        self.release_button(2, AI.pad.Button.L)
        self.tilt_stick(1, None)

    def shield(self, length):
        self.press_trigger(0, 0.3)
        self.press_trigger(length, 0.0)
