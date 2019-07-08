import tkinter
import random
from Germ_cats import *
# from Spanish_cats import *
from tkinter import *
import json
class TestGenerator:
    file="times.txt"
    def __init__(self, vocab,vocabfile):
       
        self.vocab=vocab
        self.vocabfile=vocabfile
        try:
                                    with open(self.vocabfile,"r") as f:
                                                                    #NEEED TO MOVE THIS PART OUTSIDE OF FUNCTION OTHERWISE RETAINS DATA BETWEEN USER SESSIONS

                                        data = json.load(f)
                                        print("#########!######DATA READABLE ON __INIT__")

                                        
                                                                                  #NOTE: here because is using tkinter EVENT logic this func is actualyl called with LANGWINDOW class so can use its properties such as self.vocabfile etc 
        except:
                     with open (self.vocabfile,"w")as f:
                         print("####1#####1##1#1 DATA NOT READABLE ON __INIT__")
                         contents="{}"
                         f.write(contents)
                                          

     

#    def __init__(self,parent):
        
  #      Wordroot = Frame(parent)
 #       Wordroot.pack()
 #       print("this is parent " + str(parent))
    
    
    
    def hoola(self ):
        print("hoola!")
        print("this is self.vocab " +str(self.vocab))
        print("this is "+ str(self.vocab))
        print ("Здравствуй, мир!")
    
    def Change(event,self,vocab,x):
              
               #contents={}
                                            #data.update(contents)
                                            #print(str(data)+"this is DATA")
                                            #with open(self.vocabfile, "w") as f:
                                                 #json.dump(data,f,indent=2)
            
              print("this is self.vocabfile ##############2####2###:")
              print(str(self.vocabfile))

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

                  

                  try:
                      newnumb
                      newnumb+=1
                      print("try success! newnumb below")
                  except:
                      print("try unsuccesful newnumbintialised below")
                      newnumb=1
                  name=e1.get()  
                  for k, v in testcats.items():
                      if k ==key:
                         targetval=v
                         
                  file=TestGenerator.file
                  with open (file, "r") as f:
                          contents=f.read()
                          print (contents)
                  numbcontents=(int(contents))+1
                  print("numbcontents BELOW")
                  print(str(numbcontents))
                  print("this is target value " + targetval)
                  print(name)
                  print("BELOW IS SELF.VOCABFILE")
                  print(str(self.vocabfile))
                  if numbcontents<=5:
                      print("less")
                      numbcontents+=1
                      print("this is newnumb " + str(numbcontents))
                      ###HERE IS WHERE if name ==target val goes !
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
                  if name==targetval:
                                             
                                              print("well done!")
                                              with open(self.vocabfile, 'r') as f:     #NOTE: here because is using tkinter EVENT logic this func is actualyl called with LANGWINDOW class so can use its properties such as self.vocabfile etc 
                                                    data = json.load(f)
                                                    print("DATA below")
                                                    print(str(data))
                                                    print("KEY IS " + str(key))
                                                    truecheck=False
                                                    for item in data:
                                                        if item ==key:
                                                            truecheck==True
                                                            valueint=int(data[key])
                                                            if valueint == 5:  #change this back to 5!!
                                                                Questionwind=Toplevel()
                                                                QuestLabel=Label(Questionwind, text="you have guessed correctly over five times now, do you want to remove the word from the vocab list?")
                                                                QuestLabel.pack(side=TOP)
                                                                def notremove():
                                                                    with open(self.vocabfile, "r") as f:
                                                                        data=json.load(f)
                                                                        for k, v in data.items():
                                                                            
                                                                            if k == key:
                                                                               with open(self.vocabfile, "r")as f:
                                                                                   data=json.load(f)
                                                                      
                                                                                   d1={key:0}
                                                                                   print(str(d1) + "||||||||!!! this is D1 !!!!!")
                                                                                   data.update(d1)
                                                                               with open(self.vocabfile, 'w') as f:
                                                                                   json.dump(data, f, indent=2)
                                                                                   #break
                                                                        

                                                                        Questionwind.destroy()
                                                                        e1.delete(first=0, last=100)
                                                                        Wordroot.destroy()
                                                                        
                                                                        incrementdat=self.vocabfile
                                                                        TestGenerator.Change(event,self,incrementdat,x)
                                                                def remove():
                                                                    print (self.wordslist)
                                                                    print (str(self.usefile)+ "is self.usefile")
                                                                   
                                                                    print("this is self.wordslist" + str(self.wordslist))
                                                                
                                                                    with open(self.usefile, "r") as f:
                                                                       data=json.load(f)
                                                                       for k in data:
                                                                           print(k)
                                                                           print(data[k])
                                                                           if key in data[k]:
                                                                
                                                                                print("item found and is " + key)
                                                                                with open (self.usefile, "r") as f:
                                                                                                   data=json.load(f)
                                                                                                   d = {k: v for k,v in data.items() if v}    #in order to iterate over dict have to recast it into a list in this way
                                                                                for k in d:
                                                                                    print("this is data[k]" + str(d[k]))
                                                                                for x  in d[k]:
                                                                                  if key== x:  #var was currentkey

                                                                                       print("x found and is " + key)
                                                                                       d[k].pop(x) 

                                                                                 #      del data[k][x]
                                                                                       self.wordslist[k].pop(x)
                                                                                       print(str(self.wordslist) + "THIS IS SELF WORDSLIST AFTER X POPPED")
                                                                                       
                                                                                       
                                                                                       with open(self.usefile, "w") as f:
                                                                                    
                                                                                           json.dump(d, f, indent=2)
                                                                                           Questionwind.destroy()
                                                                                           Wordroot.destroy()
                                                                                      
                                                                                           print (key+ "destroyed")
                                                                                       break

                                                                           else:
                                                                                        pass
                                                                
                                                                var=IntVar()
                                                                var.set(0)
                                                                Rad1=Radiobutton(Questionwind,variable=var, value=1, text="yes", command=remove)
                                                                Rad2=Radiobutton(Questionwind, text="no",variable=var, value=2, command=notremove)
                                                                Rad1.pack(side="left")
                                                                Rad2.pack(side="left")
                                                                print("you have guessed correctly over five times now!")
                                                                valueint+=1
                                                                d1={key:valueint}
                                                                data.update(d1)
                                                                with open(self.vocabfile, 'w') as f:
                                                                         json.dump(data, f, indent=2)
                                                            elif valueint< 5:
                                                                  print("you have not guessed correctly more than five times in the current session!")
                                                                  with open(self.vocabfile, "r") as f:
                                                                      data1=json.load(f)
                                                                      d = {k: v for k,v in data1.items() if v}
                                                                      for k, v in d.items():
                                                                          print(k,v)
                                                                          if k==key:
                                                                                  print("HERE IS VALUE" + str(v))
                                                                                  intv=(int(v))
                                                                                  intv+=1
                                                                                  
                                                                  #intv=int(vint)                
                                                                  
                                                                  print("|||||||||||This is now VALUE  |||||||||" +str(v))
                                                                  
                                                                  valueint+=1       
                                                                  print("as;falsf'skfaos;kf;osafosakfosaf[ok NEW VALUEINT BELOW!")
                                                                  print(valueint)
                                                                  with open(self.vocabfile, "r")as f:
                                                                          data=json.load(f)
                                                                      
                                                                          d1={key:valueint}
                                                                          print(str(d1) + "||||||||!!! this is D1 !!!!!")
                                                                          data.update(d1)
                                                                  with open(self.vocabfile, 'w') as f:
                                                                           json.dump(data, f, indent=2)
                                                                  with open (self.vocabfile,"r")as f:
                                                                          data=json.load(f)
                                                                          print("HERE IS IF VALUE INT LESS THAN 5 ?????????SEEE DATA FILE BELOW")
                                                                          print(str(data))
                                                                  
                                                                  e1.delete(first=0, last=100)
                                                                  Wordroot.destroy()
                                                                        
                                                                  incrementdat=self.vocabfile
                                                                  TestGenerator.Change(event,self,incrementdat,x)

                                                                  
                                                                          
                                                                  
                                                            return truecheck
                                                    if truecheck==False:
                                                             print("first time word has come up!")
                                                             with open(self.vocabfile, "r")as f:
                                                                  data=json.load(f)
                                                                  d1={key:1}
                                                                  data.update(d1)
                                                             print("updated data below")
                                                             print(str(data))
                                                             with open(self.vocabfile, 'w') as f:
                                                                json.dump(data, f, indent=2)
                                                             with open (self.vocabfile, "r") as f:
                                                                data=json.load(f)
                                                                print("a;djaodgja;ojdajodj DDDDDDAAAATTTTAAA below daasfa")
                                                                print(str(data))


                                                    else:
                                                        pass
                                                        
                                                    


                                                            
                                                        
                                                    
                                                        
                                                        
                                                    
                                                                                                                                                         
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
                                              
                                              print("self.vocabfile is ###111####:")
                                              print(str(self.vocabfile))
                                              with open(self.vocabfile, "r")as f:
                                                  data=json.load(f)
                                                  print("JUST BEFORE |||||,,,,|||| NEW CALL this is file")
                                                  print(str(data))
                                              LangTest=TestGenerator(newkey, self.vocabfile)
                                              incrementdat=self.vocabfile
                                              TestGenerator.Change(event,self,incrementdat,x)
                                                 
                  elif name!=targetval:
                                              with open (file,"w")as f:
                                                    f.write(str(numbcontents))
                                              with open ("times.txt", "r") as f:
                                                    contents=f.read()
                                                    print("this is new contents "+ contents)
                                              print ("try again!")
                                              
                  
                          
                  
              e1.bind("<Return>",checkinput)
              e1.pack()
              Wordroot.geometry=("500x500")
              Wordroot.update()
