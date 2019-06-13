import tkinter
from tkinter import *
from tkinter import messagebox
from Germ_cats import *
from functools import partial
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
    print(words)
    def Change(x):
              Wordroot = tkinter.Tk()
              Wordroot.geometry("500x500")
              Windowlabel=Label(Wordroot, text=x)
              Windowlabel.pack()
              name=StringVar()
              def genlist():
                 for key, value in categories.items():
                   if key == x:
                     print ("this is "+ key)
                     print ("this is categories [x]")
                     print(categories[x])
                     testcats=categories[x]   #here we are splitting the categories dict into only the part that conforms to the original category the user selected (i.e abstract, verbs etc)
                     return testcats
                
              testcats=genlist()
              def genkey():
                  key=random.choice(list(testcats))
                  Germlabel=Label(Wordroot, text="How do you say " + key + " in English?")
                  Germlabel.pack()
                  return key
              key=genkey()
              
             
              e1 = Entry(Wordroot, textvariable=name)
              def checkinput(name):
                  
                  name=e1.get()  
                  for k, v in testcats.items():
                      if k ==key:
                         targetval=v
                         
    
                  with open ("times.txt", "r") as f:
                          contents=f.read()
                          print (contents)
                  numbcontents=int(contents)
                  print("this is target value " + targetval)
                  print(name)
                  if numbcontents<=5:
                      print("less")
                      numbcontents+=1
                      print("this is newnumb " + str(numbcontents))
                      
                      if name==targetval:
                                              print("well done!")
                                              Wordroot.destroy()
                                              Change(x)
                                                 
                      elif name!=targetval:
                                              with open ("times.txt","w")as f:
                                                    f.write(str(numbcontents))
                                              with open ("times.txt", "r") as f:
                                                    contents=f.read()
                                                    print("this is new contents "+ contents)
                                              print ("try again!")
                                              
                  else:
                      if v[:3]=="to ":
                          
                           print("to " + v[4-6] + " here are the first three letters of the word!")
                           with open("times.txt", "w") as f:
                                f.write("1")
                          
                      else:
                                print(v[:3] + " here are the first three letters of the word! ")
                                with open("times.txt", "w") as f:
                                  f.write("1")
                          
                  
              e1.bind("<Return>",checkinput)
              e1.pack()
              
    for word in words:
                    
                     Radiobutton=tkinter.Radiobutton(Germroot, text=word, command=lambda x=word: Change(x))   #you need a lambda to pass the particular WORD of the item being iterated over into the function as argument (otherwise it only does this AFTER all buttons created and passes LAST word in)
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
