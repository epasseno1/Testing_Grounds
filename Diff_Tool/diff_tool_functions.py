import zipfile, os
import platform
import os
import shutil
from pathlib import Path




# def file_import():
"""Will be used for input validation and looping, but main logic needs work still. """
#     """A function that can be used to import files."""
#     tmp_file = file_locator()
#     print(tmp_file)



def get_obj_name():
    """A function that is used to capture the name of an object or file, and pass it to a validator"""
    tmp_ObType= input("Is the item you are searching for folder (1) or file (2)? ")
    tmp_ObName = input("Please enter the name of the object you wish to locate.")
    # Here I need to start the while false loop and send the input over to the validator
    # Things to validate for obj type are that the input is nothing but numbers, and not empty
    # things to validate for the file name; ban special characters, limit length of filename, no blank values. 


def file_import():
    """A function that can be used to locate files on the C: drive and copy their ABS or REL path to the clipboard."""
    tmp_file_found = fileObjectLocator(tmp_ObName, int(tmp_ObType))
    print(tmp_file_found)

    
def fileObjectLocator(temp_fileN, temp_type):
    root = getPath()
    my_return = os.walk(root)

    for item in my_return:
        for filename in item[temp_type]:
            if filename == temp_fileN:
                location = (os.path.join(item[0], filename))
                return location




def getPath():
    """A function that will be used to determine the OS of the host system which is used for file lookups
    """
    my_system = platform.system() 

    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs ="/"
    return root_fs


