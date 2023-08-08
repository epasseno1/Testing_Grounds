A tool that can be used to identify differences between two text files. 

Libraries that will be used in the process.

pyinstaller .exe
Tkinter GUI
pyclip
os 
platform

Main functions - 

The ability to create filters that will remove dates and other information using 
regular expressions

ALlow the creation of custom filters using regular
expressions

integrate readio buttons into the gui that allow the toggling
of search critera

Allow for the files to be searched for by name

Within the GUI, show the differences in a different color than the
clear text.



I need to introduce logic and controls for the file search function that will allow 
for remediation in the event that a file is not found, or there are duplicate files.

This will require an input validation like function to serve as a loop 




I will use the file locater function to get the input from the user on the file they want to use
Then, the file object locater will take that information, perform a search, then if the 
file was found, return false and no file path. If the search succeeds, then return true, and the 
absolute path for the object. 











