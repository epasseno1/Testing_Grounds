# main loop that will allowm the user to choose which function they wish to perform. 
from diff_tool_functions import *


program_run = True

while program_run:
    
    user_selection = input("\nPlease choose an operation to perform\nUpload item #1\nSearch for an item #2\n'q' for quit\n")

    if user_selection == "1":
        file_import()
    if user_selection == "2":
        obj_location = get_obj_name()
        print(obj_location)
        



    if user_selection.lower() == 'q':
        program_run = False