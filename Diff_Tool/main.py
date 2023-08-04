# main loop that will allowm the user to choose which function they wish to perform. 
from diff_tool_functions import *


program_run = True

while program_run:
    
    user_selection = input("\nPlease choose an operation to perform\nUpload item #1\nUpload item #2\nSearch for an item\n'q' for quit\n")

    if user_selection == "1":
        file_import()

    if user_selection =="2":
        file_import()


    if user_selection.lower() == 'q':
        program_run = False