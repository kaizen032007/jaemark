import tkinter as tk


def open_Admissions_window(window):
    admissions_win = tk.Toplevel(window)
    admissions_win.title('Admissions')
    admissions_win.geometry('400x400')
    admissions_win.configure(bg='white')
    # 🟢 Make it fullscreen!
    admissions_win.state('zoomed')

    icon = tk.PhotoImage(file='perpetual.png')
    admissions_win.iconphoto(False, icon)
    admissions_win.icon = icon

    tk.Label(admissions_win, text='Admissions Information', font=('Arial', 18, 'bold'), bg='white', fg='royal blue').pack(pady=20)
    # Example content
    tk.Label(admissions_win, text='Admission requirements:', bg='white').pack(anchor='w', padx=20)
    tk.Label(admissions_win, text='1. Completed application form', bg='white').pack(anchor='w', padx=40)
    tk.Label(admissions_win, text='2. High school diploma or equivalent', bg='white').pack(anchor='w', padx=40)
    tk.Label(admissions_win, text='3. Entrance exam results', bg='white').pack(anchor='w', padx=40)
                      