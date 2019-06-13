import tkinter
import random
from Germ_cats import *
from tkinter import *
class TestGenerator:
    file="times.txt"
    
    def hoola(self ):
        print("hoola!")
    def Change(self, x):
        
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
              def checkinput(self):
                  file=TestGenerator.file
                  name=e1.get()  
                  for k, v in testcats.items():
                      if k ==key:
                         targetval=v
                         
    
                  with open (file, "r") as f:
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
                                              TestGenerator.Change(self,x)
                                                 
                      elif name!=targetval:
                                              with open (file,"w")as f:
                                                    f.write(str(numbcontents))
                                              with open ("times.txt", "r") as f:
                                                    contents=f.read()
                                                    print("this is new contents "+ contents)
                                              print ("try again!")
                                              
                  else:
                      
                      if v[0:2]=="to":
                           
                           
                           print("to " + v[3:6] + " here are the first three letters of the word!")
                           with open(file, "w") as f:
                                f.write("1")
                          
                      else:
                                print(targetval + "this is value")
                                print(targetval[:3] + " here are the first three letters of the word! ")
                                with open(file, "w") as f:
                                  f.write("1")
                          
                  
              e1.bind("<Return>",checkinput)
              e1.pack()
