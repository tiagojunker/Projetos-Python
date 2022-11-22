from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()

def select_directory():
    folder_selected = filedialog.askdirectory()
    return folder_selected

select_directory()