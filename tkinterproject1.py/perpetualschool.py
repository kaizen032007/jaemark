import tkinter as tk 
import random
from tkinter import messagebox
import webbrowser


def open_gmail():
    webbrowser.open("https://mail.google.com/")

#GUI
window = tk.Tk()
window.geometry('500x500')

#fullscreen
 # 🟢 Make it zoomed
window.state('zoomed')

#sidebar
sidebar = tk.Frame(window, width=250, bg='gold')
sidebar.pack(side='left', fill='y')

#sidebar buttons


# Registration window function
from registration import open_registration_window
registration_btn = tk.Button(
    sidebar,
    text='Registration',
    command=lambda: open_registration_window(window),
    width=27, height=3,
    font=('arial', 10, 'bold'),
    bg='royal blue', fg='gold', cursor='hand2')
registration_btn.pack(padx=10, pady=10)

# Admissions window function
from Admission import open_Admissions_window
admissions_btn = tk.Button(
    sidebar,
    text='Admissions',
    command=lambda: open_Admissions_window(window),
    width=27, height=3,
    font=('arial', 10, 'bold'),
    bg='royal blue', fg='gold', cursor='hand2')
admissions_btn.pack(padx=10, pady=10)

# About us button
from Aboutus import open_aboutus_window
aboutus_btn = tk.Button(
    sidebar,
    text='About us',
    command=lambda: open_aboutus_window(window),
    width=27, height=3,
    font=('arial', 10, 'bold'),
    bg='royal blue', fg='gold', cursor='hand2')
aboutus_btn.pack(padx=10, pady=10)

# Reservations button
from Reservations import open_reservation_window
reservations_btn = tk.Button(
    sidebar,
    text='Reservations',
    command=lambda: open_reservation_window(window),
    width=27, height=3,
    font=('arial', 10, 'bold'),
    bg='royal blue', fg='gold', cursor='hand2')
reservations_btn.pack(padx=10, pady=10)


# Bottom bar for contact info
sidebar_lowbar = tk.Frame(sidebar, bg='royal blue', width=250, height=140)
sidebar_lowbar.pack(side='bottom', fill='x')
sidebar_lowbar.pack_propagate(False)


# Use a unique name for the separator to avoid overwriting the sidebar
sidebar_separator = tk.Frame(sidebar_lowbar, bg='gold', width=3, height=150)
sidebar_separator.pack(side='right', fill='x')

sidebar_contact = tk.Label(sidebar_lowbar, text='Contact us', bg='royal blue', fg='gold', font=('arial', 20, 'bold', 'underline'))
sidebar_contact.pack(padx=10, pady=(10,0), anchor='w')

# Phone number (two labels)
sidebar_1row = tk.Frame(sidebar_lowbar, bg='royal blue')
sidebar_1row.place(x=4, y=55)

tk.Label(sidebar_1row, text='Phone number: ', bg='royal blue', fg='white',
         font=('Arial', 10, 'bold', 'underline')).pack(side='left')

tk.Label(sidebar_1row, text='09123456789', bg='royal blue', fg='gold',
         font=('Arial', 10, 'bold', 'underline')).pack(side='left')


# Email
sidebar_2row = tk.Frame(sidebar_lowbar, bg='royal blue')
sidebar_2row.place(x=4, y=77)

tk.Label(sidebar_2row, text='Email: ', bg='royal blue', fg='white',
         font=('Arial', 10, 'bold', 'underline')).pack(side='left')

email_label = tk.Label(sidebar_2row, text='PerpetualHelp@Upshl.edu.ph', bg='royal blue', fg='gold',
         font=('Arial', 10, 'bold', 'underline'), cursor='hand2'
         )
email_label.pack(side='left')
email_label.bind("<Button-1>", lambda e: open_gmail())

# Address
sidebar_3row = tk.Frame(sidebar_lowbar, bg='royal blue')
sidebar_3row.place(x=4, y=100)

tk.Label(sidebar_3row, text='Address: ', bg='royal blue', fg='white',
         font=('Arial', 10, 'bold', 'underline')).pack(side='left')

tk.Label(sidebar_3row, text='123 pogi Sampaloc, Manila', bg='royal blue', fg='gold',
         font=('Arial', 10, 'bold', 'underline')).pack(side='left')

#icon
icon = tk.PhotoImage(file='perpetual.png')  # Add your icon file path here
window.iconphoto(False, icon)

#---------------------------------------#
#-----------MAIN CONTENT----------------#-------------------------------------------------------------------------------------------------------------
#---------------------------------------#

#content
content = tk.Frame(window, bg='white',)
content.pack(side='left', fill='both', expand=True)
photo = tk.PhotoImage(file='schoolbuilding.png')  # Add your image file path here
photo_label = tk.Label(content, image=photo, bg='sky blue')
photo_label.place(x=740, y=87)

#sample1
photo2 = tk.PhotoImage(file='sampleperps3.png')
photo_label = tk.Label(content, image=photo2, bg='sky blue')
photo_label.place(x=0, y=300)

#sample2
photo3 = tk.PhotoImage(file='sampleperps1.png')
photo_label = tk.Label(content, image=photo3, bg='sky blue')
photo_label.place(x=200, y=50)

#sample3 
photo4 = tk.PhotoImage(file='sampleperps4.png')
photo_label = tk.Label(content, image=photo4, bg='sky blue')
photo_label.place(x=0, y=50)

#sample4
photo5 = tk.PhotoImage(file='sampleperps5.png')
photo_label = tk.Label(content, image=photo5, bg='sky blue')
photo_label.place(x=204, y=304)

#enrollment photo
photo1 = tk.PhotoImage(file='perpsenroll.png')
photo_label = tk.Label(content, image=photo1, bg='sky blue')
photo_label.place(x=420, y=87)


# header (pack first so it stays on top)
header = tk.Frame(content, width=200, height=100, bg='royal blue')
header.pack(side='top', fill='x')

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

#-------------------------------------------------------------------------------------------------------------------------------------------------------

#content downbar
downbar = tk.Frame(content, bg='royal blue', width=100, height=340)
downbar.pack(side='bottom', fill='x')

list = tk.Label(downbar, text='LIST OF PROGRAMS OFFERED', font=('arial', 20, 'bold'), fg='blue', bg='gold')
list.place(x=20 ,y=10 )

#NURSING
programs1 = tk.Label(downbar, text='1. NURSING', font=('arial', 20, 'bold'), fg='blue', bg='gold')
programs1.place(x=40, y=70)
programs1 = tk.Button(downbar, text='CHECK TUITION',  font=('arial', 10, 'bold'), fg='blue', bg='white',cursor='hand2')
programs1.place(x=210, y=75)
#COMPUTER SCIENCE
programs2 = tk.Label(downbar, text='2. COMPUTER SCIENCE', font=('arial', 20, 'bold'), fg='blue', bg='gold',)
programs2.place(x=40, y=120)
programs2 = tk.Button(downbar, text='CHECK TUITION', font=('arial', 10, 'bold'), fg='blue', bg='white', cursor='hand2')
programs2.place(x=370, y=125)
#INFORMATION TECHNOLOGY
programs3 = tk.Label(downbar, text='3. INFORMATION TECHNOLOGY', font=('arial', 20, 'bold'), fg='blue', bg='gold',)
programs3.place(x=40, y=170)
programs3 = tk.Button(downbar, text='CHECK TUITION', font=('arial', 10, 'bold'), fg='blue', bg='white', cursor='hand2')
programs3.place(x=480, y=175)
#PHYSICAL THERAPY
programs4 = tk.Label(downbar, text='4. PHYSICAL THERAPY', font=('arial', 20, 'bold'), fg='blue', bg='gold',)
programs4.place(x=40, y=220)
programs4 = tk.Button(downbar, text='CHECK TUITION', font=('arial', 10, 'bold'), fg='blue', bg='white', cursor='hand2')
programs4.place(x=360, y=224)
#RADIOOGY TECHNOLOGY
programs5 = tk.Label(downbar, text='5. RADIOLOGY TECHNOLOGY', font=('arial', 20, 'bold'), fg='blue', bg='gold',)
programs5.place(x=40, y=270)
programs5 = tk.Button(downbar, text='CHECK TUITION', font=('arial', 10, 'bold'), fg='blue', bg='white', cursor='hand2')
programs5.place(x=450, y=274)

#2ND LIST

#BUSINESS ADMINISTRATION
programs6 = tk.Label(downbar, text='6. BUSINESS ADMINISTRATION', font=('arial', 20, 'bold'), fg='blue', bg='gold',)
programs6.place(x=700, y=70)
programs6 = tk.Button(downbar, text='CHECK TUITION', font=('arial', 10, 'bold'), fg='blue', bg='white', cursor='hand2')
programs6.place(x=1130, y=74)
#MEDICAL TECHNOLOGY
programs7 = tk.Label(downbar, text='7. MEDICAL TECHNOLOGY', font=('arial', 20, 'bold'), fg='blue', bg='gold',)
programs7.place(x=700, y=120)
programs7 = tk.Button(downbar, text='CHECK TUITION', font=('arial', 10, 'bold'), fg='blue', bg='white', cursor='hand2')
programs7.place(x=1070, y=125)
#CYBERSECURITY
programs8 = tk.Label(downbar, text='8 CYBERSECURITY', font=('arial', 20, 'bold'), fg='blue', bg='gold',)
programs8.place(x=700, y=170)
programs8 = tk.Button(downbar, text='CHECK TUITION', font=('arial', 10, 'bold'), fg='blue', bg='white', cursor='hand2')
programs8.place(x=975, y=175)
#ARCHITECTURE
programs9 = tk.Label(downbar, text='9 ARCHITECTURE', font=('arial', 20, 'bold'), fg='blue', bg='gold',)
programs9.place(x=700, y=220)
programs9 = tk.Button(downbar, text='CHECK TUITION', font=('arial', 10, 'bold'), fg='blue', bg='white', cursor='hand2')
programs9.place(x=955, y=225)
#MARINE TRANSPORTATION
programs0 = tk.Label(downbar, text='10. MARINE TRANSPORTATION', font=('arial', 20, 'bold'), fg='blue', bg='gold',)
programs0.place(x=700, y=270)
programs0 = tk.Button(downbar, text='CHECK TUITION', font=('arial', 10, 'bold'), fg='blue', bg='white', cursor='hand2')
programs0.place(x=1130, y=275)

#header

# Logo name
name = tk.Label(header, text='PERPETUAL HELP COLLEGE OF MANILA', bg='royal blue', 
                fg='gold', font=('Arial', 35, 'bold'))
name.place(x=10, y=10)


window.mainloop()   