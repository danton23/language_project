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
              Wordroot = Toplevel()
                     
              
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
                     print(categories[x])
                     print("this is self.wordslist[x]"+ str(self.wordslist[x]))
                     testcats=self.wordslist[x]   #here we are splitting the categories dict into only the part that conforms to the original category the user selected (i.e abstract, verbs etc)
                     return testcats
              
              
              formattedwords=self.wordslist.items()
              print("this is formattedwords " + str(formattedwords))
              testcats=genlist(formattedwords)
              def genkey():
                  print("this is " + str(testcats))
                  key=random.choice(list(testcats))
                  Germlabel=Label(Wordroot, text="How do you say " + key + " in English?")
                  Germlabel.pack()
                  return key
              key=genkey()
              
             
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
                      
                      if name==targetval:
                                              print("well done!")
                                              with open(self.vocabfile, 'r') as f:     #NOTE: here because is using tkinter EVENT logic this func is actualyl called with LANGWINDOW class so can use its properties such as self.vocabfile etc 
                                                    data = json.load(f)
                                                    if key not in data:
                                                        print("first time word has come up!")
                                                        d1={key:1}
                                                        data.update(d1)
                                                        with open(self.vocabfile, 'w') as f:
                                                             json.dump(data, f, indent=2)
                                                        
                                                    elif key in data:
                                                        valueint=int(data[key])
                                                        
                                                        if valueint >= 2:  #change this back to 5!!
                                                            Questionwind=Toplevel()
                                                            QuestLabel=Label(Questionwind, text="you have guessed correctly over five times now, do you want to remove the word from the vocab list?")
                                                            QuestLabel.pack(side=TOP)
                                                            def remove():
                                                                
                                                                        
                                                                Questionwind.destroy()
                                                            def notremove():
                                                                print (self.wordslist)
                                                                print (str(self.usefile)+ "is self.usefile")
                                                                print("this is cureent key! " + currentkey)
                                                                print("this is self.wordslist" + str(self.wordslist))
                                                                
                                                                with open(self.usefile, "r") as f:
                                                                    data=json.load(f)
                                                                    for k in data:
                                                                        print(k)
                                                                        print(data[k])
                                                                        if currentkey in data[k]:
                                                                
                                                                           print("item found and is " + currentkey)
                                                                           with open (self.usefile, "r") as f:
                                                                               data=json.load(f)
                                                                               d = {k: v for k,v in data.items() if v}    #in order to iterate over dict have to recast it into a list in this way
                                                                               for k in d:
                                                                                   print("this is data[k]" + str(d[k]))
                                                                               for x  in d[k]:
                                                                                  if currentkey== x:

                                                                                       print("x found and is " + currentkey)
                                                                                       d[k].pop(x) 

                                                                                 #      del data[k][x]
                                                                                       
                                                                                       with open(self.usefile, "w") as f:
                                                                                    
                                                                                           json.dump(d, f, indent=2)
                                                                                           Questionwind.destroy()
                                                                                      
                                                                                           print (currentkey+ "destroyed")
                                                                                       break
                                                                               else:
                                                                                        pass
                                                                Questionwind.destroy()
                                                            var=IntVar()
                                                            var.set(0)
                                                            Rad1=Radiobutton(Questionwind,variable=var, value=1, text="yes", command=remove)
                                                            Rad2=Radiobutton(Questionwind, text="no",variable=var, value=2, command=notremove)
                                                            Rad1.pack(side="left")
                                                            Rad2.pack(side="left")
                                                            print("you have guessed correctly over five times now!")
                                                            d1={key:valueint}
                                                            data.update(d1)
                                                            with open(self.vocabfile, 'w') as f:
                                                                         json.dump(data, f, indent=2)
                                                        elif valueint<= 5:
                                                                  print("you have not guessed correctly more than five times in the current session!")
                                                                  valueint+=1
                                                                  d1={key:valueint}
                                                                  data.update(d1)
                                                                  with open(self.vocabfile, 'w') as f:
                                                                           json.dump(data, f, indent=2)
                                                    
                                                    

                                               
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
