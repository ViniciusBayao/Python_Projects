# Starting to import tkinter packages will need further
import customtkinter, tkinter.font, tkinter as tk
from tkinter import *

# Declaring expression variable

expression = "" 
 
# Function to update expression 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
 
    # concatenation of string 
    expression = expression + str(num) 
 
    # update the expression by using set method 
    equation.set(expression) 
 
 
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
 
    # Put that code inside the try block 
    # which may generate the error 
    try: 
 
        global expression 
 
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
 
        equation.set(total) 
 
        # initialize the expression variable 
        # by empty string 
        expression = "" 
 
    # if error is generate then handle 
    # by the except block 
    except: 
 
        equation.set(" error ") 
        expression = "" 
 
 
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
 
 
# Driver code 
if __name__ == "__main__":

    # Creating the GUI using Custom Tk

    gui = customtkinter.CTk()

    # Changing the icon of Custom Tk window

    gui.iconbitmap("171352_calculator_icon.ico")

    # Setting the background color of Custom Tk Window

    gui.configure(bg="ccc")

    # Setting the size of window

    gui.geometry("360x810")

    # Declaring StringVar and putting into equation

    equation = StringVar() 

    # Declaring the title of the Window project

    gui.title("My Calculator")

    # Option to not allow user resize the Window original size on x and y.

    gui.resizable(False, False)

    # Setting the font of numbers that will be shown inside the text box

    Desired_font = tk.font.Font(family= "sans-serif",  size= 21,  weight= "bold")

    # declaring the Entry of expression field and setting first attributes

    expression_field = Entry(gui, textvariable=equation, highlightthickness=2)

    # Setting the grid attributes

    expression_field.grid(columnspan=10, ipadx=5 , ipady=40, padx= 10, pady= 20)

    # Setting the configurations of expression field

    expression_field.configure(font= Desired_font, fg="white", disabledforeground="white", justify='center', bg="#3d3d3d", disabledbackground="#3d3d3d", highlightcolor="#1c1c1c", highlightbackground="#1c1c1c")

    expression_field.configure(state='disabled')

    #calculator buttons with configs and calling respective previous functions to execute proper actions

    button1 = customtkinter.CTkButton(gui, text='1', width=80, height= 70, command= lambda: press(1))
    button1.grid(row=2, column=0, ipadx= 10, padx=10, pady= 20)
    button2 = customtkinter.CTkButton(gui, text='2', width=80, height= 70, command= lambda: press(2))
    button2.grid(row=2, column=1, ipadx=10, padx=10, pady= 20)
    button3 = customtkinter.CTkButton(gui, text='3', width=80, height= 70, command= lambda: press(3))
    button3.grid(row=2, column=2, ipadx=10, padx=10, pady= 20)
    button4 = customtkinter.CTkButton(gui, text='4', width=80, height= 70, command= lambda: press(4))
    button4.grid(row=3, column=0, ipadx= 10, padx=10, pady= 20)
    button5 = customtkinter.CTkButton(gui, text='5', width=80, height= 70, command= lambda: press(5))
    button5.grid(row=3, column=1, ipadx= 10, padx=10, pady= 20)
    button6 = customtkinter.CTkButton(gui, text='6', width=80, height= 70, command= lambda: press(6))
    button6.grid(row=3, column=2, ipadx= 10, padx=10, pady= 20)
    button7 = customtkinter.CTkButton(gui, text='7', width=80, height= 70, command= lambda: press(7))
    button7.grid(row=4, column=0, ipadx= 10, padx=10, pady= 20)
    button8 = customtkinter.CTkButton(gui, text='8', width=80, height= 70, command= lambda: press(8))
    button8.grid(row=4, column=1, ipadx=10, padx=10, pady= 20)
    button9 = customtkinter.CTkButton(gui, text='9', width=80, height= 70, command= lambda: press(9))
    button9.grid(row=4, column=2, ipadx=10, padx=10, pady= 20)
    button_plus = customtkinter.CTkButton(gui, text='+', width=80, height= 70, command= lambda: press("+"))
    button_plus.grid(row=5, column=0, ipadx=10, padx=10, pady= 20)
    button0 = customtkinter.CTkButton(gui, text='0', width=80, height= 70, command= lambda: press(0))
    button0.grid(row=5, column=1, ipadx=10, padx=10, pady= 20)
    button_minus = customtkinter.CTkButton(gui, text='-', width=80, height= 70, command= lambda: press("-"))
    button_minus.grid(row=5, column=2, ipadx=10, padx=10, pady= 20)
    button_clear = customtkinter.CTkButton(gui, text='Clear', width=80, height= 70, command= clear)
    button_clear.grid(row=7, column=1, ipadx=10, padx=10, pady= 20)
    button_divide= customtkinter.CTkButton(gui, text='/', width=80, height= 70, command= lambda: press("/"))
    button_divide.grid(row=6, column=0, ipadx=10, padx=10, pady= 20)
    button_multiply = customtkinter.CTkButton(gui, text='*', width=80, height= 70, command= lambda: press("*"))
    button_multiply.grid(row=6, column=1, ipadx=10, padx=10, pady= 20)
    button_equal = customtkinter.CTkButton(gui, text='=', width=80, height= 70, command= equalpress)
    button_equal.grid(row=6, column=2, ipadx=10, padx=10, pady= 20)

# Declaring the mainloop which makes the window remains open until someone close it.

gui.mainloop()

# Project used as a reference and basis for building the application: https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
