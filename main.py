import os
import time
import random

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
os.system('cls')
i = 0
x = False
old_bpm = False
while True:
    if i == 0:
        if x:
            bpm = random.randrange(x - random.randrange(30, 45), x + random.randrange(30, 45))
        else:
            bpm = random.randrange(100, 250)
        i = i + random.randrange(random.randrange(20, 30), random.randrange(30, 40))
    randbpm = random.randrange(bpm - random.randrange(7, 10), bpm + random.randrange(7, 10))
    if randbpm > 999:
        randbpm = random.randrange(bpm - random.randrange(7, 10), bpm + random.randrange(7, 10))
    if old_bpm:
        if randbpm == old_bpm:
            randbpm = random.randrange(bpm - random.randrange(7, 10), bpm + random.randrange(7, 10))
    with open(os.path.join(__location__, 'BPM.nozzle'), 'w+') as bpm_file:
        print(f'New random BPM: {randbpm}')
        bpm_file.write(str(randbpm))
        bpm_file.close()
    x = bpm
    old_bpm = randbpm
    time.sleep(1)
    i = i - 1
