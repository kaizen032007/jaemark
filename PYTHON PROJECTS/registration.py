import tkinter as tk
from tkinter import messagebox

def registration():
    username = entries['username'].get()
    password = entries['password'].get()
    age = entries['age'].get()
    email = entries['email'].get()

    errors = []

    # username
    if len(username) < 3:
        errors.append("YOUR USERNAME MUST CONTAIN MORE THAN THREE CHARACTERS")
    if " " in username:
        errors.append("YOUR USERNAME MUST NOT CONTAIN SPACES")
    if not username.isalpha():
        errors.append("YOUR USERNAME MUST NOT CONTAIN ANY DIGITS")

    # age
    if not age.isdigit():
        errors.append("YOUR AGE MUST BE DIGITS ONLY")
    else:
        age = int(age)
        if age < 13 or age > 100:
            errors.append("YOUR AGE MUST BE BETWEEN 13 AND 100")

    # email
    if "@" not in email or "." not in email:
        errors.append("YOUR EMAIL MUST CONTAIN @ AND .")
    if " " in email:
        errors.append("YOUR EMAIL MUST NOT CONTAIN ANY SPACES")

    if errors:
        error_message = '\n'.join(errors)
        messagebox.showerror("INVALID REGISTRATION", error_message)
    else:
        messagebox.showinfo("SUCCESS", f"Welcome {username.upper()}! Your account has been created!")

def clear():
    for entry in entries.values():
        entry.delete(0, tk.END)

def toggle_password():
    if show_pass_var.get():
        entries["password"].config(show="")
    else:
        entries["password"].config(show="*")

# ------------- Window Setup -------------
window = tk.Tk()
window.title("BANCO DE ORO")
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width // 2) - (screen_height // 3)
y_position = (window_width // 2) - (window_height // 5)
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
window.resizable(False, False)

# ------------- Header -------------
header = tk.Frame(window, width=100, height=100, bg='green', relief='ridge', borderwidth=10)
header.pack(side='top', fill='x')

header_text = tk.Label(header, text='UNIVERSITY BANK', fg='gold', font=('times new roman', 20), bg='green')
header_text.pack(padx=5, pady=5)

# ------------- Background -------------
background = tk.Frame(window, bg='#83eb34')
background.pack(fill='both', expand=True)

box = tk.Frame(window, bg='#19b31c', width=350, height=300, relief='groove', borderwidth=20)
box.place(x=75, y=120)

# ------------- Form Fields -------------
fields = ["username", "password", "age", "email"]
entries = {}

for row, label_text in enumerate(fields):
    label = tk.Label(box, text=label_text.upper(), font=("arial", 10, 'bold'), bg='#19b31c', fg='black')
    label.grid(row=row, column=0, padx=5, pady=5, sticky='e')

    entry = tk.Entry(box, show="*" if label_text == "password" else "") 
    entry.grid(row=row, column=1, padx=5, pady=5)
    entries[label_text] = entry

# ------------- Show Password Checkbox -------------
show_pass_var = tk.BooleanVar()
tk.Checkbutton(
    box,
    text="Show Password",
    bg='#19b31c',
    variable=show_pass_var,
    command=toggle_password
).grid(row=1, column=2, padx=5)

# ------------- Buttons -------------
tk.Button(box, text="Register", command=registration, bg='gold').grid(row=len(fields), column=1, pady=10)
tk.Button(box, text="Clear", command=clear, bg='gold').grid(row=len(fields), column=2, pady=10)

window.mainloop()
