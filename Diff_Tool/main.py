# main loop that will allowm the user to choose which function they wish to perform. 
from diff_tool_functions import *


program_run = True


core_method = Core()

while program_run:
    
    user_selection = input("\nPlease choose an operation to perform:\n\nUpload item (1)\nSearch for an item (2)\nPrint current objects (3)\n'q' for quit\n\nSelection: ")

    if user_selection == "1":
        core_method.file_import()
    if user_selection == "2":
        obj_location = core_method.get_obj_location()
    if user_selection == "3":
        obj_location = core_method.print_objects()
        
        



    if user_selection.lower() == 'q':
        program_run = False
