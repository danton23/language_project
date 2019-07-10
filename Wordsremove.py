import tkinter
from tkinter import *
import shlex
import json

def Wordsremove(self,Windowroot,Wordlist,wordlist2,vocabcat,listuse, totaliteration,usedwords,category): #For Langage App just need to change listuse to pass in vocab items on first pass
  wordlist=listuse
  print("listusebelow")

  if len(wordlist)==0:
    warnvar=IntVar()
    warnvar.set(1)
    Warnwin=Toplevel()
    Warnlab=Label(Warnwin,text="No vocab in this category, please update!")
    Warnlab.pack(side=TOP)
    def destroy():
      Warnwin.destroy()
      return
    Warnbut=Radiobutton(Warnwin, text="ok",variable=warnvar,value=2,command=destroy)
    Warnbut.pack(side=BOTTOM)
    return
  else:
    pass
  print("Windowroot is " + str(Windowroot))
  Windowroot.destroy()
  print("BELOW is LISTUSE this iteration;;;;;''''';;;;;")
  print("WORDLIST2 LEN BELOW! ###############!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
  print(len(wordlist2))
  print(str(totaliteration) + "is initialisation totalit#1#1#1???????")
  
  print("THIS IS SEEEEEEEEEEEEEEEEEEEEELF " + str(self))
  
  try:
     self.destroy()
     for item in Wordlist:
       print("THIS IS ITEM IN WORDLIST" + str(item))
       usewindow=item
       usewindow.destroy()
  except:
    pass
  Wordroot=Toplevel()  #IMPORTANT! IF you don't use TOPlevel (but use, e.g TK() then the INTVAR only works on FIRST window - (otherwise ALL radiobuttos appear selected on following winds!)
  Wordroot.geometry("1000x1000")
  try:
     Wordlist
     print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
     for item in Wordlist:
       item.destroy()
  except:
    Wordlist=[]
  Wordlist.append(Wordroot)
  
  Framedict={}    #in order to be able to dynmaically add Frames to Radbuttons below must use a dictionary
  Frame1=Frame(Wordroot, height="100", width="100", bg="green")
  f1={"Frame1":Frame1}   #AS you ALWAYS want three frames in screen (with same pattern) can explicitly define them here 
  Framedict.update(f1)
  Frame1.pack(side=TOP, expand="True", fill="both")   #NEED FILL so that it covers background, DONT put inside pointless invisible window frame (i.e like a bootstrap "Container" like treid beofre(causes probs)
  Frame2=Frame(Wordroot, height="100", width="100",bg="red")
  f2={"Frame2":Frame2}
  Framedict.update(f2)
  Frame2.pack(side=TOP, fill="both", expand="True")
  Frame3=Frame(Wordroot, height="100", width="100", bg="purple")
  f3={"Frame3":Frame3}
  Framedict.update(f3)
  Frame3.pack(side=TOP, fill="both", expand="True")
  Frame4=Frame(Wordroot,height="50", width="100", bg="black")
  Frame4.pack(side=TOP, fill="both", expand="True")
  print(str(Framedict))
  pageit=0
  testlist=[]
  iteration=0
  testvar=IntVar()
  
  print(str(testvar.get())+ "ORIGINAL TESTVAR")
  rownum=0 #initialise to zero WITHIN function, this way it will only ever get to max number of rows/frames perpage as, at this point, func is called again, resetting it to ZERO
  radit=0
  Radlist=[]
  
  worditerations=0
  print(str(len(listuse)) + " THIS IS LEN OF LISTUSE THIS ITERATION!")
  def Speakvoc(Raddat):
               print(Raddat)
               Raddat2=Raddat.split(":")
               print("this is RAdDAT2"+str(Raddat2))
               checkvalue=Raddat2[0]
               print("this is checkvalue" +checkvalue)
               print(self.usefile + " is self.usefile")
              
               var=IntVar()
               var.set(-1)
               QuestionWind=Toplevel()
               Questlabel=Label(QuestionWind, text="Are you sure?")
               Questlabel.pack(side=TOP)
               def remove():
                 
                 with open(self.usefile, "r") as f:
                                    data=json.load(f)
                                    for k in data:
                                                 print(k)
                                                 print(data[k])
                                                 if checkvalue in data[k]:
                                                            
                                                           print("item found and is " + checkvalue)
                                                           with open (self.usefile, "r") as f:
                                                                     d = {k: v for k,v in data.items() if v}    #in order to iterate over dict have to recast it into a list in this way
                                                                     for k in d:
                                                                           print("this is data[k]" + str(d[k]))
                                                                     for x  in d[k]:
                                                                              if checkvalue== x:
                                                                                     print("x found and is " + checkvalue)
                                                                                     d[k].pop(x)
                                                                                     with open (self.usefile,"w") as f:
                                                                                       json.dump(d, f, indent=2)
                                                                                       QuestionWind.destroy()
                                                                                       Wordroot.destroy()
                                                                                       print(self.wordslist)
                                                                                       print("WORDSLIST ABOVE")
                                                                                       print(x)
                                                                                      
                                                                                       currentdict=self.wordslist
                                                                                       def iteratedict(currentdic):
                                                                                                      for item in currentdic:
                                                                                                          if x in currentdic[item]:
                                                                                                                     print (str(x) +  " is x")
                                                                                                                     print((str(currentdic[item])) + "this is currentdic[x]")
                                                                                                                     for k, v in currentdic[item].items():
                                                                                                                       if k ==x:
                                                                                                                         currentdic[item].pop(k,v)
                                                                                                                         print("This is now currentdic" + str(currentdic))
                                                                                                                         print(str(self.wordslist) + "this is now self.wordslist")
                                                                                                                         break


                                                                                       iteratedict(currentdict)
                                                                                       return
                 print("RADDAT BELOW")
                 print(Raddat)
                 print("remove")
                 wordlist.pop(Raddat)   #take it out of overall wordlist
                 print(wordlist)
                 print (str(Raddat))   #text[4] is val 
                 for x in Radlist:   #i.e for ever radiobutton listed in the list 
                  
                     conftext=str(x.config("text")) #FIRST need to cast this into a string otherwise python cannot work with the data
                     conflist=list(conftext)
                     print(str(conftext[1]))
                     print(conflist)
                     confsplit=shlex.split(conftext)
                     print(str(confsplit) + "is confsplit")
                     newitem=(confsplit[4]).strip(")")  #all items have ")" at end so must remove
                 if Raddat == newitem:      
                      print("found" + item)
                      x.destroy()     #destroy button from screen
                      Radlist.remove(x)    #need to also remove it from buttonlist
                 else:
                      print("no match")
                 print(str(self.wordslist) + " AFTER POP")
                 with open (self.usefile, "r") as f:
                   data=json.load(f)
                 for k, v in data.items():
                     if k == category:
                       data[k].pop(checkvalue)
                       print("FOUND")
                       with open (self.usefile,"w") as f:
                         json.dump(data,f, indent=2)

                       break
                     else:
                       print("not found")
                       break
                 Wordroot.destroy()
               def notremove():
                 print("not remove")
                 QuestionWind.destroy()
                
               Rad1=Radiobutton(QuestionWind,variable=var, value=1, text="yes", command=remove)
               Rad2=Radiobutton(QuestionWind, text="no",variable=var, value=2, command=notremove)
               Rad1.pack(side="left")
               Rad2.pack(side="left")

               
               
              
  for word in wordlist:
      
      
      print("word added " + word + "total its = " + str(wordlist))
      worditerations+=1
      
      pageit+=1
      print(str(pageit) + " = pageit")
      #totaliteration+=1
      print(str(totaliteration) + "####### TOTALITERATION ########")#this enables you to check when LAST iteration occurs (otherwise final list won't print if wordslist total not divisible by 3)
   # if iteration == len(wordlist):
    #    print(testlist)
      
      print(str(len(wordlist)) +"is len wordlist")
      print(str(totaliteration)+ " is totaliteration")
      print((str(len(wordlist)) + "is current len wordlist" + str(totaliteration) + "is total Iteration"))

  #Below was an ELSE statement before the portion above was commented above  
    
      usedwords.append(word)
      print(str(usedwords)+"is usedwords")
         
         

      if len(testlist)<3 and totaliteration !=len(wordlist2) : #and totaliteration != len(wordlist):    #this sets size of list (row)
             print("NOT PACKED TOTAL IT:"+str(totaliteration+2) + "len(wordlist2)"+str(len(wordlist2)))
             testlist.append(word)
             print(str(testlist) + "this is test list which HASN'T been PACKED ####1!!!!!!!###!")

      elif totaliteration == len(wordlist2):
          testlist.append(word)
          rownum+=1
          Framename="Frame"+str(rownum)
          for k,v in Framedict.items():    #need to use .items() in order to iterate over k AND v
              if k == Framename:
                  Frameuse=v
                  print(str(Frameuse) + " = Frameuse")
              #else:
                #  print("no match found")
          for item in testlist:
              print(item+"THIS IS ITEM IN TESTLIST")
              radit+=1
              Frameuse=Frameuse
              print(str(radit) +"is radit")
              name=item
              VocabRad=Radiobutton(Frameuse,text=item,variable=testvar,value=radit, command= lambda totaliteration=totaliteration, Raddat= name:Speakvoc(Raddat))
              VocabRad.pack(side=LEFT,padx=50)
              Radlist.append(VocabRad)
          
          testlist=[]   #here we clear testlist to use again 
          
          print("LAST WORD" +word)
       
      else:         #HERE WE CREATE AND PACK RADBUTTON IF haVE REACHED ROW SIZE
          testlist.append(word)
          iteration+=1
          rownum+=1 
          pagename=(str(iteration))
          print("pagename is " + pagename)
          Rowname="Row"+pagename
          print(Rowname)
          print(testlist)
          
              
                  
          Framename2="Frame"+str(rownum)
          print(Framename2+"is Framename")
          for k,v in Framedict.items():    #need to use .items() in order to iterate over k AND v
              if k == Framename2:
                  Frameuse=v
                  print(str(Frameuse) + " = Frameuse")
              else:
                  print("no match found")
          

            
          
          if rownum==1:
             buttonval=0

          elif rownum ==2:
             buttonval=4

          else:
             buttonval=7
          print(str(testvar.get())+ " TESTVAR now")
          for item in testlist:
              Framename3="Frame"+str(rownum)
              print("ROWNUM IS"+str(rownum))
              buttonval+=1
              print(item+"THIS IS ITEM IN TESTLIST")
              radit+=1
              print(str(radit) +"is radit")
              name=item
              for k, v in Framedict.items():
                if k==Framename2:
                  Frameuse2=v
              
              VocabRad=Radiobutton(Frameuse2,text=item,variable=testvar, value=buttonval, command= lambda totaliteration=totaliteration, Raddat= name:Speakvoc(Raddat))
              VocabRad.pack(side=LEFT, padx=50)
              Radlist.append(VocabRad)
              print("Buttonval value is " + str(buttonval))
           
          
          if rownum==1 or rownum ==2:
            print("rownum = " + str(rownum))
            testlist=[]   #here we clear testlist to use again
          elif rownum==3:
             print("rownum == 3!!!")
            
          
             pageit=0
             print ("page limit reached!")
             usedword_set=set(usedwords)  #SET returns UNORDERED LIST (need to do to compare for some reason, see below)
             result=[]
             for n in wordlist:
                   if not n in usedword_set and not n in result:    #check each item in wordlist if it has NOT been used (ie is NOT in usedword(set)) then add it to new list called result
                              result.append(n)
             print(str(result) + " THis is RESULT FROM WORDLIST")
             newwordslist=result  #need to pass this into new function call below to ensure that data list worked on in next iteration is only unused words IN ORIGINAL ORDER
          #newwordslist.append(word)
             print(str(wordlist) + " this is wordlist")
             print (str(usedwords)+ " this is usedwords")
             print(str(newwordslist)+"is newwordslist")
             RadChange=Radiobutton(Frame4, text="change page!", variable=testvar, value=100000, command= lambda self=self,Windowroot=None,Wordlist=Wordlist,wordlist2=wordlist2,vocabcat=vocabcat,totaliteration=totaliteration,listuse=newwordslist, usedwords=usedwords, category=category: Wordsremove(self,Windowroot,Wordlist,wordlist2,vocabcat,listuse,totaliteration,usedwords,category=category))
             RadChange.pack(side=LEFT, padx=200)
             testlist=[]
             break
