import tkinter as tk
from tkinter import messagebox

def create_input_form(root, fields):
    inputs = {}
    for idx, field in enumerate(fields):
        label = tk.Label(root, text=field)
        label.grid(row=idx, column=0)
        entry = tk.Entry(root)
        entry.grid(row=idx, column=1)
        inputs[field] = entry
    return inputs

def show_message(title, message):
    messagebox.showinfo(title, message)
