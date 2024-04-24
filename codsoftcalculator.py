import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display and input numbers
input_entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 14))
input_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to update the entry with numbers
def click(num):
    current = input_entry.get()
    input_entry.delete(0, tk.END)
    input_entry.insert(tk.END, str(current) + str(num))

# Function to handle addition
def add():
    global fnum
    global operation
    operation = "+"
    fnum = float(input_entry.get())
    input_entry.delete(0, tk.END)

# Function to handle subtraction
def sub():
    global fnum
    global operation
    operation = "-"
    fnum = float(input_entry.get())
    input_entry.delete(0, tk.END)

# Function to handle multiplication
def mul():
    global fnum
    global operation
    operation = "*"
    fnum = float(input_entry.get())
    input_entry.delete(0, tk.END)

# Function to handle division
def div():
    global fnum
    global operation
    operation = "/"
    fnum = float(input_entry.get())
    input_entry.delete(0, tk.END)

# Function to handle percentage
def percentage():
    num = float(input_entry.get())
    result = num / 100
    input_entry.delete(0, tk.END)
    input_entry.insert(tk.END, result)

# Function to handle exponentiation
def exponent():
    global fnum
    global operation
    operation = "**"
    fnum = float(input_entry.get())
    input_entry.delete(0, tk.END)

# Function to handle clearing the entry
def clear():
    input_entry.delete(0, tk.END)

# Function to handle the equal button
def equal():
    try:
        snum = float(input_entry.get())
        if operation == "+":
            result = fnum + snum
        elif operation == "-":
            result = fnum - snum
        elif operation == "*":
            result = fnum * snum
        elif operation == "/":
            if snum == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = fnum / snum
        elif operation == "**":
            result = fnum ** snum
        else:
            result = "Error"
        
        input_entry.delete(0, tk.END)
        input_entry.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: click(0))

button_add = tk.Button(root, text="+", padx=40, pady=20, command=add)
button_sub = tk.Button(root, text="-", padx=40, pady=20, command=sub)
button_mul = tk.Button(root, text="*", padx=40, pady=20, command=mul)
button_div = tk.Button(root, text="/", padx=40, pady=20, command=div)
button_per = tk.Button(root, text="%", padx=40, pady=20, command=percentage)
button_int = tk.Button(root, text="^", padx=40, pady=20, command=exponent)
button_equal = tk.Button(root, text="=", padx=40, pady=20, command=equal)
button_clear = tk.Button(root, text="AC", padx=85, pady=20, command=clear)

# Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_per.grid(row=4, column=1)
button_int.grid(row=4, column=2)
button_equal.grid(row=5, column=2, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=2)

root.mainloop()