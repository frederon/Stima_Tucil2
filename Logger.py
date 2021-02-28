from dearpygui.core import *
from dearpygui.simple import *


class Logger:
    def __init__(self, parent):
        # parent window where should the logger be printed
        self.parent = parent
        # logs data
        self.logs = []

    def add_log(self, log, color=(255, 255, 255)):
        # add new text in the log, with specific color
        add_text(log, parent=self.parent, color=color)
        self.logs.append(log)

    def delete_log(self, log):
        # delete specific log
        if (log in self.logs):
            delete_item(log)
            self.logs.remove(log)

    def clear_logs(self):
        # clear all logs
        for log in self.logs:
            delete_item(log)
