import tkinter as tk 
from tkinter import messagebox
import random 

def clear ():
    for entry in entries.values():
        entry.delete(0, tk.END)

def toggle_password():
    if show_pass_var.get():
        entries["password"].config(show="")
    else:
        entries["password"].config(show="*")

window = tk.Tk()
window.title("NUBANK")
window_width = 600
window_height = 500
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
x_position = (screen_width//2) - (screen_height//3)
y_position = (window_height//2) - (window_width//3)
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
window.resizable(False, False)

header = tk.Frame(window, width=500, height=100, bg='blue', borderwidth=10, relief='ridge')
header.pack(side='top', fill='both')

text_header = tk.Label(header, text='NUBANK', fg='gold', bg='blue', font=('times new roman', 30))
text_header.pack(padx=10, pady=10)

box_login = tk.Frame(window, width=320, height=250, bg='blue', borderwidth=10, relief='sunken')
box_login.place(x=100, y=150)

form_field = ["username", 'password', 'age', 'email']
entries = {}

for row, label_text in enumerate(form_field):
    label = tk.Label(box_login, text=label_text.upper(), font=('times new roman', 15, 'bold'), fg='gold', bg='blue')
    label.grid(row=row, column=0, padx=5, pady=5, stick='e')

    entry = tk.Entry(box_login, show="*" if label_text == "password" else "")
    entry.grid(row=row, column=1, padx=5, pady=5)
    entries[label_text] = entry

show_pass_var = tk.BooleanVar()
tk.Checkbutton(
    box_login,
    text="Show Password",
    bg="blue",
    variable=show_pass_var,
    command=toggle_password
).grid(row=1, column=2, padx=5)

tk.Button(box_login, text="Clear", command=clear, bg='gold').grid(row=len(form_field), column=2, pady=10)



















window.mainloop()