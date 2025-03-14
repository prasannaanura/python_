import tkinter as tk
from tkinter import messagebox

# Example Python function
def add_numbers(num1, num2):
    return num1 + num2

# GUI
def on_calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = add_numbers(num1, num2)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("invalid input", "Please enter valid numbers try again")

# Create the main window
root = tk.Tk()
root.title("My Simple Calculator")

# Add widgets
tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

calc_button = tk.Button(root, text="Calculate", command=on_calculate)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=3, column=0, columnspan=2, pady=20)

# Run the main event loop
root.mainloop()
