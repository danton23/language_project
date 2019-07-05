import tkinter
import random
from Germ_cats import *
# from Spanish_cats import *
from tkinter import *
import json
class TestGenerator:
    file="times.txt"
    def __init__(self, vocab):
       
        self.vocab=vocab

     

#    def __init__(self,parent):
        
  #      Wordroot = Frame(parent)
 #       Wordroot.pack()
 #       print("this is parent " + str(parent))
    
    
    
    def hoola(self ):
        print("hoola!")
        print("this is self.vocab " +str(self.vocab))
        print("this is "+ str(self.vocab))
        print ("Здравствуй, мир!")
    
    def Change(event,self,x):

              print("this is self.wordslist"  + str(self.wordslist))
              
              print("this is event " + str(event))
              print(event)
              print("this is self " +str(self))
              print(self)
              print("this is X " + str(x))
              print(x)

              
                     #json.dump(data, f, indent=2)
                         
                     
              
            #  Windowlabel=Label(Wordroot, text=x)
             # Windowlabel.pack()
              name=StringVar()
        #      def action(self):
       #           print("destroyed")
      #            Langwindow.destroy()
     #         Wordroot.bind("<Destroy>", action)
              
             
              def genlist(formattedwords):
                 for key, value in formattedwords:
                   if key == x:
                     print ("this is "+ key)
                     print ("this is categories [x]")
                     #print(categories[x])
                     print("this is self.wordslist[x]"+ str(self.wordslist[x]))
                     if self.wordslist[x]=={}:
                         print("you must add words")
                         return
                    
                     testcats=self.wordslist[x]   #here we are splitting the categories dict into only the part that conforms to the original category the user selected (i.e abstract, verbs etc)
                     return testcats
              
              
              formattedwords=self.wordslist.items()
              print("this is formattedwords " + str(formattedwords))
              testcats=genlist(formattedwords)
             
              def genkey():
                  print("this is " + str(testcats))
                  
                  try:
                      key=random.choice(list(testcats))
                      return key
                  except:
                      Warnwin=Toplevel()
                      Warnlabel=Label(Warnwin, text="There are no words in this category, please update category in order to Test!")
                      Warnlabel.pack(side=TOP)
                      warnvar=IntVar()
                      warnvar.set(1)
                      def destroy():
                          Warnwin.destroy()
                          return
                      Warnbut=Radiobutton(Warnwin,text="ok", variable=warnvar,value=2,command=destroy)
                      Warnbut.pack(side=BOTTOM)
                      return
                  
                  
                  
                  
             
              key=genkey()
              
              
              if key == None:
                  return
                  
              
              Wordroot=Toplevel()
              Germlabel=Label(Wordroot, text="How do you say " + key + " in English?")
              Germlabel.pack()
             
              
             
              
              e1 = Entry(Wordroot, textvariable=name)
              
              def checkinput(event):

                  

                 
                  name=e1.get()  
                  for k, v in testcats.items():
                      if k ==key:
                         targetval=v
                         
                  file=TestGenerator.file
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
                      ###HERE IS WHERE if name ==target val goes !
                      if name==targetval:
                                                                                             
                                              print("self.vocab= " + str(self.vocabfile))
                                              Wordroot.destroy()
                                              print("this is original x" )
                                              keylist=[]
                                              for k in self.wordslist:
                                                  keylist.append(k)
                                              for k, v in testcats.items():
                                                  currentkey=k
                                              print(currentkey + "this is currentkey")

                                              print("current dict= " + str(self.wordslist))
    

                                              currentdic=self.wordslist
                                              def iteratedict(currentdic):
                                                  for x in currentdic:
                                                       if currentkey in currentdic[x]:
                                                                  print (str(currentkey) +  " is currentkey")
                                                                  print((str(currentdic[x])) + "this is currentdic[x]")
                                                                  print(str(x) + "this is x")
                                                                  newkey=x
                                                                  return newkey
                                              newkey=iteratedict(currentdic)
                                              print("this is newkey " + str(newkey))
                                              print(" here are keys %s"%(keylist))
                                              
                                              
                                              LangTest=TestGenerator(newkey)
                                              TestGenerator.Change(event,self,x)
                                                 
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
              Wordroot.geometry=("500x500")
              Wordroot.update()
