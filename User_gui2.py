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
Rootvar=IntVar()
Rootvar.set(1)
print("this is SpanCategories " + str(SpanCategories))
class Langwindow:
    def __init__(self, wordslist):
        
         self.wordslist=wordlist
    butvar=IntVar()
    butvar.set(99)
    def __init__(self):
       
       self.ident=""
    
    def make(self):
        Langroot=Toplevel(root)
        
        Langroot.geometry("500x500")
        words=[]
        words+=self.wordslist
        print("this is words " + str(words))
        LangTest=TestGenerator(self.wordslist)
        print("this is LangTest.vocab " + str(LangTest.vocab))
        LangTest.hoola()
 #      LangTest.parent=Langroot
        self.radVar=IntVar()
        self.radVar.set(99)
        
        buttonlist=[]
        list=[]
        iterlist=0
        
       

        
                         

        var=IntVar()
        var.set(99)
        values=[0,1,2]

        for word in words:
            
            #list+=1 #use this to create values for the radiobutton value (determines if is on or off) this works!!
     #       print("this is current list value "+str(list)) + "this is current var "+str(var.get())
            iterlist+=1
            print(list)
            Radiobutton=tkinter.Radiobutton(Langroot, text=word,value=iterlist, variable=var,command=lambda self=self,  x=word: LangTest.Change(self,x)) #vocab=words
            buttonlist.append(Radiobutton)
            #you need a lambda to pass the particular WORD of the item being iterated over into the function as argument (otherwise it only does this AFTER all buttons created and passes LAST word in)
        #here HAD command=partial(Change)) and worked 
            if list == 0:Radiobutton.select()
            Radiobutton.pack(side=tkinter.LEFT)
    def test(self):
        print("working!")
#newwindow=Langwindow.create(self)
Spanwindow=Langwindow()
Spanwindow.wordslist=SpanCategories
print(Spanwindow.wordslist)
Russwindow=Langwindow()
Russwindow.wordslist=categories
Russwindow.ident=Russwindow
Russwindow.test()
Germwindow=Langwindow()
Germwindow.wordslist=categories



#def Spanwindow():
#    Spanroot = tkinter.Tk()
 #   Spanroot.geometry("500x500")
w= Radiobutton(root, text ="German", variable=Rootvar,value=1, command=Germwindow.make)
w.pack(anchor=W)
w1 =Radiobutton(root, text ="Russian",variable=Rootvar, value=2, command=Russwindow.make)
w1.pack(anchor=W)
w3=Radiobutton(root, text ="Spanish", variable=Rootvar, value=3, command=Spanwindow.make)
w3.pack(anchor=W)
root.mainloop()
