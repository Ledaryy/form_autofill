import tkinter as tk
from tkinter import filedialog, Text
import os

from settings import *
from main import main_function

root = tk.Tk()


def add_file():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
    initialdir="/", 
    title="Select File",
    filetypes=(("Excel-files", "*.xlsx"), ("all files", "*.*"))
    )
    
    log_file(filename)

    label = tk.Label(frame, text=filename, bg="gray")
    label.pack()

def log_file(path_name):
    with open(LOG_FILE, 'a') as out:
        out.write(path_name + "\n")


def run_main():
    with open(LOG_FILE, 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
    main_function(excel_path=last_line)


canvas = tk.Canvas(root, height=600, width=1000, bg="#FFEFDB")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.1)

open_file = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42", command=add_file)
open_file.pack()

run = tk.Button(root, text="Run", padx=10,
                     pady=5, fg="white", bg="#263D42", command=run_main)
run.pack()



root.mainloop()