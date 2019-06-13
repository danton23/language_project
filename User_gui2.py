import tkinter
from tkinter import *
from tkinter import messagebox
from Germ_cats import *
from functools import partial
from TestGen import TestGenerator
import random


root = tkinter.Tk()
root.geometry("500x500")
Masterlabel=Label(root, text="Please choose a Language to work on today!")
Masterlabel.pack(side=TOP)
var=IntVar()
var.set(1)
def Germwindow():
    Germroot=tkinter.Tk()
    Germroot.geometry("500x500")
    var=IntVar()
    var.set(0)
    button_identities = []
    words=[]
    words+=categories
    print("this is words " + str(words))
    GermTest=TestGenerator()
    print(GermTest)
    GermTest.hoola
    
    
              
    for word in words:
                    
                     Radiobutton=tkinter.Radiobutton(Germroot, text=word, command=lambda x=word: GermTest.Change( x) )   #you need a lambda to pass the particular WORD of the item being iterated over into the function as argument (otherwise it only does this AFTER all buttons created and passes LAST word in)
        #here HAD command=partial(Change)) and worked
                     
                     Radiobutton.pack(side=tkinter.LEFT) 
def Russwindow():
    Rusroot = tkinter.Tk()
    Rusroot.geometry("500x500")
def Spanwindow():
    Spanroot = tkinter.Tk()
    Spanroot.geometry("500x500")
w= Radiobutton(root, text ="German", variable=var,value=1, command=Germwindow)
w.pack(anchor=W)
w1 =Radiobutton(root, text ="Russian",variable=var, value=2, command=Russwindow)
w1.pack(anchor=W)
w3=Radiobutton(root, text ="Spanish", variable=var, value=3, command=Spanwindow)
w3.pack(anchor=W)
root.mainloop()
