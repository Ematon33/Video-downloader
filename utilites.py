import os
import sys


def resource_path(relative_path):
    """
    Obtain the absolute path to a resource, works for development and when packaged with PyInstaller.

    PyInstaller creates a temporary folder and stores its path in the _MEIPASS attribute.
    This function checks for that attribute to determine the base path.
    """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
