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
    root.destroy()
    Germroot = tkinter.Tk()
    Germroot.geometry("500x500")
    Windowlabel=Label(Germroot, text="Choose a Category")
    Windowlabel.pack()
    genkey="blank"
    def Change(genkey):
             try:
               Germroot.destroy() # (here may need to define another func to put exept inside)
             except:
                pass
             Wordroot = tkinter.Tk()
             Wordroot.geometry("500x500")
             Windowlabel=Label(Wordroot, text=word)
             Windowlabel.pack()
             print(word)
             #isfirsttime=int()
             for item in categories:
                 tempdict=categories.get(item)
             
            
                                    
           
           #  gkey=str(firsttime())
            # print(gkey)
             
            
             if(genkey=="blank"):
                genkey=random.choice(list(tempdict))
                print("genkey is "+genkey+ "...first time round!")
                
             else:
                 pass
                 print("passing!")

             Germlabel=Label(Wordroot, text="How do you say " + genkey + " in English?")
             Germlabel.pack()
             def checkinput(name):    #had variable (name) before
                        name=e1.get()
                        print(name)
                         # print(name)
                          #stres=e1.get(name)
                          #result=str(stres)
                          #check=name.get()
                          # print(check)
                        #  result=str(e1.get(name))
                        #  print(result)
                       #   newresult=result.replace('\r', '')
                        #  print(newresult)

                     # print(categories.get(key))
                          #print(categories)
                        for k, v in categories[word].items():
                                 if k == genkey:
                                   if name==v:
                                              print ("correct" + v)
                                              genkey=gennewkey()
                                              print("new key is " + genkey)
                                              Wordroot.destroy()
                                              Change(genkey)
                                              
                                   elif name!=v:
                                              print("booo!" + v)

                                   else:
                                           break
             name=StringVar()
             e1 = Entry(Wordroot, textvariable=name)
             e1.bind("<Return>",checkinput)
             e1.pack()
             def gennewkey():
                       print("###running gennewkey#####")
                       print("at this point current key is " + genkey)
                       newkey=random.choice(list(tempdict))
                       print("new generated key =" + newkey + " #####")
                       if newkey!=genkey:
                             genkey=newkey
                             print("at this point, decided that newkey!=key, so key is assigned to " + genkey)
                             return genkey
                       elif newkey==genkey:
                             print("decided that newkey == current key so function SHoULD run again ###")
                             gennewkey(genkey)
         #   def generator():
                         
                           #  newkey=random.choice(list(tempdict))
             
            
    
             var=IntVar()
             var.set(0)
             button_identities = []
             words=[]
             words+=categories
             for word in words: 
                             Radiobutton=tkinter.Radiobutton(Germroot, text=word, variable=var,value=1, command=(Change(genkey)))   #here HAD command=partial(Change)) and worked
                             Radiobutton.pack(side=tkinter.LEFT) 
    
             
                                  
    

  #  for item in categories:
   #              if word == item:
     #                 tempdict = categories.get(item)
    #                  key=random.choice(list(tempdict))
      #                return key
  #  print(words)
    
    
    
    
                                                                                 
                         #     if k == key:
                           #       print(k)
                           #   else:
                         #         print("aoatoato")
                      #    if newresult == categories[key]:
                     #         print("Correct")
                     #     else:
                      #        print("incorrect")
                          
           
                      
        
          
    
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
