# importing the library modules 
import time 
from tkinter import *

# global variable declaration 
expression = ""
governer = 0
height = 0 
weight = 0 
 
# function to create the algebric expression 
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
 
 
# function to evaluate the algebric expression 
def equalpress():

    if governer == 1:
        print('processing the bmi data ')
        global height
        global weight
        h_in_meters =float(height * 0.3048)
        print('weight in kg',weight)
        print('height in feet',height)
        print('height in meters',h_in_meters)
        body_mass_index = float(weight/(h_in_meters*h_in_meters))
        print(body_mass_index)
        equation.set("body mass index is ")
        gui.update()
        time.sleep(1.100)
        equation.set("")
        equation.set(body_mass_index)

    else:
        try:
            global expression
            total = str(eval(expression))
            equation.set(total)
            expression = ""
        except:
            equation.set(" error ")
            expression = ""
 
# function to cleare the console window 
def clear():
    global expression
    expression = ""
    equation.set("")

# function to activate the bmi mode 
def bmi():
    global governer
    if governer == 0:
        governer = 1
        equation.set("bmi mode started")
        gui.update()
        time.sleep(1)
        equation.set("")
        gui.update()
        gui.geometry('202x300')
        gui.update()
       
    else :
        governer = 0
        equation.set("bmi mode turning off")
        gui.update()
        time.sleep(1)
        equation.set("")
        gui.update()
        gui.geometry('202x160')
        gui.update() 

# function to get the height data from the console and stores it in the global variable 
def get_bmi_H():
     global expression
     global height
     height = expression
     height = float(height)
     t.delete("1.0", END)
     t.insert(END,str(expression))
     gui.update()

# function to get the weight data from the console and stores it in the global variable 
def get_bmi_W():
     global expression
     global weight
     weight = expression
     weight = float(weight)
     t1.delete("1.0", END)
     t1.insert(END,str(expression))
     gui.update()

#----main code starts from here-------------------------------------
if __name__ == "__main__":

# creating main tkinter window and named it as the gui of dimension as 202x160
    gui = Tk()
    gui.configure(background="black")
    gui.title("Python Calcy")
    gui.geometry("202x160")
    equation = StringVar()

# creating the widgets 
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4,ipadx=40,ipady=5)

    button1 = Button(gui, text=' 1 ', fg='white', bg='red',
                    command=lambda: press(1), height=1, width=5)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='white', bg='red',
                    command=lambda: press(2), height=1, width=5)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='white', bg='red',
                    command=lambda: press(3), height=1, width=5)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='white', bg='red',
                    command=lambda: press(4), height=1, width=5)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='white', bg='red',
                    command=lambda: press(5), height=1, width=5)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='white', bg='red',
                    command=lambda: press(6), height=1, width=5)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='white', bg='red',
                    command=lambda: press(7), height=1, width=5)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='white', bg='red',
                    command=lambda: press(8), height=1, width=5)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='white', bg='red',
                    command=lambda: press(9), height=1, width=5)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='white', bg='red',
                    command=lambda: press(0), height=1, width=5)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='white', bg='red',
                command=lambda: press("+"), height=1, width=5)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='white', bg='red',
                command=lambda: press("-"), height=1, width=5)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='white', bg='red',
                    command=lambda: press("*"), height=1, width=5)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='white', bg='red',
                    command=lambda: press("/"), height=1, width=5)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='white', bg='red',
                command=equalpress, height=1, width=5)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='white', bg='red',
                command=clear, height=1, width=5)
    clear.grid(row=5, column='1')
 
    Decimal= Button(gui, text='.', fg='white', bg='red',
                    command=lambda: press('.'), height=1, width=5)
    Decimal.grid(row=6, column=0)

    stop=Button(gui,text='stop',command=gui.destroy,activebackground='red',height=1, width=5,fg='red')
    stop.grid(row=6,column=1)

    bmi=Button(gui,text='bmi',command=bmi,activebackground='red',height=1, width=5,fg='red')
    bmi.grid(row=6,column=2)

    buttH = Button(gui, text='H', fg='white', bg='red',
                    command=get_bmi_H, height=1, width=5)
    buttH.grid(row=7, column=0)

    t=Text(gui,height = 1, width = 5,background='white')
    t.grid(row=7,column=1) 

    buttW = Button(gui, text='W', fg='white', bg='red',
                command=get_bmi_W, height=1, width=5)
    buttW.grid(row=7, column=2)

    t1=Text(gui,height = 1, width = 5,background='white')
    t1.grid(row=7,column=3)
   
    print('gui started ')
    equation.set("python gui based calculator")
    gui.update()
    time.sleep(2)
    equation.set("a project by shubham khangar")
    gui.update()
    time.sleep(0.5)
    equation.set("a project by shubham khangar")
    gui.update()
    time.sleep(0.5)
    equation.set("")
    gui.update()

    gui.mainloop()
