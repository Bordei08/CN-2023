from ex1 import ex1
from ex2 import verf_adunarea
from ex2 import verf_inmultirea
from ex3 import ex3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np





def intf_ex1():

    def get_answer_ex1():
     output_value.delete('1.0', END)
     output_value.insert(END, str(ex1()))

    ex1_intf = Tk()
    ex1_intf.title("Ex 1")
    ex1_intf.geometry("800x400")
    ex1_intf.config(bg="#f1e4d3")
    appName = Label(ex1_intf,text="Exercitiul 1",font = ("Comic Sans MS", 30, "bold"),fg="#5b7771", bg="#f1e4d3")
    appName.place(x=300, y=10)

    message ='''1.0 + u != 1.0
u > 0
u = pow(10,-m)
u = ?'''

    text_box = Text(
        ex1_intf,
       height=4,width=50,font=("arial",20),bd=5
    )
    text_box.pack(expand=True)
    text_box.insert('end', message)
    text_box.place(x = 15, y = 100)
    text_box.config(bg = "#5b7771", fg = "#402e20")
    solve_butto = Button(ex1_intf, text = "rezolva", bd = 5, command = get_answer_ex1)
    solve_butto.config(bg = "#5b7771",fg = "#402e20",font=("Comic Sans MS",20,"bold"), activebackground = "#bfb48d")
    solve_butto.place(x = 30, y = 250)

    output_value = Text(ex1_intf,height=1,width=15,font=("arial",20,"bold"),bd=5)
    output_value.config(bg = "#5b7771", fg = "#402e20")
    output_value.place(x = 200, y = 250)
    ex1_intf.mainloop()

def intf_ex2():

    def get_answer_ex2():
     output_value1.delete('1.0', END)
     output_value1.insert(END, str(verf_adunarea(1.0, ex1(), ex1())))
     output_value2.delete('1.0', END)
     output_value2.insert(END, str(verf_inmultirea()))


    ex2_intf = Tk()
    ex2_intf.title("Ex 3")
    ex2_intf.geometry("800x400")
    ex2_intf.config(bg="#f1e4d3")
    appName = Label(ex2_intf,text="Exercitiul 2",font = ("Comic Sans MS", 30, "bold"),fg="#5b7771", bg="#f1e4d3")
    appName.place(x=300, y=10)

   
    solve_butto = Button(ex2_intf, text = "rezolva", bd = 5, command = get_answer_ex2)
    solve_butto.config(bg = "#5b7771",fg = "#402e20",font=("Comic Sans MS",20,"bold"), activebackground = "#bfb48d")
    solve_butto.place(x = 330, y = 100)

    output_value1 = Text(ex2_intf,height=5,width=20,font=("arial",20,"bold"),bd=5)
    output_value1.config(bg = "#5b7771", fg = "#402e20")
    output_value1.place(x = 50, y = 200)
    output_value2 = Text(ex2_intf,height=5,width=20,font=("arial",20,"bold"),bd=5)
    output_value2.config(bg = "#5b7771", fg = "#402e20")
    output_value2.place(x = 450, y = 200)
    ex2_intf.mainloop()


def intf_ex3():
    def get_answer_ex3():
        A = np.random.randint(10, size=(int(input_A_n.get('1.0', END)), int(input_A_m.get('1.0',END))))
        B = np.random.randint(10, size=(int(input_B_n.get('1.0', END)), int(input_B_m.get('1.0',END))))  
        n_min = int(input_n_min.get('1.0', END))
        file = open("answer_ex3.txt", "w")
        file.write(str(ex3(A,B,n_min)))
        file.close()

    ex3_intf = Tk()
    ex3_intf.title("Ex 3")
    ex3_intf.geometry("800x400")
    ex3_intf.config(bg="#f1e4d3")
    appName = Label(ex3_intf,text="Exercitiul 3",font = ("Comic Sans MS", 30, "bold"),fg="#5b7771", bg="#f1e4d3")
    appName.place(x=300, y=10)

    input_n_min = Text(ex3_intf,height=1,width=10,font=("arial",20,"bold"),bd=5)
    input_n_min.config(bg = "#5b7771", fg = "#402e20")
    input_n_min.insert('end', "n_min")
    input_n_min.place(x=20, y=130)
    
    input_A_n = Text(ex3_intf,height=1,width=10,font=("arial",20,"bold"),bd=5)
    input_A_n.config(bg = "#5b7771", fg = "#402e20")
    input_A_n.insert('end', "A rows")
    input_A_n.place(x=20, y=200)

    input_A_m = Text(ex3_intf,height=1,width=10,font=("arial",20,"bold"),bd=5)
    input_A_m.config(bg = "#5b7771", fg = "#402e20")
    input_A_m.insert('end', "A cols")
    input_A_m.place(x=250, y=200)

    input_B_n = Text(ex3_intf,height=1,width=10,font=("arial",20,"bold"),bd=5)
    input_B_n.config(bg = "#5b7771", fg = "#402e20")
    input_B_n.insert('end', "B rows")
    input_B_n.place(x=20, y=270)

    input_B_m = Text(ex3_intf,height=1,width=10,font=("arial",20,"bold"),bd=5)
    input_B_m.config(bg = "#5b7771", fg = "#402e20")
    input_B_m.insert('end', "B cols")
    input_B_m.place(x=250, y=270)

    solve_butto = Button(ex3_intf, text = "rezolva", bd = 5, command = get_answer_ex3)
    solve_butto.config(bg = "#5b7771",fg = "#402e20",font=("Comic Sans MS",20,"bold"), activebackground = "#bfb48d")
    solve_butto.place(x = 20, y = 320)
    ex3_intf.mainloop()

def meniu():
    homework = Tk()
    homework.title("Tema 1 CN")
    homework.geometry("800x400")
    homework.config(bg="#f1e4d3")
    appName = Label(homework,text="Exericiti",font = ("Comic Sans MS", 30, "bold"),fg="#5b7771", bg="#f1e4d3")
    appName.place(x=300, y=10)

    ex1_button = Button(homework, text = "Exercitiul 1", bd = 5, command = intf_ex1 )
    ex1_button.config(bg = "#5b7771",fg = "#402e20",font=("Comic Sans MS",20,"bold"), activebackground = "#bfb48d")
    ex1_button.place(x = 290, y = 100)

    ex2_button = Button(homework, text = "Exercitiul 2", bd = 5, command = intf_ex2 )
    ex2_button.config(bg = "#5b7771",fg = "#402e20",font=("Comic Sans MS",20,"bold"), activebackground = "#bfb48d")
    ex2_button.place(x = 290, y = 200)

    ex3_button = Button(homework, text = "Exercitiul 3", bd = 5, command = intf_ex3 )
    ex3_button.config(bg = "#5b7771",fg = "#402e20",font=("Comic Sans MS",20,"bold"), activebackground = "#bfb48d")
    ex3_button.place(x = 290, y = 300)

    homework.mainloop()

meniu()    

