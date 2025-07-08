import tkinter as tk

def open_reservation_window(window):
    reservation_win = tk.Toplevel(window)
    reservation_win.title('Reservation')
    reservation_win.geometry('500x400')
    reservation_win.configure(bg='gold')
    reservation_win.state('zoomed')
    icon = tk.PhotoImage(file='perpetual.png')
    icon.iconphoto(False, icon)
    icon.icon = icon

    Frame = tk.Frame(reservation_win, bg='gold')
    Frame.pack(fill='both', expand=True)

    label = tk.Label(reservation_win, text='Reservation Form', font=('Arial', 35, 'bold'),
                     bg='royal blue', fg='gold', width='200')
    label.pack(pady=(20, 5))


    # Optional: Exit Fullscreen with Escape key
    reservation_win.bind("<Escape>", lambda event: reservation_win.attributes("-fullscreen", False))

