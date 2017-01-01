import os.path
import time

from AI.Characters.fox import *
import AI.memory_watcher
import AI.menu_manager
import AI.pad
import AI.state
import AI.state_manager
import AI.stats


def find_dolphin_dir():
    """Attempts to find the dolphin user directory. None on failure."""
    candidates = ['~/.dolphin-emu', '~/.local/share/.dolphin-emu', '~/Library/Application Support/Dolphin']
    for candidate in candidates:
        path = os.path.expanduser(candidate)
        if os.path.isdir(path):
            return path
    return None

def write_locations(dolphin_dir, locations):
    """Writes out the locations list to the appropriate place under dolphin_dir."""
    path = dolphin_dir + '/MemoryWatcher/Locations.txt'
    with open(path, 'w') as f:
        f.write('\n'.join(locations))

        dolphin_dir = find_dolphin_dir()
        if dolphin_dir is None:
            print('Could not detect dolphin directory.')
            return

def run(fox, state, sm, mw, pad, stats, test_mode):
    mm = AI.menu_manager.MenuManager()
    fox.set_pad(pad)
    while True:
        last_frame = state.frame
        res = next(mw)
        if res is not None:
            sm.handle(*res)
        if state.frame > last_frame:
            stats.add_frames(state.frame - last_frame)
            start = time.time()
            if test_mode is True:
                make_action_test(state, pad, mm, fox)
            else:
                make_action(state, pad, mm, fox)
            stats.add_thinking_time(time.time() - start)

def make_action(state, pad, mm, fox):
    if state.menu == AI.state.Menu.Game:
        fox.advance(state)
    elif state.menu == AI.state.Menu.Characters:
        mm.pick_fox(state, pad)
    elif state.menu == AI.state.Menu.Stages:
        pad.tilt_stick(AI.pad.Stick.C, 0.5, 0.5)
    elif state.menu == AI.state.Menu.PostGame:
        mm.press_start_lots(state, pad)

def make_action_test(state, pad, mm, fox):
    #print(state.menu)
    if state.menu == AI.state.Menu.Game:
        fox.advance(state)
    elif state.menu == AI.state.Menu.PostGame:
        mm.press_start_lots(state, pad)

def main():
    dolphin_dir = find_dolphin_dir()
    if dolphin_dir is None:
        print('Could not find dolphin config dir.')
        return

    #Make false to automate caracter selection and for playing purposes
    test_mode = True

    print("0. Fox")
    print("1. Falcon")

    if input("Select the AI's character: ") is "0":
        character = Fox()

    state = AI.state.State()
    sm = AI.state_manager.StateManager(state, test_mode)
    write_locations(dolphin_dir, sm.locations())
    stats = AI.stats.Stats()

    try:
        print('Start dolphin now. Press ^C to stop AI.')
        pad_path = dolphin_dir + '/Pipes/AI'
        mw_path = dolphin_dir + '/MemoryWatcher/MemoryWatcher'
        with AI.pad.Pad(pad_path) as pad, AI.memory_watcher.MemoryWatcher(mw_path) as mw:
            run(character, state, sm, mw, pad, stats, test_mode)
    except KeyboardInterrupt:
        print('Stopped')
        print(stats)

if __name__ == '__main__':
    main()
