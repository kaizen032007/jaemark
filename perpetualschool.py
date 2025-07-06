import tkinter as tk 
import random
import tkinter as messagebox



#GUI
window = tk.Tk()
window.geometry('500x500')

#sidebar
sidebar = tk.Frame(window, width=250, bg='gold')
sidebar.pack(side='left', fill='y')

#sidebar buttons
sidebar_Hbuttons = tk.Button(sidebar, text='Home', command=lambda: 
                            messagebox.showinfo("Home"), width=27, height=3, font=('arial', 10, 'bold'), 
                            bg='royal blue', fg='gold')
sidebar_Hbuttons.pack(padx=10, pady=10)

sidebar_Ebuttons = tk.Button(sidebar, text='Admissions', command=lambda:
                            messagebox.showinfo("Admissions"), width=27, height=3, font=('arial', 10, 'bold')
                            , bg='royal blue', fg='gold')
sidebar_Ebuttons.pack(padx=10, pady=10)

siderbar_Abuttons = tk.Button(sidebar, text='About us', command=lambda: messagebox.showinfo('About us')
                              , width=27, height=3, font=('arial', 10, 'bold'),
                              bg='royal blue', fg='gold')
siderbar_Abuttons.pack(padx=10, pady=10)

sidebar_tbuttons = tk.Button(sidebar, text='Topnotchers', command=lambda:
                            messagebox.showinfo("Topnotchers"), width=27, height=3, font=('arial', 10, 'bold')
                            , bg='royal blue', fg='gold')
sidebar_tbuttons.pack(padx=10, pady=10)


# Bottom bar for contact info
sidebar_lowbar = tk.Frame(sidebar, bg='royal blue', width=250, height=140)
sidebar_lowbar.pack(side='bottom', fill='x')
sidebar_lowbar.pack_propagate(False)

sidebar_contact = tk.Label(sidebar_lowbar, text='Contact us', bg='royal blue', fg='gold', font=('arial', 20, 'bold'))
sidebar_contact.pack(padx=10, pady=(10,0), anchor='w')

sidebar_1contact = tk.Label(sidebar_lowbar, text='Phone number: 09123456789', bg='royal blue', fg='gold', font=('arial', 10, 'bold'))
sidebar_1contact.pack(padx=10, pady=(5,10), anchor='w')

sidebar_2contact = tk.Label(sidebar_lowbar, text='Email: PerpetualHelp@Upshl.edu.ph', bg='royal blue', fg='gold', font=('arial', 10, 'bold'))
sidebar_2contact.place(x=10, y=77)

sidebar_place = tk.Label(sidebar_lowbar, text='Address: 123 pogi Sampaloc, Manila', bg='royal blue', fg='gold', font=('arial', 10, 'bold'))
sidebar_place.place(x=10, y=100)



#content
content = tk.Frame(window, bg='white')
content.pack(side='left', fill='both', expand=True)
icon = tk.PhotoImage(file='')

#header
header = tk.Frame(content, width=200, height=80, bg='royal blue')
header.pack(side='top', fill='x')

#logoname

# Logo name
name = tk.Label(header, text='PERPETUAL HELP COLLEGE OF MANILA', bg='royal blue', 
                fg='gold', font=('Arial', 35, 'bold'))
name.place(x=10, y=10)

# Real-time clock
clock_label = tk.Label(header, bg='gold', fg='red', font=('Arial', 30, 'bold'))
clock_label.place(x=1100, y=17)  # Adjust x as needed for your layout

def update_clock():
    import time
    current_time = time.strftime('%I:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

update_clock()


window.mainloop()   