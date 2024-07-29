import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function Definitions
def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero is not allowed.")
        else:
            result = num1 / num2
            result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# GUI Setup
root = tk.Tk()
root.title("Simple Calculator")

# Load an image (if you have an icon or any other image to use)
# Replace 'calculator_icon.png' with your image file path
# try:
#     img = Image.open("calculator_icon.png")
#     img = img.resize((32, 32), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(img)
#     root.iconphoto(False, img)
# except IOError:
#     print("Image file not found.")

# Create and place widgets
tk.Label(root, text="Number 1:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Number 2:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="Add", command=add).grid(row=2, column=0, pady=5)
tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1, pady=5)
tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0, pady=5)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=1, pady=5)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
