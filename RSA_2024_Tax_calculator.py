import tkinter as tk
from tkinter import ttk

# Function to calculate tax based on annual income
def calculate_tax(annual_income):
    if annual_income <= 237100:
        tax = annual_income * 0.18
    elif annual_income <= 370500:
        tax = 42678 + (annual_income - 237100) * 0.26
    elif annual_income <= 512800:
        tax = 77362 + (annual_income - 370500) * 0.31
    elif annual_income <= 673000:
        tax = 121475 + (annual_income - 512800) * 0.36
    elif annual_income <= 857900:
        tax = 179147 + (annual_income - 673000) * 0.39
    elif annual_income <= 1817000:
        tax = 251258 + (annual_income - 857900) * 0.41
    else:
        tax = 644489 + (annual_income - 1817000) * 0.45
    return tax

# Function triggered by the button to perform the calculation
def on_calculate():
    income = float(income_entry.get())
    period = period_combo.get()
    # Adjusting for the period to calculate the annual income correctly
    # Doesnt matter what time period you select anual and monthy are both displayed 
    annual_income = income if period == 'Yearly' else income * 12
    annual_tax = calculate_tax(annual_income)
    monthly_tax = annual_tax / 12 if period == 'Monthly' else annual_tax / 12
    tax_result_var.set(f"Annual Tax: {annual_tax:.2f} | Monthly Tax: {monthly_tax:.2f}")

# Creating the main window
root = tk.Tk()
root.title("Income Tax Calculator")

# Adding a grid
mainframe = ttk.Frame(root, padding="12")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Variables
tax_result_var = tk.StringVar()

# Widgets
income_label = ttk.Label(mainframe, text="Income (Monthly/Yearly):")
income_label.grid(column=0, row=0, sticky=tk.W)

income_entry = ttk.Entry(mainframe)
income_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

period_label = ttk.Label(mainframe, text="Tax Period:")
period_label.grid(column=0, row=1, sticky=tk.W)

period_combo = ttk.Combobox(mainframe, values=["Monthly", "Yearly"])
period_combo.grid(column=1, row=1, sticky=(tk.W, tk.E))
period_combo.set("Monthly")

calculate_btn = ttk.Button(mainframe, text="Calculate Tax", command=on_calculate)
calculate_btn.grid(column=1, row=2, sticky=tk.W)

tax_result_label = ttk.Label(mainframe, textvariable=tax_result_var)
tax_result_label.grid(column=0, row=3, columnspan=2, sticky=tk.W)

# Running the application
root.mainloop()
