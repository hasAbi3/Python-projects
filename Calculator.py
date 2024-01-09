from tkinter import *
import tkinter as tk

# Create tkinter container
root = Tk()
root.title("Calculator")

expression = ""
input_text = StringVar()
input_text.set("0")  # Initialize the input field with "0"

# Define tkinter widget functions

# btn_click updates the input field whenever a button is clicked
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# btn_clear clears the input field when the 'Clear' button is pressed
def btn_clear():
    global expression
    expression = ""
    input_text.set("0")

# btn_equal calculates the entered expression
def btn_equal():
    global expression
    try:
        result = str(eval(expression))  # eval() evaluates the string expression
        input_text.set(result)
        expression = result
    except Exception:
        input_text.set("Error")
        expression = ""

# Create the input field
input_field = Entry(root, font=('arial', 18, 'bold'), textvariable=input_text, bd=0, insertwidth=4, width=14,
                    justify='right')
input_field.grid(row=0, column=0, columnspan=4)

# Define button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons
row_val = 1
col_val = 0
for button in buttons:
    Button(root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'),
           bd=8, command=lambda button=button: btn_click(button) if button != '=' else btn_equal()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add the clear button
Button(root, text="C", padx=20, pady=20, font=('arial', 20, 'bold'), bd=8, command=btn_clear).grid(row=row_val, column=col_val)

root.mainloop()




