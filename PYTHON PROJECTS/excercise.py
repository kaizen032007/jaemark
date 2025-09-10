import tkinter as tk


window = tk.Tk()
window.geometry("500x500")

forms = ['username', 'email', 'age', 'phone']
entries = {}

for name, label_text in enumerate(forms):
    label = tk.Label(window, text=label_text, fg='black')
    label.grid(row=name, column=0, padx=5, pady=5, stick='e')




window.mainloop()