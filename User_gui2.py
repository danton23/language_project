import tkinter
from tkinter import *
from tkinter import messagebox
from Germ_cats import *
from functools import partial
from TestGen import TestGenerator
from Span_cats import *
import random


root = tkinter.Tk()
root.geometry("500x500")
Masterlabel=Label(root, text="Please choose a Language to work on today!")
Masterlabel.pack(side=TOP)
var=IntVar()
var.set(1)
class Langwindow:
    wordslist=categories
    def make(self):
        Langroot=tkinter.Tk()
        Langroot.geometry("500x500")
        words=[]
        words+=Langwindow.wordslist
        print("this is words " + str(words))
        LangTest=TestGenerator()
        for word in words:
            Radiobutton=tkinter.Radiobutton(Langroot, text=word, command=lambda x=word: LangTest.Change(x))#you need a lambda to pass the particular WORD of the item being iterated over into the function as argument (otherwise it only does this AFTER all buttons created and passes LAST word in)
        #here HAD command=partial(Change)) and worked

            Radiobutton.pack(side=tkinter.LEFT)
    def test(self):
        print("working!")
#newwindow=Langwindow.create(self)
Spanwindow=Langwindow()
print(Spanwindow)
Spanwindow.test()
Spanwindow.wordslist=SpanCategories
print(Spanwindow.wordslist)
Russwindow=Langwindow()
Russwindow.test()
Germwindow=Langwindow()



#def Spanwindow():
#    Spanroot = tkinter.Tk()
 #   Spanroot.geometry("500x500")
w= Radiobutton(root, text ="German", variable=var,value=1, command=Germwindow.make)
w.pack(anchor=W)
w1 =Radiobutton(root, text ="Russian",variable=var, value=2, command=Russwindow.make)
w1.pack(anchor=W)
w3=Radiobutton(root, text ="Spanish", variable=var, value=3, command=Spanwindow.make)
w3.pack(anchor=W)
root.mainloop()
