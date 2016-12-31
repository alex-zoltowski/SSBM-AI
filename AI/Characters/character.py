import AI.pad
from abc import abstractmethod

class Character:

    def __init__(self):
        self.action_list = []
        self.last_action = 0

    def logic(self, state, pad):
        pass

    def advance(self, state, pad):
        #print(state.players[2].action_state)
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
            self._logic(state, pad)

    def dashdance(self, pad):
        for _ in range(5):
            self.action_list.append((4, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.0, 0.5]))
            self.action_list.append((4, pad.tilt_stick, [AI.pad.Stick.MAIN, 1.0, 0.5]))

        self.action_list.append((1, pad.tilt_stick, [AI.pad.Stick.MAIN, 0.5, 0.5]))

    def compare_state(self, state, current_state):
        return state.players[2].action_state is current_state
