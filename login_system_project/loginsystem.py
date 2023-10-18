# importing tkinter, Custom tkinter and tkinter.messagebox

from tkinter import *
import tkinter as tk
import customtkinter
from tkinter.messagebox import showinfo

# Setting appearance mode to dark

customtkinter.set_appearance_mode("Dark")

# The only valid E-mail and password 

mail_regist = "adm20@gmail.com"
password_regist = "123456789!"

# Function to verify if e-mail and password match after user input the values

def usr_verification(enter_mail, enter_password):
    mail = enter_mail
    password = enter_password
    if password == '123456789!' and mail == 'adm12@gmail.com':
        showinfo('ADMIN', 'Welcome ADM!')
    else:
        showinfo('Wrong Credentials', 'Sorry, you are not allowed.')

# Starting the GUI creation process of Tk and setting the basic configs

gui = customtkinter.CTk()

gui.geometry('500x250')

gui.title('Login System')

gui.configure(bg='#1b1c29')

# Does not allow the user to resize the window

gui.resizable(False, False)

Desired_font1 = tk.font.Font(family= "sans-serif",  size= 14,  weight= "bold")
Desired_font2 = tk.font.Font(family= "sans-serif",  size= 14)

# Placing the icon

gui.iconbitmap("Eye_37136.ico")

# Starting to instantiate and configure email and password entries and labels.

ln = Label(gui, text="E-mail: ")
ln.grid(row=2, column=0, ipady=20, padx= 20)
ln.configure(font= Desired_font1, bg='#242424', fg='#c2c4d1')

en = Entry(gui, bd=5)
en.grid(row=2, column=1, ipadx=20)
en.configure(font= Desired_font2 ,bg='#e8f2fa', highlightcolor="#1c1c1c", highlightbackground="#1c1c1c")

lw = Label(gui, text="Password: ")
lw.grid(row=3, column=0, ipady= 20, padx=20)
lw.configure(font= Desired_font1, bg='#242424', fg='#c2c4d1')

ew = Entry(gui, show="*", bd=5)
ew.grid(row=3, column=1, ipadx=20)
ew.configure(font= Desired_font2, bg='#e8f2fa', highlightthickness=1, highlightcolor="#1c1c1c", highlightbackground="#1c1c1c")

# Setting the button so that, when clicking on it, the email and password data are sent to the function, thus validating or not the user admin (admin)

btn = Button(gui, text="Login", command=lambda: usr_verification(en.get(), ew.get()))
btn.grid(row=4, column=1, padx= 20, ipadx=30, ipady=10, pady= 20)
btn.configure(font= Desired_font1, bg='#05070a', fg='#7989a3', highlightcolor="#1c1c1c", highlightbackground="#1c1c1c", cursor="hand2", activebackground='#1c2430')

gui.mainloop()
