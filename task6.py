import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox, filedialog

# Define the main application class
class RestaurantManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing System")
        self.root.geometry("1000x600")  # Adjusted size for more sections

        # Set blue color scheme
        self.bg_color = "#ADD8E6"  # Light blue background color
        self.fg_color = "#000080"  # Dark blue foreground color

        self.root.configure(bg=self.bg_color)

        # Initialize variables for storing item quantities
        self.drink_vars = {
            "Lassi": tk.IntVar(), "Coffee": tk.IntVar(), "Tea": tk.IntVar(), "Juice": tk.IntVar(),
            "Shakes": tk.IntVar(), "Milk": tk.IntVar(), "Shikanji": tk.IntVar(), "Redbull": tk.IntVar()
        }

        self.food_vars = {
            "Roti": tk.IntVar(), "Dal Makhni": tk.IntVar(), "Mutter Panner": tk.IntVar(), "Paratha": tk.IntVar(),
            "Mix Veg": tk.IntVar(), "Omelete": tk.IntVar(), "Veg Biryani": tk.IntVar(), "Rice": tk.IntVar()
        }

        # Additional food sections
        self.additional_food_vars = {
            "Paneer Tikka": tk.IntVar(), "Naan": tk.IntVar(), "Chole Bhature": tk.IntVar(), "Pulao": tk.IntVar()
        }

        # Variables to display costs
        self.total_drinks_cost = tk.StringVar()
        self.total_foods_cost = tk.StringVar()
        self.total_additional_foods_cost = tk.StringVar()
        self.service_charge = tk.StringVar()
        self.paid_tax = tk.StringVar()
        self.subtotal = tk.StringVar()
        self.total_cost = tk.StringVar()

        # Call method to create the GUI layout
        self.create_widgets()

    def create_widgets(self):
        # Drinks section
        drinks_frame = tk.LabelFrame(self.root, text="Drinks", padx=10, pady=10, bg=self.bg_color, fg=self.fg_color)
        drinks_frame.grid(row=0, column=0, padx=10, pady=10)

        for i, (drink, var) in enumerate(self.drink_vars.items()):
            tk.Label(drinks_frame, text=drink, bg=self.bg_color, fg=self.fg_color).grid(row=i, column=0, sticky='w')
            tk.Entry(drinks_frame, textvariable=var).grid(row=i, column=1)

        # Foods section
        foods_frame = tk.LabelFrame(self.root, text="Foods", padx=10, pady=10, bg=self.bg_color, fg=self.fg_color)
        foods_frame.grid(row=0, column=1, padx=10, pady=10)

        for i, (food, var) in enumerate(self.food_vars.items()):
            tk.Label(foods_frame, text=food, bg=self.bg_color, fg=self.fg_color).grid(row=i, column=0, sticky='w')
            tk.Entry(foods_frame, textvariable=var).grid(row=i, column=1)

        # Additional Foods section
        additional_foods_frame = tk.LabelFrame(self.root, text="Additional Foods", padx=10, pady=10, bg=self.bg_color, fg=self.fg_color)
        additional_foods_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        for i, (food, var) in enumerate(self.additional_food_vars.items()):
            tk.Label(additional_foods_frame, text=food, bg=self.bg_color, fg=self.fg_color).grid(row=i, column=0, sticky='w')
            tk.Entry(additional_foods_frame, textvariable=var).grid(row=i, column=1)

        # Cost Display
        cost_frame = tk.LabelFrame(self.root, text="Cost", padx=10, pady=10, bg=self.bg_color, fg=self.fg_color)
        cost_frame.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        tk.Label(cost_frame, text="Cost of Drinks:", bg=self.bg_color, fg=self.fg_color).grid(row=0, column=0, sticky='w')
        tk.Entry(cost_frame, textvariable=self.total_drinks_cost).grid(row=0, column=1)

        tk.Label(cost_frame, text="Cost of Foods:", bg=self.bg_color, fg=self.fg_color).grid(row=1, column=0, sticky='w')
        tk.Entry(cost_frame, textvariable=self.total_foods_cost).grid(row=1, column=1)

        tk.Label(cost_frame, text="Cost of Additional Foods:", bg=self.bg_color, fg=self.fg_color).grid(row=2, column=0, sticky='w')
        tk.Entry(cost_frame, textvariable=self.total_additional_foods_cost).grid(row=2, column=1)

        tk.Label(cost_frame, text="Service Charge:", bg=self.bg_color, fg=self.fg_color).grid(row=3, column=0, sticky='w')
        tk.Entry(cost_frame, textvariable=self.service_charge).grid(row=3, column=1)

        tk.Label(cost_frame, text="Paid Tax:", bg=self.bg_color, fg=self.fg_color).grid(row=4, column=0, sticky='w')
        tk.Entry(cost_frame, textvariable=self.paid_tax).grid(row=4, column=1)

        tk.Label(cost_frame, text="Subtotal:", bg=self.bg_color, fg=self.fg_color).grid(row=5, column=0, sticky='w')
        tk.Entry(cost_frame, textvariable=self.subtotal).grid(row=5, column=1)

        tk.Label(cost_frame, text="Total Cost:", bg=self.bg_color, fg=self.fg_color).grid(row=6, column=0, sticky='w')
        tk.Entry(cost_frame, textvariable=self.total_cost).grid(row=6, column=1)

        # Buttons
        button_frame = tk.Frame(self.root, padx=10, pady=10, bg=self.bg_color)
        button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        tk.Button(button_frame, text="Total", command=self.calculate_total).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Save", command=self.save_bill).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Send", command=self.send_bill).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Clear", command=self.clear_fields).grid(row=0, column=3, padx=5)
        tk.Button(button_frame, text="Exit", command=self.root.quit).grid(row=0, column=4, padx=5)

    def calculate_total(self):
        # Prices of items
        prices = {
            "Lassi": 50, "Coffee": 20, "Tea": 10, "Juice": 30, "Shakes": 50, 
            "Milk": 20, "Shikanji": 15, "Redbull": 150,
            "Roti": 5, "Dal Makhni": 128, "Mutter Panner": 150, "Paratha": 48,
            "Mix Veg": 70, "Omelete": 20, "Veg Biryani": 120, "Rice": 58,
            "Paneer Tikka": 200, "Naan": 15, "Chole Bhature": 150, "Pulao": 80
        }

        # Calculate costs for drinks
        total_drinks_cost = sum(var.get() * prices[drink] for drink, var in self.drink_vars.items())

        # Calculate costs for foods
        total_foods_cost = sum(var.get() * prices[food] for food, var in self.food_vars.items())

        # Calculate costs for additional foods
        total_additional_foods_cost = sum(var.get() * prices[food] for food, var in self.additional_food_vars.items())

        service_charge = 50  # fixed service charge
        subtotal = total_drinks_cost + total_foods_cost + total_additional_foods_cost + service_charge
        tax = subtotal * 0.05  # 5% tax
        total_cost = subtotal + tax

        # Update variables
        self.total_drinks_cost.set(f'₹{total_drinks_cost:.2f}')
        self.total_foods_cost.set(f'₹{total_foods_cost:.2f}')
        self.total_additional_foods_cost.set(f'₹{total_additional_foods_cost:.2f}')
        self.service_charge.set(f'₹{service_charge:.2f}')
        self.subtotal.set(f'₹{subtotal:.2f}')
        self.paid_tax.set(f'₹{tax:.2f}')
        self.total_cost.set(f'₹{total_cost:.2f}')

    def clear_fields(self):
        # Clear all fields
        for var in list(self.drink_vars.values()) + list(self.food_vars.values()) + list(self.additional_food_vars.values()):
            var.set(0)

        # Clear cost display
        for var in [self.total_drinks_cost, self.total_foods_cost, self.total_additional_foods_cost, 
                    self.service_charge, self.paid_tax, self.subtotal, self.total_cost]:
            var.set("")

    def save_bill(self):
        # Save the bill to a file
        bill_details = f'''
        Total Drinks Cost: {self.total_drinks_cost.get()}
        Total Foods Cost: {self.total_foods_cost.get()}
        Total Additional Foods Cost: {self.total_additional_foods_cost.get()}
        Service Charge: {self.service_charge.get()}
        Paid Tax: {self.paid_tax.get()}
        Subtotal: {self.subtotal.get()}
        Total Cost: {self.total_cost.get()}
        '''
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file:
            file.write(bill_details)
            file.close()
            messagebox.showinfo("Save Bill", "Bill Saved Successfully!")

    def send_bill(self):
        # Sending the bill logic here (e.g., email, printing)
        messagebox.showinfo("Send Bill", "Bill Sent Successfully!")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    root.mainloop()
