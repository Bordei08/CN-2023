from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import homework 



def solve_homework():

    flag, res = homework.use_case_1()
    output_usecase1_value1.delete('1.0', END)
    output_usecase1_value1.insert(END,str(flag))
    output_usecase1_value2.delete('1.0', END)
    output_usecase1_value2.insert(END,str(res))   

    flag, res = homework.use_case_2()
    output_usecase2_value1.delete('1.0', END)
    output_usecase2_value1.insert(END,str(flag))
    output_usecase2_value2.delete('1.0', END)
    output_usecase2_value2.insert(END,str(res))  

    flag, res = homework.use_case_3()
    output_usecase3_value1.delete('1.0', END)
    output_usecase3_value1.insert(END,str(flag))
    output_usecase3_value2.delete('1.0', END)
    output_usecase3_value2.insert(END,str(res))  

    flag, res = homework.use_case_4()
    output_usecase4_value1.delete('1.0', END)
    output_usecase4_value1.insert(END,str(flag))
    output_usecase4_value2.delete('1.0', END)
    output_usecase4_value2.insert(END,str(res)) 

    flag, res = homework.use_case_5()
    output_usecase5_value1.delete('1.0', END)
    output_usecase5_value1.insert(END,str(flag))
    output_usecase5_value2.delete('1.0', END)
    output_usecase5_value2.insert(END,str(res)) 

def get_solve_bonus():
    flag = homework.solve_bonus()
    output_bonus_value1.delete('1.0', END)
    output_bonus_value1.insert(END, str(flag))    

homework4_intf = Tk()
homework4_intf.title("Tema 4")
homework4_intf.geometry("1400x1000")
homework4_intf.config(bg="#f1e4d3")
appName = Label(homework4_intf,text="Homework 4",font = ("Comic Sans MS", 30, "bold"),fg="#5b7771", bg="#f1e4d3")
appName.place(x=500, y=10)


use_case_1 = Label(homework4_intf,text="Cazul 1 cu a1.txt si b1.txt",font = ("Comic Sans MS", 25, "bold"),fg="#5b7771", bg="#f1e4d3")
use_case_1.place(x=20, y=100)
    
output_usecase1_value1 = Text(homework4_intf,height=1,width=20,font=("arial",20,"bold"),bd=5)
output_usecase1_value1.config(bg = "#5b7771", fg = "#402e20")
output_usecase1_value1.place(x = 35, y = 170)

output_usecase1_value2 = Text(homework4_intf,height=1,width=25,font=("arial",20,"bold"),bd=5)
output_usecase1_value2.config(bg = "#5b7771", fg = "#402e20")
output_usecase1_value2.place(x = 500, y = 170)


use_case_2 = Label(homework4_intf,text="Cazul 2 cu a2.txt si b2.txt",font = ("Comic Sans MS", 25, "bold"),fg="#5b7771", bg="#f1e4d3")
use_case_2.place(x=20, y=230)
    
output_usecase2_value1 = Text(homework4_intf,height=1,width=20,font=("arial",20,"bold"),bd=5)
output_usecase2_value1.config(bg = "#5b7771", fg = "#402e20")
output_usecase2_value1.place(x = 35, y = 300)

output_usecase2_value2 = Text(homework4_intf,height=1,width=25,font=("arial",20,"bold"),bd=5)
output_usecase2_value2.config(bg = "#5b7771", fg = "#402e20")
output_usecase2_value2.place(x = 500, y = 300)

use_case_3 = Label(homework4_intf,text="Cazul 3 cu a3.txt si b3.txt",font = ("Comic Sans MS", 25, "bold"),fg="#5b7771", bg="#f1e4d3")
use_case_3.place(x=20, y=360)
    
output_usecase3_value1 = Text(homework4_intf,height=1,width=20,font=("arial",20,"bold"),bd=5)
output_usecase3_value1.config(bg = "#5b7771", fg = "#402e20")
output_usecase3_value1.place(x = 35, y = 430)

output_usecase3_value2 = Text(homework4_intf,height=1,width=25,font=("arial",20,"bold"),bd=5)
output_usecase3_value2.config(bg = "#5b7771", fg = "#402e20")
output_usecase3_value2.place(x = 500, y = 430)

use_case_4 = Label(homework4_intf,text="Cazul 4 cu a4.txt si b4.txt",font = ("Comic Sans MS", 25, "bold"),fg="#5b7771", bg="#f1e4d3")
use_case_4.place(x=20, y=490)
    
output_usecase4_value1 = Text(homework4_intf,height=1,width=20,font=("arial",20,"bold"),bd=5)
output_usecase4_value1.config(bg = "#5b7771", fg = "#402e20")
output_usecase4_value1.place(x = 35, y = 550)

output_usecase4_value2 = Text(homework4_intf,height=1,width=25,font=("arial",20,"bold"),bd=5)
output_usecase4_value2.config(bg = "#5b7771", fg = "#402e20")
output_usecase4_value2.place(x = 500, y = 550)

use_case_5 = Label(homework4_intf,text="Cazul 5 cu a5.txt si b5.txt",font = ("Comic Sans MS", 25, "bold"),fg="#5b7771", bg="#f1e4d3")
use_case_5.place(x=20, y=610)
    
output_usecase5_value1 = Text(homework4_intf,height=1,width=20,font=("arial",20,"bold"),bd=5)
output_usecase5_value1.config(bg = "#5b7771", fg = "#402e20")
output_usecase5_value1.place(x = 35, y = 670)

output_usecase5_value2 = Text(homework4_intf,height=1,width=25,font=("arial",20,"bold"),bd=5)
output_usecase5_value2.config(bg = "#5b7771", fg = "#402e20")
output_usecase5_value2.place(x = 500, y = 670)


solve_butto = Button(homework4_intf, text = "rezolva", bd = 5, command = solve_homework )
solve_butto.config(bg = "#5b7771",fg = "#402e20",font=("Comic Sans MS",20,"bold"), activebackground = "#bfb48d")
solve_butto.place(x = 600, y = 720)

bonus = Label(homework4_intf,text="Bonus",font = ("Comic Sans MS", 25, "bold"),fg="#5b7771", bg="#f1e4d3")
bonus.place(x=1000, y=100)
bonus = Label(homework4_intf,text="A + B == aplusb.txt",font = ("Comic Sans MS", 25, "bold"),fg="#5b7771", bg="#f1e4d3")
bonus.place(x=1000, y=170)

output_bonus_value1 = Text(homework4_intf,height=1,width=20,font=("arial",20,"bold"),bd=5)
output_bonus_value1.config(bg = "#5b7771", fg = "#402e20")
output_bonus_value1.place(x = 1000, y = 230)

solve_bonus_butto = Button(homework4_intf, text = "rezolva", bd = 5, command = get_solve_bonus )
solve_bonus_butto.config(bg = "#5b7771",fg = "#402e20",font=("Comic Sans MS",20,"bold"), activebackground = "#bfb48d")
solve_bonus_butto.place(x = 1000, y = 290)




homework4_intf.mainloop()