import tkinter
from tkinter import *
from tkinter import messagebox
from Germ_cats import *
from functools import partial
root = tkinter.Tk()
root.geometry("500x500")
Masterlabel=Label(root, text="Please choose a Language to work on today!")
Masterlabel.pack(side=TOP)
var=IntVar()
var.set(1)
def Germwindow():
    root.destroy()
    Germroot = tkinter.Tk()
    Germroot.geometry("500x500")
    Windowlabel=Label(Germroot, text="Choose a Category")
    Windowlabel.pack()
    
    
    def Change(word):
             print(word)
             Germroot.destroy()
             Wordroot = tkinter.Tk()
             Wordroot.geometry("500x500")
             Windowlabel=Label(Wordroot, text=word)
             Windowlabel.pack()
    
    var=IntVar()
    var.set(0)
    button_identities = []
    words=[]
    words+=categories
  #  print(words)
    for word in words: 
         Radiobutton=tkinter.Radiobutton(Germroot, text=word, variable=var,value=1, command=partial(Change,word))
         Radiobutton.pack(side=tkinter.LEFT)
        # button_identities.append(button)
   # print(button_identities)   #print(item)
    #b=Radiobutton(Germroot, text=item)
    #    b.pack
        
        
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
def Fredcallback():
    msg=messagebox.showinfo("clicked!")
# fred=Button(root, text ="click me!", command = Fredcallback)
# fred.place(x=30,y=40)
root.mainloop()
