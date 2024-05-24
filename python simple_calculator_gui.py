# Importing Tkinter module to be able to create the GUI
import tkinter as tk
from tkinter import messagebox

# Function to validate if the input string is a valid number
def validate_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

# Function to perform the calculation based on user inputs and selected operation
def perform_calculation():
    first_number = entry_first_number.get()
    second_number = entry_second_number.get()
    operation = operation_var.get()

    # Validate the inputs
    if not validate_number(first_number) or not validate_number(second_number):
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        return

    # Convert inputs to float
    first_number = float(first_number)
    second_number = float(second_number)

    # Perform the selected operation
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            messagebox.showerror("Math Error", "Division by zero is not allowed.")
            return
        result = first_number / second_number
    else:
        messagebox.showerror("Operation Error", "Invalid operation selected.")
        return
    
    # Display the result in the result label
    result_label.config(text=f"{result}")

# Initialize the main application window
app = tk.Tk()
app.title("Simple Calculator")


# Input box for the first number
tk.Label(app, text="Enter the first number:").grid(row=0, column=0, padx=10, pady=5)
entry_first_number = tk.Entry(app)
entry_first_number.grid(row=0, column=1, padx=10, pady=5)

# Input box for the second number
tk.Label(app, text="Enter the second number:").grid(row=1, column=0, padx=10, pady=5)
entry_second_number = tk.Entry(app)
entry_second_number.grid(row=1, column=1, padx=10, pady=5)

# Operations text
tk.Label(app, text="Choose an operation:").grid(row=2, column=0, padx=10, pady=5)

# Variable to store the selected operation
operation_var = tk.StringVar(value="+")
operation_font = ('Helvetica', 16)

# Operations buttons
tk.Radiobutton(app, text="+", variable=operation_var, value="+", font=operation_font).grid(row=2, column=1, padx=5, pady=5, sticky="w")
tk.Radiobutton(app, text="-", variable=operation_var, value="-", font=operation_font).grid(row=2, column=1, padx=5, pady=5, sticky="n")
tk.Radiobutton(app, text="*", variable=operation_var, value="*", font=operation_font).grid(row=2, column=2, padx=5, pady=5, sticky="e")
tk.Radiobutton(app, text="/", variable=operation_var, value="/", font=operation_font).grid(row=2, column=1, padx=5, pady=5, sticky="se")

# Calculate button to trigger the calculation
tk.Button(app, text="Calculate", command=perform_calculation, font=('Helvetica', 12)).grid(row=3, column=0, columnspan=5, pady=10)

# Visual box for the result
result_label = tk.Label(app, text="Result:", relief="sunken", font=('Helvetica', 16), width=15, anchor="e")
result_label.grid(row=4, column=0, columnspan=5, pady=5, padx=10)

# Loop for the GUI
app.mainloop()
