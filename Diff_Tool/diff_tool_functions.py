
from platform import *



def file_import():
    """A function that can be used to import files."""
    print("I worked")


def file_locator():
    """A function that can be used to locate files on the C: drive and copy their ABS or REL path to the clipboard."""


def file_find():
    """A function that is used to locate files within the FS of the system"""


def getPath():
    """A function that will be used to determine the OS of the host system"""
    my_system = platform.system() 

    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs ="/"
    return root_fs