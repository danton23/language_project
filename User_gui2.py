import tkinter
import json
from tkinter import *
from tkinter import messagebox
from Germ_cats import *
from functools import partial
from TestGen import TestGenerator
from Span_cats import *
import random
from Wordsremove import Wordsremove
import json
import win32api



root = tkinter.Tk()
root.geometry("500x500")
root.title("Language App")
frame = Frame(root, height="250", width="250", bg="green")
frame.pack(side="bottom", fill="both", expand="True")
Masterlabel=Label(root, text="Please choose a Language to work on today!")
Masterlabel.pack(side=TOP,pady=100)
Rootvar=IntVar()
Rootvar.set(1)
print("this is SpanCategories " + str(SpanCategories))
class Langwindow:
    def __init__(self, wordslist, usefile, vocabfile,language):
        
         self.wordslist=wordslist
         self.usefile=usefile
         self.vocabfile=vocabfile
         self.language=language
         words={}
         
        
         
    butvar=IntVar()
    butvar.set(99)
    
    
    def make(self):

        print("this is words " + str(self.wordslist))
        LangTest=TestGenerator(self.wordslist,self.vocabfile)  #arg was self.wordslist
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
        testvar=IntVar()
        testvar.set(1)
        
        
        
       
                
                   
            
                
               
            
        
       
 
        
        
        def Framegen(words):
            print(dir(self))
             
            iterlist=0
            rootwindow=Toplevel(root)
            rootwindow.geometry("550x350")
            
            def RemoveWords():
              Removeroot=Toplevel(root)
              Removeroot.geometry("300x300")
              Removelabel=Label(Removeroot, text = "Please choose a category to edit")
              Removelabel.pack(side="top")
              Removeframe=Frame(Removeroot, height="150", width="150", bg="green")
              Removeframe.pack(fill="both", expand="True")
              testvar=IntVar()
              testvar.set(1)
              templist=0
              def RemoveWord(x,uselist):
                  print("USELIST BELOW!!!")
                  for word in uselist:
                      print(word)
                
                
                  print(x + "THIS IS CURRENT X!")
                  def DestroyWord(y):
                      print(y)
             
              for word in self.wordslist:
                          print("this is templist!")
                          templist+=1
                          
                          print (str(self.wordslist) + "is self.wordslist")
              for k in self.wordslist:
                           justwords=(self.wordslist[k])
              convertedlist=[(k,v) for k, v in justwords.items()]
              print("CONVERTED LIST BELOW")
              print(convertedlist)
              listtouse=[]
              out = [item for t in convertedlist for item in t ]
              outlist=[s.rstrip("[]") for s in out]   #This is how you remove character from list
              print("OUTLIST BELOW")
              print(outlist)
              emptylist=[]
              iterate=0
              for item in wordsused:
                                print(item + "is item " +str(iterate)+ "is iterate")
                                if iterate==1:
                                   newstring+=item
                                   emptylist.append(newstring)
                                   newstring=""
                                   iterate=0
                                else:
                                   iterate+=1    #iterate =1 on first pass
                                   newstring=item+": "
                                   print("EMPTYLIST BELOW!!")        
                                   print(emptylist)    
               
                                Radiobutton=tkinter.Radiobutton(Removeframe, text=item, variable=testvar, value=templist,command=lambda self=self,Windowroot=Removeroot,Wordlist=None, wordlist2=emptylist,x=word, y=emptylist,totaliteration=0,usedwords=[]:Wordsremove(self,Windowroot,Wordlist,wordlist2,x,y,totaliteration,usedwords), padx=50)
                                Radiobutton.pack(side=LEFT)
            def Removecat(vocabtodisplay,usedwords):
                        iterlist=0
                        Mainremovecat=Toplevel()
                        WindLabel=Label(Mainremovecat, text="Please choose a category to test!", bg="red")
                        WindLabel.pack(side="top")
                        wordframe=Frame(Mainremovecat, height="50", width="250", bg="blue")
                        wordframe.pack(expand="True", fill="both")
                        Selectframe=Frame(Mainremovecat, height="25", width="250", bg="green")
                        Selectframe.pack(expand="True",fill="both")
                        buttonlist=[]
                
                        emptylist=[]
                        iteration=0
            
            
                        print("vocab to display below")
                        print(str(vocabtodisplay))
                        print("CHECKING INITIAL WORDSUSED!")
                        print(str(wordsused))
                        wordsused2=[]
                        listylistlist=[]
                        littleit=0
                        
                        for word in vocabtodisplay:
                                 
                                 
                 
                                 if iterlist <=2:
                                     
                                     iterlist+=1
                                     print("WORDS USED INITIAL")
                                     print(str(wordsused))
                                    
            #list+=1 #use this to create values for the radiobutton value (determines if is on or off) this works!!
     #       print("this is current list value "+str(list)) + "this is current var "+str(var.get())
                                     emptylist=[]
                                     print("here is word" + str(word))
                                     print(str(self.wordslist.get(word)))
                                     myvocab=self.wordslist.get(word)
                                     listylistlist.append(myvocab)
                                     print(str(myvocab) + "IS MYVOCAB")
                                     print("here are vocab items")
                                     
                                     print(str(self.wordslist))
                                     
                                     print("listy listy list [littleit] is " + str(listylistlist[littleit]))
                                     Radiobutton=tkinter.Radiobutton(wordframe, text=word, variable=testvar, value=iterlist,command=lambda self=self,Windowroot=Mainremovecat,Wordlist=None,wordlist2=emptylist,x=None, y=listylistlist[littleit],totaliteration=0,usedwords=[],category=word:Wordsremove(self,Windowroot,Wordlist,wordlist2,x,y,totaliteration,usedwords, category), padx=50)
                                     buttonlist.append(Radiobutton)
            #you need a lambda to pass the particular WORD of the item being iterated over into the function as argument (otherwise it only does this AFTER all buttons created and passes LAST word in)
        #here HAD command=partial(Change)) and worked 
            #if list == 0:Radiobutton.select()
                                     Radiobutton.pack(side="left", padx=50)
                                     wordsused2.append(word)
                                     iteration+=1
                                     littleit+=1
                              
                                 elif iterlist >2:
                                       print("wordsused elif iterlist > 2 is" +str(wordsused))
                                       iteration=0
                                       print("listylistlist" + str(listylistlist[0]))
                                       
                                       usedword_set=set(wordsused2)  #SET returns UNORDERED LIST (need to do to compare for some reason, see below)
                                       result=[]
                                       print("usedword_set below")
                                       print(str(usedword_set))
                                       print("Self wordlist beloW")
                                       print(str(self.wordslist))
                                       for n in vocabtodisplay:
                                   
                                             if not n in usedword_set and not n in result:    #check each item in wordlist if it has NOT been used (ie is NOT in usedword(set)) then add it to new list called result
                                                                              result.append(n)
                                                                              print(str(result) + " THis is RESULT FROM WORDLIST")
                                   
                                       if len(result)==0:
                                           pass
                     
                                       def Newframe2(words,wordsused):
                                                    
                           
                                                     Mainremovecat.destroy()
                           
                           
                                                     Removecat(words,wordsused)
                     
                                       print("WORDS USED AT END OF FUNC BELOW")
                                       print(str(wordsused))
                                       Radiobutton=tkinter.Radiobutton (Selectframe,text="next page!", value=iterlist, variable=var, command=lambda words=result,wordsused=wordsused2:Newframe2(words,wordsused2))
                                       Radiobutton.pack(side="left", padx=200)
                                       break
                        #emptywords=[]
                        #Removecat(self.wordslist,emptywords)
                
            Radiobutton3=tkinter.Radiobutton(rootwindow, text="click to edit a category", variable=testvar, bg="red", value=1, command=lambda vocabtodisplay=self.wordslist,wordsused=[]:Removecat(vocabtodisplay,wordsused))
            Radiobutton3.pack(side=BOTTOM)
            def CategoryDelete(words,wordsused):
                
              
              Deleteroot=Toplevel(root)
              Deleteroot.geometry("500x500")
              Deletelabel=Label(Deleteroot, text="Please choose a Delete!")
              Deletelabel.pack(side="top")
              DeleteFrame=Frame(Deleteroot, height="150", width="150", bg="green")
              DeleteFrame.pack(fill="both", expand="True")
              SelectFrame3=Frame(Deleteroot, height="150", width="150", bg="orange")
              SelectFrame3.pack(fill="both",expand="True")
              testvar=IntVar()
              iteration=0
              testvar.set(1)
              vocabtomod=self.wordslist
              vocablist=[]
              for k, v in vocabtomod.items():     # in order to do for k, v in pyton3 need to use .items() to convert into a list that CAN be iterated over
                    vocabitem=k, v
                    vocablist.append(vocabitem)
              print(vocablist)
              newvar=IntVar()
              newvar.set(1)
              iterlist=0
              def CategoryGone(x):
                  Deleteroot.destroy()
                  Checkroot=Toplevel(root)
                  Checkroot.geometry("500x500")
                  CheckLab=Label(Checkroot, text="Are you sure?")
                  CheckLab.pack()
                  e1=Entry(Checkroot,textvariable=v)
                  def checkvalue5(event,self):
                      name=e1.get()
                      if name=="y" or name =="yes":
                          with open(self.usefile, "r") as f:
                              data=json.load(f)
                              for item in data:
                                  if item ==x:
                                      data.pop(item)
                                      with open(self.usefile, "w") as f:
                                          json.dump(data, f, indent=2)
                                      for item in self.wordslist:
                                          if item ==x:
                                              self.wordslist.pop(x)
                                              break
                                      Checkroot.destroy()
                                      rootwindow.destroy()
                                      self.make() #THIS 'refreshes' window with newly updated values VERY USEFUL AND SMOOTH!
                                      #rootwindow=Toplevel(root)
                                      #rootwindow.geometry("700x700")
                                  

                      elif name =="n" or name =="no":
                          Checkroot.destroy()
                      else:
                          win32api.MessageBox(0, "Please select an appropriate value, must be (y)es or (n)o", "Incorrect Entry")
                          print("please select (y)es or (n)o")
                          e1.destroy()
                          Checkroot.destroy()
                          CategoryGone(x)
                          
                      
                  e1.bind("<Return>",lambda event,self=self:checkvalue5(event,self))
                  e1.pack()
              for word in words:
                 
                 
                 if iteration <=2:
                              
            #list+=1 #use this to create values for the radiobutton value (determines if is on or off) this works!!
     #       print("this is current list value "+str(list)) + "this is current var "+str(var.get())
                              iteration+=1
                              Radiobutton=tkinter.Radiobutton(DeleteFrame, text=word, variable=testvar, value=iteration,command=lambda x=word:CategoryGone(x), padx=50)
                              Radiobutton.pack(side=LEFT)
            #you need a lambda to pass the particular WORD of the item being iterated over into the function as argument (otherwise it only does this AFTER all buttons created and passes LAST word in)
        #here HAD command=partial(Change)) and worked 
            #if list == 0:Radiobutton.select()
                              Radiobutton.pack(side="left", padx=50)
                              wordsused.append(word)
                              iteration+=1
                 elif iteration >2:
                     iteration=0
                     print("wordsusedis" +str(wordsused))
                     usedword_set=set(wordsused)  #SET returns UNORDERED LIST (need to do to compare for some reason, see below)
                     result=[]
                     for n in self.wordslist:
                         if not n in usedword_set and not n in result:    #check each item in wordlist if it has NOT been used (ie is NOT in usedword(set)) then add it to new list called result
                                   result.append(n)
                                   print(str(result) + " THis is RESULT FROM WORDLIST")
                                   
                     if len(result) ==0:
                          break
                     
                     def Newframe2(words,wordsused):
                           
                           Deleteroot.destroy()
                           
                           
                           CategoryDelete(words,wordsused)
                     
                     
                     Radiobutton=tkinter.Radiobutton(SelectFrame3, text="next page!", value=iterlist, variable=var, command=lambda words=result:Newframe2(words,wordsused))
                     Radiobutton.pack(side="left",padx=200)
                     break
              
                
            Radiobutton4=tkinter.Radiobutton(rootwindow,text="click to remove a category", variable=testvar, bg="red", value =2,command=lambda vocabtodisplay=self.wordslist,wordsused=[]:CategoryDelete(vocabtodisplay,wordsused))
            Radiobutton4.pack(side=BOTTOM)
            def UpdateWords(words,wordsused):
              
              Updateroot=Toplevel(root)
              Updateroot.geometry("500x500")
              Updatelabel=Label(Updateroot, text="Please choose a category to add to!")
              Updatelabel.pack(side="top")
              UpdateFrame=Frame(Updateroot, height="150", width="150", bg="green")
              UpdateFrame.pack(fill="both", expand="True")
              SelectFrame2=Frame(Updateroot, height="150", width="150", bg="orange")
              SelectFrame2.pack(fill="both",expand="True")
              testvar=IntVar()
              iteration=0
              testvar.set(1)
              vocabtomod=self.wordslist
              vocablist=[]
              for k, v in vocabtomod.items():     # in order to do for k, v in pyton3 need to use .items() to convert into a list that CAN be iterated over
                    vocabitem=k, v
                    vocablist.append(vocabitem)
              print(vocablist)
              newvar=IntVar()
              newvar.set(1)
              iterlist=0
              for word in words:
                 
                 
                 if iteration <=2:
                              
            #list+=1 #use this to create values for the radiobutton value (determines if is on or off) this works!!
     #       print("this is current list value "+str(list)) + "this is current var "+str(var.get())
                              iteration+=1
                              Radiobutton=tkinter.Radiobutton(UpdateFrame, text=word, variable=testvar, value=iteration,command=lambda x=word:AddWord(x), padx=50)
                              Radiobutton.pack(side=LEFT)
            #you need a lambda to pass the particular WORD of the item being iterated over into the function as argument (otherwise it only does this AFTER all buttons created and passes LAST word in)
        #here HAD command=partial(Change)) and worked 
            #if list == 0:Radiobutton.select()
                              Radiobutton.pack(side="left", padx=50)
                              wordsused.append(word)
                              iteration+=1
                 elif iteration >2:
                     iteration=0
                     print("wordsusedis" +str(wordsused))
                     usedword_set=set(wordsused)  #SET returns UNORDERED LIST (need to do to compare for some reason, see below)
                     result=[]
                     for n in self.wordslist:
                         if not n in usedword_set and not n in result:    #check each item in wordlist if it has NOT been used (ie is NOT in usedword(set)) then add it to new list called result
                                   result.append(n)
                                   print(str(result) + " THis is RESULT FROM WORDLIST")
                                   
                     if len(result) ==0:
                          break
                     
                     def Newframe2(words,wordsused):
                           
                           Updateroot.destroy()
                           
                           
                           UpdateWords(words,wordsused)
                     
                     
                     Radiobutton=tkinter.Radiobutton(SelectFrame2, text="next page!", value=iterlist, variable=var, command=lambda words=result:Newframe2(words,wordsused))
                     Radiobutton.pack(side="left",padx=200)
                     break
              
                  
            #print (words)
            Radiobutton5=tkinter.Radiobutton(rootwindow, text="click to update a category", variable=testvar ,bg="red", value=0, command=lambda vocabtodisplay=self.wordslist,wordsused=[]:UpdateWords(vocabtodisplay,wordsused))
            Radiobutton5.pack(side=BOTTOM)

        
            
            
                    
        
            def EntryWindow():
                    Wordroot = Toplevel()
                    Wordroot.geometry=("500x500")
                    Windowlabel.pack()
                    v=StringVar()
                    e1 = Entry(Wordroot, textvariable=v)
                    def checkvalue(self):
                            print("these are current wordvalues " + str(LangTest.vocab))
                            name=e1.get()
                            print(name)
                            Wordroot.destroy()
                            Wordroot2=Tk()
                            Wordroot2.geometry=("500x500")
                            Windowlabel=Label(Wordroot2, text="please enter the new English word")
                            Windowlabel.pack()
                            v=StringVar()
                            e2=Entry(Wordroot2, textvariable=v)
                            def checkvalue2(self):
                                name=e2.get()
                                print(name)
                                Wordroot2.destroy()
                            e2.bind("<Return>",checkvalue2)
                            e2.pack()
                    e1.bind("<Return>",checkvalue)
                    e1.pack()

                    #put code back in here from seperate file (of ENTRYWINDOW)
            
                    
            def AddWord(x):
                WordRoot=Toplevel()
                WordRoot.geometry("500x500")
                print(str(self.wordslist)+"this is wordlist")
                
                
                v=StringVar()
                def checkvalue1():
                    WordRoot.destroy()
                    WordRoot2=Toplevel()
                    WordRoot2.geometry=("500x500")
                    Windowlabel=Label(WordRoot2, text="please enter the new German word")
                    Windowlabel.pack()
                    e1=Entry(WordRoot2, textvariable=v)
                    def checkvalue2(event,self):
                            print("these are current wordvalues " + str(LangTest.vocab))
                            tempname=e1.get()
                            
                            print(tempname)
                            with open("tempwords.txt", "w") as f:
                                f.write(tempname +" ")
                           # print(self.wordslist +"this is wordlist inside checkvalue2")
                            WordRoot2.destroy()
                            WordRoot3=Tk()
                            WordRoot3.geometry=("500x500")
                            Windowlabel=Label(WordRoot3, text="please enter the new English word")   #NOTE HERE IT CANNOT DEAL WITH SPACES SO IT THINKS VERBS ARE JUST "TO
                            Windowlabel.pack()
                            v=StringVar()
                            e2=Entry(WordRoot3, textvariable=v)
                            def checkvalue3(event,self):
                                tempname2=e2.get()
                                print(str(tempname2)+ " is TEMPNAME2 ")
                               #list(map(str,input().split()))
                                with open("tempwords.txt", "a") as f:
                                   tempname3=str(tempname2)
                                   
                                   f.write(tempname3)
                                newlist=[]
                                with open("tempwords.txt", "r") as f:
                                    
                                    lines=f.readlines()
                                for i in lines:
                                        thisline=i.split(" ")
                                        print("this is this line" + str(thisline))
                                        key=thisline[0]
                                        value=tempname2
                                        print(str(value)+ "VALUE") 
                                        print("key is " + key + " value is " + value)
                                        print (str(self.wordslist) + "THis is Langwindow.wordslist ")
                                        print("key is " + key)
                                        print("this is current " + x)     ### WORK ON THIS this checks currently held values - vocab etc  - THIS ONE tells current category being manipulated
                                        print("this is words " + str(self.wordslist))  ###this shows ALL values within language group 
                              #      words+={key:value}
                                for item in self.wordslist:
                                        if item == x:
                                            print("match found!")
                                            print(self.wordslist[item])
                                            self.wordslist[item][key]=value
                                            print(self.wordslist[item][key] + "this is new value!")
                                            with open ("Germ_cats.py","a+") as f:
                                                for item in categories:
                                                    if item==x:

                                                        categories[item].update(key=value)
                                                       
                                print("this is newlist " + str(newlist))
                                print("x frm tempwords.txt = " + str(x))
        
                                with open(self.usefile, 'r') as f:
                                       data = json.load(f)
                                       print(key + "this is key now")
                                       print("this is json data[item]" + str(data[item]))
                                       d1={key:value}
                                       data[x].update(d1)
                                       print(str(data[x]) + "this is data[item]")

                                with open(self.usefile, 'w') as f:
                                        json.dump(data, f, indent=2)
                                WordRoot3.destroy()
                                #Updateroot.destroy()
                            e2.bind("<Return>", lambda event, self=self: checkvalue3(event,self)) ##as Button returns event by default need to use Lambda to pass in self so can call it within function
                            e2.pack()
                    e1.bind("<Return>",lambda event, self=self:checkvalue2(event,self))
                    e1.pack()
                wordvar=IntVar()
                wordvar.set(0)
                Radiobutton=tkinter.Radiobutton(WordRoot, variable=wordvar, value=1, text="click to add a new "+ self.language +" word", command=checkvalue1)
                Radiobutton.pack()
               
                           
                
             
                    
                
                   
            
                
              
          
            def AddCategory():
            
                
                   
                    WordRoot2=Toplevel()
                    WordRoot2.geometry=("500x500")
                    Windowlabel=Label(WordRoot2, text="please enter the name of the new category")
                    Windowlabel.pack()
                    e1=Entry(WordRoot2)
                    def checkvalue2(event,self):
                            print("these are current wordvalues " + str(LangTest.vocab))
                            tempname=e1.get()
                            
                            print(tempname)
                            with open("tempwords.txt", "w") as f:
                                f.write(tempname +" ")
                            self.wordslist[tempname]={}
                           # print(self.wordslist +"this is wordlist inside checkvalue2")
                            newitem={tempname:{}}
                            with open (self.usefile, "r")as f:
                               data=json.load(f)
                               data.update(newitem)
                            with open(self.usefile, "w") as f:
                                json.dump(data,f,indent=2)
                            WordRoot2.destroy()
                            rootwindow.destroy()
                            self.make()     #This 'refreshes' main Lang window with newly updated values (if you just redefine rootwindow it doesnt change at all!)  
                    e1.bind("<Return>",lambda event, self=self:checkvalue2(event,self))
                    e1.pack()
            Radiobutton3=tkinter.Radiobutton(rootwindow, text="click to add a category", variable=testvar, bg="red", value=10000, command=AddCategory)
            Radiobutton3.pack(side=BOTTOM)
            WindLabel=Label(rootwindow, text="Please choose a category to test!", bg="red")
            WindLabel.pack(side="top")
            wordframe=Frame(rootwindow, height="50", width="250", bg="blue")
            wordframe.pack(expand="True", fill="both")
            Selectframe=Frame(rootwindow, height="25", width="50", bg="green")
            Selectframe.pack(expand="True",fill="both")
            
                
            
            iteration=0
            
            
            iterlist+=1
            for word in words:
                print(word)
                print("WOOOOOORDLIST")
            for word in words:
                 print(word + "WORD!")
                 iterlist+=1
                 
                 if iteration <2:
                              print("Current iteration"+str(iteration))
                              ("Currentwordis" + str(word))
                              
            #list+=1 #use this to create values for the radiobutton value (determines if is on or off) this works!!
     #       print("this is current list value "+str(list)) + "this is current var "+str(var.get())
                              Radiobutton=tkinter.Radiobutton(wordframe, text=word,value=iterlist, variable=var,command=lambda self=self,vocab=self.usefile, x=word: LangTest.Change(self,vocab,x)) #vocab=words
                              buttonlist.append(Radiobutton)
            #you need a lambda to pass the particular WORD of the item being iterated over into the function as argument (otherwise it only does this AFTER all buttons created and passes LAST word in)
        #here HAD command=partial(Change)) and worked 
            #if list == 0:Radiobutton.select()
                              Radiobutton.pack(side="left", padx=50)
                              wordsused.append(word)
                              iteration+=1
                              
                 elif iteration >1:
                    
                    
                    Radiobutton=tkinter.Radiobutton(wordframe, text=word,value=iterlist, variable=var,command=lambda self=self,vocab=self.usefile, x=word: LangTest.Change(self,vocab,x)) #vocab=words
                    buttonlist.append(Radiobutton)
            #you need a lambda to pass the particular WORD of the item being iterated over into the function as argument (otherwise it only does this AFTER all buttons created and passes LAST word in)
        #here HAD command=partial(Change)) and worked 
            #if list == 0:Radiobutton.select()
                    Radiobutton.pack(side="left", padx=50)
                    wordsused.append(word)
                    print("wordsusedis" +str(wordsused))
                    print("CURRENT ITERATION"+str(iteration))
                   
                     
                    usedword_set=set(wordsused)  #SET returns UNORDERED LIST (need to do to compare for some reason, see below)
                    result=[]
                    for n in self.wordslist:
                         if not n in usedword_set and not n in result:    #check each item in wordlist if it has NOT been used (ie is NOT in usedword(set)) then add it to new list called result
                                   result.append(n)
                                   print(str(result) + " THis is RESULT FROM WORDLIST")
                                   
                    if len(result) ==0:
                       ("Print len (result) ==0 BREAAAKING")
                       break
                     
                    def Newframe(words):
                           
                           rootwindow.destroy()
                           
                           
                           Framegen(words)

                    
                     
                    Radiobutton=tkinter.Radiobutton(Selectframe, text="next page!", value=iterlist, variable=var, command=lambda x=result:Newframe(x))
                    Radiobutton.pack(side="left", padx=200)
                    iteration=0
                    break
        wordsused=[]
        Framegen(self.wordslist)
#newwindow=Langwindow.create(self)

#Spanwindow.wordslist=SpanCategories
#print(Spanwindow.wordslist)


def WordsGen(file):
    words={}
    with open(file, "r") as f:
               data = json.load(f)
               for k, v in data.items():
                    words.update({k:v})
    print("this is RUswords NOW!" + str(words))
    return (words)
def current_languages():
    languages=[]
    with open("languages.json", "r")as f:
        data=json.load(f)
        count1=0
        for k, v in data.items():
            for item in v:
                count1+=1
        print("count 1 is")
                
        count=0 
        while count< count1:
          for k,v in data.items():
              for item in v:
                count+=1
                languages.append(item)
                print("languages is " +str(languages))
        else:
               return languages
        
languages=current_languages()
print("these are languages!" + str(languages))

#for item in languages:
 #   print (item)
  #  Newwind=Langwindow(str(item)+"words", str(item)+"_cats.json", str(item)+".json", str(item))
   # print (Newwind.usefile)    #way of dynamically checking existing languages - try to figure out how to use this to generate Radiobuttons!
    
Rusfile="Rus_cats.json"
with open("Russvocabcheck.json","w") as f:
                      contents="{}"
                      f.write(contents)
Ruswords=WordsGen(Rusfile)
Russwindow=Langwindow(Ruswords,Rusfile, "Russvocabcheck.json","Russian")

#Russwindow.ident=Russwindow

Germfile="Germ_cats.json"
with open ("Germvocabcheck.json","w")as f:
                         contents="{}"   #NEED TO 'wipe' this every time app is run otherwise is stores previous scores and vocab and other funcs don'trun properly
                         f.write(contents)
with open("Spanvocabcheck.json", "w") as f:
                         contents="{}"
                         f.write(contents)

Germwords=WordsGen(Germfile)
Germwindow=Langwindow(Germwords, Germfile, "Germvocabcheck.json", "German")  #use last variable to check how many times a word guessed correctly in Langtest
Spanfile="Span_cats.json"
Spanwords=WordsGen(Spanfile)
Spanwindow=Langwindow(Spanwords, Spanfile, "Spanvocabcheck.json", "Spanish")
#Germwindow.wordslist=categories




w= Radiobutton(frame, text ="German", variable=Rootvar,value=1, command=Germwindow.make, padx=1) #parent WAS root before
w.pack(side="left", padx=50)
w1 =Radiobutton(frame, text ="Russian",variable=Rootvar, value=2, command=Russwindow.make, padx=1)
w1.pack(side="left", padx=50)
w3=Radiobutton(frame, text ="Spanish", variable=Rootvar, value=3, command=Spanwindow.make, padx=1)
w3.pack(side="left", padx=50)
root.mainloop()
