from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
from homework import main



def get_solution():
   
    main(int(str(input_n.get('1.0', END))), int(str(input_minim.get('1.0', END))), int(str(input_maxim.get('1.0', END))))
    

homework3_intf = Tk()
homework3_intf.title("Tema 3")
homework3_intf.geometry("800x400")
homework3_intf.config(bg="#f1e4d3")
appName = Label(homework3_intf,text="Homework 3",font = ("Comic Sans MS", 30, "bold"),fg="#5b7771", bg="#f1e4d3")
appName.place(x=300, y=10)

input_n = Text(homework3_intf,height=1,width=10,font=("arial",20,"bold"),bd=5)
input_n.config(bg = "#5b7771", fg = "#402e20")
input_n.insert('end', "N")
input_n.place(x=20, y=130)
    
input_minim = Text(homework3_intf,height=1,width=10,font=("arial",20,"bold"),bd=5)
input_minim.config(bg = "#5b7771", fg = "#402e20")
input_minim.insert('end', "Minim")
input_minim.place(x=20, y=200)

input_maxim = Text(homework3_intf,height=1,width=10,font=("arial",20,"bold"),bd=5)
input_maxim.config(bg = "#5b7771", fg = "#402e20")
input_maxim.insert('end', "Maxim")
input_maxim.place(x=250, y=200)


solve_butto = Button(homework3_intf, text = "rezolva", bd = 5, command = get_solution)
solve_butto.config(bg = "#5b7771",fg = "#402e20",font=("Comic Sans MS",20,"bold"), activebackground = "#bfb48d")
solve_butto.place(x = 20, y = 320)
homework3_intf.mainloop()