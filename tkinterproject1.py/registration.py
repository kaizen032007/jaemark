import tkinter as tk

def open_registration_window(window):
    reg_win = tk.Toplevel(window)
    reg_win.title('Registration')
    reg_win.geometry('500x400')
    reg_win.configure(bg='gold')
    # 🟢 Make it fullscreen!
    reg_win.state('zoomed')


    icon = tk.PhotoImage(file='perpetual.png')
    reg_win.iconphoto(False, icon)
    reg_win.icon = icon


    # Title
    tk.Label(reg_win, text='Registration Form', font=('Arial', 35, 'bold'),
             bg='royal blue', fg='gold', width='200').pack(pady=(20, 5))
    
    # Subtext
    tk.Label(reg_win, text='STRICTLY TO STUDENTS WHO HAVE ENROLLED ALREADY.',
             bg='royal blue', fg='white', font=('arial', 17, 'bold'), width='70').pack(pady=(0, 15))

    # Container Frame (to group labels & entries)
    form_frame = tk.Frame(reg_win, bg='gold')
    form_frame.pack(fill='both', expand=True)

    # Label + Entry pairs
    for label_text in ['Name:', 'Email:', 'Password:', 'Student Number:']:
        row = tk.Frame(form_frame, bg='gold')
        row.pack(fill='x', padx=20, pady=5)

        tk.Label(row, text=label_text, width=15, anchor='w', bg='royal blue', fg='gold', font=('Arial', 18, 'bold') ).pack(side='left')
        entry = tk.Entry(row, width=100, show='*' if label_text == 'Password:' else '')
        entry.pack(side='left', padx=5)

    # Submit Button
    tk.Button(reg_win, text='Submit', bg='royal blue', fg='gold',
              font=('Arial', 12, 'bold')).pack(pady=20)

    # Optional: Exit Fullscreen with Escape key
    reg_win.bind("<Escape>", lambda event: reg_win.attributes("-fullscreen", False))

