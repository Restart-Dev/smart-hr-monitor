from src.hr_monitor.API.BaseAPI import *
import random
import time

old_bpm = False


def base_algorithm():
    starting_bpm = str(random.randrange(60, 100))
    write_bpm_file(starting_bpm)
    while True:
        smart_bpm_system(starting_bpm)


def smart_bpm_system(starting_bpm):
    global old_bpm
    new_bpm = random.choice(random_bpm(rnd=3, starting_bpm=starting_bpm))
    if old_bpm:
        new_bpm = random.choice(random_bpm(rnd=4, starting_bpm=old_bpm))
        if new_bpm == old_bpm:
            new_bpm = int(random.choice(random_bpm(rnd=10, starting_bpm=new_bpm)))
    if verify(new_bpm) is not False:
        new_bpm = verify(new_bpm)
    write_bpm_file(str(new_bpm))
    print(f'New BPM: {new_bpm}')
    old_bpm = new_bpm
    time.sleep(1)


def random_bpm(rnd, starting_bpm):
    change = random.randrange(0, rnd)
    plus = int(starting_bpm) + change
    minus = int(starting_bpm) - change
    possibilities = [str(plus), str(minus)]
    return possibilities


def verify(new_bpm):
    if int(new_bpm) < 52:
        new_bpm = int(new_bpm) + 1
        return new_bpm
    if int(new_bpm) > 199:
        new_bpm = int(new_bpm) - 1
        return new_bpm
    return False
