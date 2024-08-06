import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk

# Function to fetch exchange rates
def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data["rates"]

# Function to convert USD to selected currency
def convert_currency():
    try:
        amount = float(entry_amount.get())
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        selected_currency = to_currency_var.get()
        rate = exchange_rates[selected_currency]
        converted_amount = amount * rate
        result_var.set(f"{amount:.2f} USD = {converted_amount:.2f} {selected_currency}")
    except ValueError as ve:
        messagebox.showerror("Error", f"Invalid input: {ve}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to clear inputs
def clear_inputs():
    entry_amount.delete(0, tk.END)
    result_var.set("")

# Initialize the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x300")
root.resizable(False, False)

# Fetch exchange rates
exchange_rates = get_exchange_rates()

# Header
header_label = ttk.Label(root, text="USD Currency Converter Using Python", font=("Helvetica", 16, "bold"))
header_label.pack(pady=10)

# Image
image_path = r"C:\Users\HP\Downloads\currency.png"
image = Image.open(image_path)
image = image.resize((50, 50), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)

# Amount input
amount_frame = ttk.Frame(root, padding="10")
amount_frame.pack(pady=5)

label_amount = ttk.Label(amount_frame, text="Amount")
label_amount.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_amount = ttk.Entry(amount_frame, width=20)
entry_amount.grid(row=0, column=1, padx=5, pady=5)

# From Currency input (fixed to USD)
from_currency_var = tk.StringVar(value="USD")
from_currency_label = ttk.Label(amount_frame, textvariable=from_currency_var, width=20)
from_currency_label.grid(row=0, column=2, padx=5, pady=5)

# To Currency input
to_currency_var = tk.StringVar()
to_currency_combobox = ttk.Combobox(amount_frame, textvariable=to_currency_var, values=list(exchange_rates.keys()), state="readonly", width=20)
to_currency_combobox.grid(row=0, column=3, padx=5, pady=5)

# Buttons
button_frame = ttk.Frame(root, padding="10")
button_frame.pack(pady=5)

button_convert = ttk.Button(button_frame, text="Search", command=convert_currency, style="TButton")
button_convert.grid(row=0, column=0, padx=10, pady=10)

button_clear = ttk.Button(button_frame, text="Clear", command=clear_inputs, style="TButton")
button_clear.grid(row=0, column=1, padx=10, pady=10)

# Result display
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the main loop
root.mainloop()

