import tkinter as tk
from tkinter import messagebox

def click(tap):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + tap)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "SYNTAX ERROR")

window = tk.Tk()
window.title("CALCULATOR")
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_position = (screen_width//2) - (window_width//2)
y_position = (screen_height//2) - (window_height//2)

window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

entry = tk.Entry(window, borderwidth=10, relief='sunken', fg='red', font=('arial', 20), justify='center')
entry.pack(padx=10, pady=10, fill='both')

buttons = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
]

for rows in buttons:
    row = tk.Frame(window)
    row.pack(expand=True, fill='both')
    for button_text in rows:
        button_text = tk.Button(row, text=button_text, borderwidth=10, relief='ridge', border=10, font=('arial', 20),
                                command=lambda text=button_text: click(text))
        button_text.pack(expand=True, side='left', fill='both')
    
equal_frame = tk.Frame(window)
equal_frame.pack(expand=True, fill='both')
equal_button = tk.Button(equal_frame, borderwidth=10, text='=', bg='green', relief='sunken', command=calculate)
equal_button.pack(fill='both', side='left', expand=True, padx=2, pady=2)

clear_button = tk.Button(window, borderwidth=10, text='CLEAR', border=10, bg='red', font=('arial', 10), command=clear)
clear_button.pack(expand=True, fill='both', side='bottom')





window.mainloop()
