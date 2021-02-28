from dearpygui.core import *
from dearpygui.simple import *


class Logger:
    def __init__(self, parent):
        self.parent = parent
        self.logs = []

    def add_log(self, log, color=(255, 255, 255)):
        add_text(log, parent=self.parent, color=color)
        self.logs.append(log)

    def delete_log(self, log):
        if (log in self.logs):
            delete_item(log)
            self.logs.remove(log)

    def clear_logs(self):
        for log in self.logs:
            delete_item(log)
