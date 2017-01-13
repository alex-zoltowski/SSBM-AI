import os.path
import time
from AI.Characters import *
import AI.memory_watcher
import AI.menu_manager
import AI.pad
import AI.state
import AI.state_manager
import AI.stats


def find_dolphin_dir():
    '''Attempts to find the dolphin user directory. None on failure.'''
    candidates = ['~/.dolphin-emu', '~/.local/share/.dolphin-emu', '~/Library/Application Support/Dolphin']
    for candidate in candidates:
        path = os.path.expanduser(candidate)
        if os.path.isdir(path):
            return path
    return None

def write_locations(dolphin_dir, locations):
    '''Writes out the locations list to the appropriate place under dolphin_dir.'''
    path = dolphin_dir + '/MemoryWatcher/Locations.txt'
    with open(path, 'w') as f:
        f.write('\n'.join(locations))

        dolphin_dir = find_dolphin_dir()
        if dolphin_dir is None:
            print('Could not detect dolphin directory.')
            return

def run(character, mw, stats):
    mm = AI.menu_manager.MenuManager()
    while True:
        last_frame = character.state.frame
        res = next(mw)
        if res is not None:
            character.sm.handle(*res)
        if character.state.frame > last_frame:
            stats.add_frames(character.state.frame - last_frame)
            start = time.time()
            if character.test_mode is True:
                character.make_action_test(mm)
            else:
                character.make_action(mm)
            stats.add_thinking_time(time.time() - start)


def main():
    dolphin_dir = find_dolphin_dir()
    if dolphin_dir is None:
        print('Could not find dolphin config dir.')
        return

    print('0. Fox')
    print('1. Falcon')

    stats = AI.stats.Stats()

    pad_path = dolphin_dir + '/Pipes/AI'
    mw_path = dolphin_dir + '/MemoryWatcher/MemoryWatcher'

    if input('Select the AIs character: ') is '0':
        character = fox.Fox(pad_path)

    write_locations(dolphin_dir, character.sm.locations())

    try:
        with AI.memory_watcher.MemoryWatcher(mw_path) as mw:
            run(character, mw, stats)
    except KeyboardInterrupt:
        character.pad.stop()
        print('Stopped')
        print(stats)
        

if __name__ == '__main__':
    main()
