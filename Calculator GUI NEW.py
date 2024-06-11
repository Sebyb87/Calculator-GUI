#Calculator GUI NEW

import tkinter as tk
from tkinter import messagebox
import os

def validate_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear_entry():
    entry.delete(0, tk.END)

def perform_calculation():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalid expression")

def save_to_memory():
    value = entry.get()
    if not validate_number(value):
        messagebox.showerror("Error", "Invalid value to save")
        return
    with open("calculator_memory.txt", "w") as file:
        file.write(value)
    memory_display.config(text=value)

def recall_from_memory():
    if not os.path.exists("calculator_memory.txt"):
        messagebox.showinfo("Info", "No value in memory.")
        return
    with open("calculator_memory.txt", "r") as file:
        value = file.read()
    entry.delete(0, tk.END)
    entry.insert(0, value)

def clear_memory():
    if os.path.exists("calculator_memory.txt"):
        os.remove("calculator_memory.txt")
        memory_display.config(text="")
    else:
        messagebox.showinfo("Info", "Memory is already empty.")

# Initialize the main application window
app = tk.Tk()
app.title("Handheld Calculator")
app.configure(bg='#E0E0E0')  # Light gray background

# Main display
entry = tk.Entry(app, font=('Arial', 20), justify='right', bd=10, insertwidth=4, width=15)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Memory display
memory_frame = tk.Frame(app, bg='#CCCCCC', bd=5, relief=tk.SUNKEN)
memory_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky='ew')
tk.Label(memory_frame, text="Memory:", font=('Arial', 12), bg='#CCCCCC').pack(side=tk.LEFT, padx=5)
memory_display = tk.Label(memory_frame, text="", font=('Arial', 12), bg='#FFFFFF', width=10, anchor='e')
memory_display.pack(side=tk.RIGHT, padx=5, fill=tk.X, expand=True)

# Button styling
button_font = ('Arial', 14)
button_relief = tk.RAISED
button_padx = 15
button_pady = 15

# Buttons

buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0' 
]

row_val = 2
col_val = 0

for button in buttons:
    if button == '0':
        tk.Button(app, text=button, font=button_font, relief=button_relief,
                  padx=button_padx, pady=button_pady, command=lambda x=button: button_click(x)).grid(row=5, column=1, columnspan=2, padx=1, pady=1, sticky='ew')
    else:
        tk.Button(app, text=button, font=button_font, relief=button_relief,
                  padx=button_padx, pady=button_pady, command=lambda x=button: button_click(x)).grid(row=row_val, column=col_val, padx=1, pady=1)
        col_val += 1
        if col_val > 2:
            col_val = 0
            row_val += 1

# Operation buttons on the right
tk.Button(app, text="+", font=button_font, relief=button_relief, bg='#FFA07A',
          padx=button_padx, pady=button_pady, command=lambda: button_click('+')).grid(row=2, column=3, padx=1, pady=1)
tk.Button(app, text="-", font=button_font, relief=button_relief, bg='#FFA07A',
          padx=button_padx, pady=button_pady, command=lambda: button_click('-')).grid(row=3, column=3, padx=1, pady=1)
tk.Button(app, text="*", font=button_font, relief=button_relief, bg='#FFA07A',
          padx=button_padx, pady=button_pady, command=lambda: button_click('*')).grid(row=4, column=3, padx=1, pady=1)
tk.Button(app, text="/", font=button_font, relief=button_relief, bg='#FFA07A',
          padx=button_padx, pady=button_pady, command=lambda: button_click('/')).grid(row=5, column=3, padx=1, pady=1)

# Memory and clear buttons on the right
tk.Button(app, text="M+", font=button_font, relief=button_relief, bg='#98FB98',
          padx=button_padx, pady=button_pady, command=save_to_memory).grid(row=2, column=4, padx=1, pady=1, sticky='ew')
tk.Button(app, text="MRC", font=button_font, relief=button_relief, bg='#98FB98',
          padx=button_padx, pady=button_pady, command=recall_from_memory).grid(row=3, column=4, padx=1, pady=1, sticky='ew')
tk.Button(app, text="MC", font=button_font, relief=button_relief, bg='#98FB98',
          padx=button_padx, pady=button_pady, command=clear_memory).grid(row=4, column=4, padx=1, pady=1, sticky='ew')

# Decimal, Equals, and Clear buttons
tk.Button(app, text=".", font=button_font, relief=button_relief,
          padx=button_padx, pady=button_pady, command=lambda: button_click('.')).grid(row=5, column=0, padx=1, pady=1)
tk.Button(app, text="=", font=button_font, relief=button_relief, bg='#FFD700',
          padx=button_padx, pady=button_pady, command=perform_calculation).grid(row=6, column=0, columnspan=4, padx=1, pady=1, sticky='ew')
tk.Button(app, text="C", font=button_font, relief=button_relief, bg='#FF6961',
          padx=button_padx, pady=button_pady, command=clear_entry).grid(row=5, column=4, padx=1, pady=1, sticky='ew')

# Loop for the GUI
app.mainloop()