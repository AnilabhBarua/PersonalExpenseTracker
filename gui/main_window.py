import sys
sys.path.append('src')
import tkinter as tk
from src.expense_manager import add_expense

def submit_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        description = description_entry.get()
        add_expense(amount, category, description)
    except ValueError:
        # Handle invalid input (non-numeric amount)
        pass

window = tk.Tk()
window.title("Expense Tracker")

# Inputs for amount, category, description
tk.Label(window, text="Amount").grid(row=0, column=0)
amount_entry = tk.Entry(window)
amount_entry.grid(row=0, column=1)

tk.Label(window, text="Category").grid(row=1, column=0)
category_entry = tk.Entry(window)
category_entry.grid(row=1, column=1)

tk.Label(window, text="Description").grid(row=2, column=0)
description_entry = tk.Entry(window)
description_entry.grid(row=2, column=1)

# Submit Button
submit_button = tk.Button(window, text="Add Expense", command=submit_expense)
submit_button.grid(row=3, column=0, columnspan=2)

window.mainloop()
