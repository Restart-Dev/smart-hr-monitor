from src.hr_monitor.API.bpm_algorithm import *
from src.hr_monitor.API.BaseAPI import *


class start:

    def __init__(self, option):
        self.option = option

    def all(self):
        possible_choice = {
            "hr_monitor": 1
        }
        if possible_choice[self.option] is 1:
            base_algorithm()
