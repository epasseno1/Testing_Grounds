A tool that can be used to identify differences between two text files. 

Libraries that will be used in the process.

pyinstaller .exe
Tkinter GUI
pyclip
os 
platform

Main functions - 

The ability to create filters that will remove dates and other information using 
pre-built regular expressions.

ALlow the creation of custom filters using regular
expressions.

integrate radio buttons into the gui that allow the toggling
of search critera.

Allow for the files to be searched for by name or folder. If the desired file is in a .zip folder, the program will unzip the folder in the desired directory,
and load the desired unzipped file into the program. 

Within the GUI, show the differences in a different color than the
clear text.

Allow for users to copy snippets of text and have the program grab clipboard contents for 
analysis.


Problem #1:
I want to nest everything into a class to make object reference much easier. 



Problem #2:

I need to introduce logic and controls for the file search function that will allow 
for remediation in the event that a file is not found, or there are duplicate files.


File & folder found - working for the first value closest to the root directory.

Multiple files found - Need to append the absolute paths to a list, then present the 
list to the user and allow them to choose the index of the item that they want. 

No files found - I need to make sure that if no files were found that walk error out properly




















Notes:


I will use the file locater function to get the input from the user on the file they want to use
Then, the file object locater will take that information, perform a search, then if the 
file was found, return false and no file path. If the search succeeds, then return true, and the 
absolute path for the object. 

An approach to finding multiple values would be to append reseults to a list, and then filter
any new results from an ongoing search. once the program finds a result it updates the list,
and continues the walk. 

If the program restarts the walk and then uses the list to skip over duplcates, this is going
to prolong the search process. 













