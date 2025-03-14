import tkinter as tk
from tkinter import messagebox

class Car:
    def __init__(self, make, model, year, color, for_sale):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

class CarGUI:
    def __init__(self, root, car):
        self.car = car
        self.root = root
        self.root.title("Car Details")
        
        # Labels
        tk.Label(root, text="Make:").grid(row=0, column=0)
        tk.Label(root, text="Model:").grid(row=1, column=0)
        tk.Label(root, text="Year:").grid(row=2, column=0)
        tk.Label(root, text="Color:").grid(row=3, column=0)
        tk.Label(root, text="For Sale:").grid(row=4, column=0)
        
        # Entry fields
        self.make_entry = tk.Entry(root)
        self.make_entry.grid(row=0, column=1)
        self.make_entry.insert(0, car.make)
        
        self.model_entry = tk.Entry(root)
        self.model_entry.grid(row=1, column=1)
        self.model_entry.insert(0, car.model)
        
        self.year_entry = tk.Entry(root)
        self.year_entry.grid(row=2, column=1)
        self.year_entry.insert(0, car.year)
        
        self.color_entry = tk.Entry(root)
        self.color_entry.grid(row=3, column=1)
        self.color_entry.insert(0, car.color)
        
        # Checkbox for sale status
        self.sale_var = tk.BooleanVar()
        self.sale_var.set(car.for_sale)
        self.sale_checkbox = tk.Checkbutton(root, variable=self.sale_var)
        self.sale_checkbox.grid(row=4, column=1)
        
        # Buttons
        tk.Button(root, text="Update", command=self.update_car).grid(row=5, column=0, columnspan=2)
    
    def update_car(self):
        self.car.make = self.make_entry.get()
        self.car.model = self.model_entry.get()
        self.car.year = self.year_entry.get()
        self.car.color = self.color_entry.get()
        self.car.for_sale = self.sale_var.get()
        messagebox.showinfo("Updated", "Car details updated successfully!")

if __name__ == "__main__":
    car1 = Car("Toyota", "Rav4", "2024", "Black", False)
    car2 = Car("Nissan", "kick", "2025", "white", True)
    root = tk.Tk()
    app = CarGUI(root, car1)
    root.mainloop()
