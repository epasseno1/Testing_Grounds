import tkinter as tk


# # This can be used to create the window that will eventually contain items for the applicaiton
# root = tk.Tk()
# root.mainloop()



root = tk.Tk()

## This can be used to adjust the initial size of the window that is opened when program is 
# launched. 
root.geometry("800x400")

# This is used to add a title to the window that is opened with the program
root.title("diffcheck.exe")

# This is used to add text to the GUI

# labels require a parent object, in this case, I will use the root itself as the parent.
label = tk.Label(root, text="Hello", font=('arial', 18))

# in the above, the parent object is the main window (root), Text is self explanitory, 
# and the fony uses the font type, and then the size of the font

# There are two parts to add the label, the second part is below
label.pack()


# Stopped at 5:21 - https://www.youtube.com/watch?v=ibf5cx221hk





# This value needs to remain at the bottom of the screen, sort of like HTML
root.mainloop()
















