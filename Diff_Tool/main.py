# main loop that will allowm the user to choose which function they wish to perform. 
from diff_tool_functions import *


program_run = True

while program_run:
    
    user_selection = input("\nPlease choose an operation to perform\nUpload item #1\nSearch for an item #2\n'q' for quit\n")

    if user_selection == "1":
        file_import()
    if user_selection == "2":
        tmp_ObType= input("Is the item you are searching for folder (1) or file (2): ")
        tmp_ObName = input("Please enter the name of the object you wish to locate: ")
        fileObjectLocator(tmp_ObType, int(tmp_ObName))

        



    if user_selection.lower() == 'q':
        program_run = False