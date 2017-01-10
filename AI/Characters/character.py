import AI.pad

class Character:

    def __init__(self, pad_path):
        self.action_list = []
        self.last_action = 0
        self.pad = AI.pad.Pad(pad_path)

    def get_pad(self):
        return self.pad

    #stops pad fifo, resets controller inputs to neutral
    def stop(self):
        self.pad.stop()

    #implemented by each character to decide what to do
    def logic(self, state):
        pass

    #compare AI's current state to test_state
    def compare_state(self, state, test_state):
        return state.players[2].action_state is test_state

    #executes button presses defined in action_list, runs logic once list is empty
    def advance(self, state):
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


    """Methods simulate controller input; appends necessary tuple to action_list"""
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


    """Methods execute actions shared among all characters"""
    def shield(self, wait, length):
        self.press_trigger(wait, 0.3)
        self.press_trigger(length, 0.0)

    def dashdance(self, wait, length):
        self.wait(wait)
        for _ in range(length):
            self.tilt_stick(4, 'LEFT')
            self.tilt_stick(4, 'RIGHT')

        self.tilt_stick(1, None)

    def shorthop(self, wait):
        self.press_button(wait, AI.pad.Button.X)
        self.release_button(1, AI.pad.Button.X)


    """Methods execute similar actions that is dependent on character frame data
       Needs to be overridden for each character"""
    def wavedash(self, wait, direction, can_airdodge):
        self.tilt_stick(wait, direction)
        self.shorthop(1)
        self.press_button(can_airdodge, AI.pad.Button.L)
        self.release_button(2, AI.pad.Button.L)
        self.tilt_stick(1, None)

    def shorthop_nair(self, wait, can_attack, can_ff):
        self.shorthop(wait)
        self.press_button(can_attack, AI.pad.Button.A)
        self.release_button(1, AI.pad.Button.A)
        self.tilt_stick(can_ff, 'DOWN')
        self.tilt_stick(3, None)
        self.press_trigger(2, 0.5)
        self.press_trigger(1, 0.0)
