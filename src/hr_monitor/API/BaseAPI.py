from src.hr_monitor.Utils.dir import curr_dir


def write_bpm_file(string='None'):
    with open(f"{curr_dir(__file__='main.py')}\\BPM.Nozzle", 'w+') as bpm_file:
        bpm_file.write(string)
