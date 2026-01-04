""" This module contains constants and functions common to all modules. """

import inspect
import os

SETTINGS_FILE_PATH = "./settings.json"

KEY_LIBRARY = "LIBRARY"
KEY_ARCHIVE = "ARCHIVE"
KEY_GAMES = "GAMES"
KEY_NOT_MODS = "NOT_MODS"
_SETTINGS_FORMAT = {
    KEY_LIBRARY: "",
    KEY_ARCHIVE: "",
    KEY_GAMES: [],
    KEY_NOT_MODS: []
}


def log():
    pass


def get_calling_module(steps_back: int = 2):
    frame = inspect.currentframe()
    for step in range(steps_back):
        frame = frame.f_back
    module_name_full = str(inspect.getmodule(frame))
    return module_name_full[module_name_full.rfind('\\') + len('\\'):module_name_full.rfind('.')]


def get_calling_object(steps_back: int = 1):
    frame = inspect.currentframe()
    for step in range(steps_back):
        frame = frame.f_back
    return frame.f_code.co_qualname


class InternalError(Exception):
    """
    The Error internal to this program - called when a behavior has to be blocked
    :param: message (optional) - details conveyed after the module name and function name that called it
    """
    def __init__(self, message: str = ''):
        self.message = f'{get_calling_module()}.{get_calling_object(2)} error: {message}.'
        super().__init__(message)


if __name__ == "__main__":
    os.chdir("..")
