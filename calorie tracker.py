import tkinter as tk
import time
import random
from tkinter import messagebox

window = tk.Tk()
window.geometry("500x500")
window.state("zoomed")

header = tk.Frame(window, bg='blue', width=200, height=200).pack(fill='x', expand=True)

label = tk.Label(window, text="TIMECLOCK", bg='gold', fg='blue').place(x=100, y=200)


window.mainloop()