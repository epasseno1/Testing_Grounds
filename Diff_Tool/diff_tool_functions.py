import zipfile, os
import platform
import os
import shutil
from pathlib import Path
import threading
import time



class Core():
    """A class that will house the main logic for the program."""

    def __init__(self , obj_1 ="", obj_2 = "", current_obj= {"object_type":"", "object_name":"", "object_location":"", "object_contents":""}):
        """Constructor for the core class."""
        self.current_obj = current_obj
        self.obj_1 = obj_1
        self.obj_2 = obj_2
    
    def file_import(self):
        """Will be used for input validation and looping, but main logic needs work still. """
        """A function that can be used to import files."""
        object_choice = input("Are you importing object 1 or object 2: ")
        
        if object_choice == "1":
            self.get_obj_location()
            self.obj_1 = self.current_obj
            print(f"Here is the path of the file you selected: {self.obj_1}")
            
        elif object_choice == "2":
            self.get_obj_location()
            self.obj_2 =self.current_obj 
            print(f"Here is the path of the file you selected: {self.obj_2}")
            
        else:
            print("you entered an invalid option")

    def fileObjectLocator(self):
        """A method that performs a file walk beginning at the root directory"""
        root = self.getPath()
        my_return = os.walk(root)
        for item in my_return:
            for filename in item[int(self.current_obj["object_type"])]:
                if filename == self.current_obj["object_name"]:
                    location = (os.path.join(item[0], filename))
                    return location
                
    def get_obj_location(self):
        """A function that is used to capture the name of an object or file, and pass it to a validator"""
        self.current_obj["object_type"] = input("Is the item you are searching for folder (1) or file (2): ")
        self.current_obj["object_name"] = input("Please enter the name of the object you wish to locate: ")
        self.current_obj["object_location"] = self.fileObjectLocator()

    def print_objects(self):
        """A method that will print the values of the current objects"""
        print(f"\nObject 1 is currently stored as: {self.obj_1}\n")
        print(f"Object 2 is currently stored as: {self.obj_2}\n")

    def getPath(self):
        """A function that will be used to determine the OS of the host system which is used for file lookups
        """
        my_system = platform.system() 

        if my_system == "Windows":
            root_fs = "C:\\"
        else:
            root_fs ="/"
        return root_fs


