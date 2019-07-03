import tkinter
from tkinter import *
import shlex


#genframe=Frame(root, height="500", width="500")
#genframe.pack()
wordlist=["cat","dog","monkey","giraffe","rhino","sealion","man","woman","mollusc","demon"]





iteration=0
pageit=0
totaliteration=0
print(wordlist)


def WordsGen(wordlist):
  Wordroot=tkinter.Tk()
  Wordroot.geometry("500x500")
  Framedict={}    #in order to be able to dynmaically add Frames to Radbuttons below must use a dictionary
  Frame1=Frame(Wordroot, height="100", width="100", bg="green")
  f1={"Frame1":Frame1}
  Framedict.update(f1)
  Frame1.pack(side=TOP, expand="True", fill="both")   #NEED FILL so that it covers background, DONT put inside pointless invisible window frame (causes probs)
  Frame2=Frame(Wordroot, height="100", width="100",bg="red")
  f2={"Frame2":Frame2}
  Framedict.update(f2)
  Frame2.pack(side=TOP, fill="both", expand="True")
  Frame3=Frame(Wordroot, height="100", width="100", bg="purple")
  f3={"Frame3":Frame3}
  Framedict.update(f3)
  Frame3.pack(side=TOP, fill="both", expand="True")
  print(str(Framedict))
  pageit=0
  totaliteration=0
  testlist=[]
  iteration=0
  testvar=IntVar()
  testvar.set(10000)
  rownum=0
  radit=0
  Radlist=[]
  for word in wordlist:
      pageit+=1
      totaliteration+=1   #this enables you to check when LAST iteration occurs (otherwise final list won't print if wordslist total not divisible by 3)
   # if iteration == len(wordlist):
    #    print(testlist)
      
      print(str(len(wordlist)) +"is len wordlist")
      print(str(totaliteration)+ " is totaliteration")
      if pageit==9:
          print ("page limit reached!")
      if totaliteration == len(wordlist):   #this checks if we are currently on last iteration 
         testlist.append(word)   #need to do this otherwise the final word will not appear!
         iteration+=1
         pagename=(str(iteration))
         print("pagename is " + pagename)
         Rowname="Row"+pagename
         print(Rowname)
         print(testlist)
         

      if len(testlist)<2:    #this sets size of list (row)
         testlist.append(word)
      else:
          testlist.append(word)
          iteration+=1
          rownum+=1
          pagename=(str(iteration))
          print("pagename is " + pagename)
          Rowname="Row"+pagename
          print(Rowname)
          print(testlist)
          def Speakvoc(Raddat):
              print(Raddat) 
              print(Raddat +" is item ")
              print("Spoke")
              wordlist.remove(Raddat)   #take it out of overall wordlist
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
                  
                  
          Framename="Frame"+str(rownum)
          print(Framename+"is Framename")
          for k,v in Framedict.items():    #need to use .items() in order to iterate over k AND v
              if k == Framename:
                  Frameuse=v
                  print(str(Frameuse) + " = Frameuse")
              else:
                  print("no match found")
          for item in testlist:
              radit+=1
              print(str(radit) +"is radit")
              name=item
              VocabRad=Radiobutton(Frameuse,text=item,variable=testvar, value=radit, command= lambda Raddat= name:Speakvoc(Raddat))
              VocabRad.pack(side=LEFT, padx=50)
              Radlist.append(VocabRad)
          
          testlist=[]   #here we clear testlist to use again 
        
WordsGen(wordlist)         

    
    
"""for word in self.list:
    valueit+=1
    numnum+=1
    print("num num =" + str(numnum))
    if numnum <=3:
        Rad=Radiobutton(Frame1, text=word, variable=testvar, value=valueit, command=Speak)

        Rad.pack(side=LEFT, padx=50) 
    elif numnum >3 and numnum <=6:   #need to use AND here, i.e numnumb>3<=6 DOESN't WORK!
         Rad2=Radiobutton(Frame2, text=word, variable=testvar, value=valueit, command=Speak)
         Rad2.pack(side=LEFT, padx=50)
    elif numnum >6 and numnum <=9:
         Rad3=Radiobutton(Frame3, text=word, variable=testvar, value=valueit, command=Speak)
         Rad3.pack(side=LEFT, padx =50)



class PageChange:
    def __init__(self, uselist):
        self.uselist=uselist
    def make(self):
      numnum=0
      valueit=0
      Newwind=tkinter.Tk()
      Newwind.geometry("500x500")
      Frame1=Frame(Newwind, height="100", width="100", bg="green")
      Frame1.pack(side=TOP, expand="True", fill="both")   #NEED FILL so that it covers background, DONT put inside pointless invisible window frame (causes probs)
      Frame2=Frame(Newwind, height="100", width="100",bg="red")
      Frame2.pack(side=TOP, fill="both", expand="True")
      for word in self.uselist:
          valueit+=1
          numnum+=1
          print("num num =" + str(numnum))
          if numnum <=3:
             Rad=Radiobutton(Frame1, text=word, variable=testvar, value=valueit, command=Speak)

             Rad.pack(side=LEFT)
          elif numnum >3:
             Rad2=Radiobutton(Frame2, text=word, variable=testvar, value=valueit, command=Speak)
             Rad2.pack(side=LEFT)
        
        
Rad3=Radiobutton(root, text="next page", variable=testvar, value =100000, command=PageChange.make)
Rad3.pack(side=BOTTOM)
"""
"""""for word in wordlist:
    valueit+=1
    e+=1
    enumber=str(e)
    print(enumber)
    if itercount==0:
        Winname="window"+enumber
        print(Winname)
        Winname=Frame(genframe, height="250", width="500", bg=colors[col])
        Winname.pack(side=TOP)
        itercount+=1
        currentWin=Winname
        Rad=Radiobutton(currentWin, text=word,variable=testvar,value=valueit, command=Speak)
        radiolist.append(Rad)
    elif itercount==2:  #length of row
          Winname="window"+enumber
          col+=1
          Winname=Frame(genframe, height="250", width="500", bg=colors[col])
          Winname.pack(side=TOP)
          col=0 #reset col
          itercount=0
          currentWin=Winname
          Rad=Radiobutton(currentWin, text=word,variable=testvar,value=valueit, command=Speak)
          radiolist.append(Rad)
    elif itercount==1:
         itercount+=1
         currentWin=Winname
         Rad=Radiobutton(currentWin, text=word,variable=testvar,value=valueit, command=Speak)
         radiolist.append(Rad)
         
print(radiolist)
for item in radiolist:
    item.pack() """
   
        
        
    
Wordroot.mainloop()
