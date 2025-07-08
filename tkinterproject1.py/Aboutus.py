import tkinter as tk 

def open_aboutus_window(window):
    aboutus_win = tk.Toplevel(window)
    aboutus_win.title('About Us')
    aboutus_win.geometry('400x400')
    aboutus_win.configure(bg='white')
    #contents




    #Title
    tk.Label(aboutus_win, text='About us!', font=('arial', 20, 'bold'), bg='white', fg='royal blue').place(x=50, y=20)

    #Subtext
    tk.Label(aboutus_win, text='We are a school that values education and excellence.', bg='white', fg='black').place(x=100, y=100)
