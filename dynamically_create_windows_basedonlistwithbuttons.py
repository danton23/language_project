
import tkinter
from tkinter import *
import shlex


#genframe=Frame(root, height="500", width="500")
#genframe.pack()
wordlist=["dog","cat","rabbit","puppy","kitten","snake","dragon","ogre","witch","giant","sorcerer","necromancer","damsel","hero","russian","german","Spanish","Polish", "Python","Linux","C++","Javascript","sysadmin","Morse","Radiodesign","Italian","Portuguese","Japanese","Aramaic","Koine","English","Russian","Bulgarian","German","Syriac","Russian","Greek","Latin","Persian","French","Arabic","Farsi","Chinese","Czech","Egyptian","C","Flask","Bash","Powershell","Java"]
passlist=wordlist
print(str(len(wordlist)) + " is length wordlist at origin")





iteration=0
pageit=0
totaliteration=0
print(wordlist)


def WordsGen(listuse, totaliteration,usedwords): #For Langage App just need to change listuse to pass in vocab items on first pass
  wordit=len(wordlist)
  print(str(totaliteration) + "is initialisation totalit#1#1#1???????")
  print(wordit)
  Wordroot=Toplevel()  #IMPORTANT! IF you don't use TOPlevel (but use, e.g TK() then the INTVAR only works on FIRST window - (otherwise ALL radiobuttos appear selected on following winds!)
  Wordroot.geometry("500x500")
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
  for word in listuse:
      
      totaliteration+=1
      print("word added " + word + "total its = " + str(totaliteration))
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
      if totaliteration+1 ==(len(wordlist)): #(MUT BE + 3 to work, thinks its to do with no of times code is called or something!)this checks if we are on LAST iteration (if don't implement this and last testlist has LESS items than needed for a row then these won't be packed!)
        rownum+=1 #need to do this or else the final testlist items pack on TOP of previous row 
        Framename="Frame"+str(rownum)
        print("LAST ITERATION" + str(testlist) + "Testlist is this!!!!!")
        wordlistlen=str(len(wordlist))
        print(wordlistlen +"is len wordlist" + str(totaliteration) + "is total iteration!!!!!!")
        print(Framename+"is Framename")
        testlist.append(word)
        for k,v in Framedict.items():    #need to use .items() in order to iterate over k AND v
              if k == Framename:
                  Frameuse=v
                  print(str(Frameuse) + " = Frameuse")
              else:
                  print("no match found")
        for item in testlist:
              print(item+"THIS IS ITEM IN TESTLIST")
              radit+=1
              print(str(radit) +"is radit")
              name=item
              VocabRad=Radiobutton(Frameuse,text=item,variable=testvar, value=radit, command= lambda totaliteration=totaliteration, Raddat= name:Speakvoc(Raddat))
              VocabRad.pack(side=LEFT, padx=50)
              Radlist.append(VocabRad)
          
        testlist=[]   #here we clear testlist to use again 
        
      
      else:
         usedwords.append(word)
         print(str(usedwords)+"is usedwords")
         
         

      if len(testlist)<2 and totaliteration<(len(wordlist)): #and totaliteration != len(wordlist):    #this sets size of list (row)
             testlist.append(word)
             print(str(testlist) + "this is test list which HASN'T been PACKED ####1!!!!!!!###!")
             
       
      else:         #HERE WE CREATE AND PACK RADBUTTON IF haVE REACHED ROW SIZE
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
          

            
          
          if rownum==1:
             buttonval=0

          elif rownum ==2:
             buttonval=4

          else:
             buttonval=7
          print(str(testvar.get())+ " TESTVAR now")
          for item in testlist:
              buttonval+=1
              print(item+"THIS IS ITEM IN TESTLIST")
              radit+=1
              print(str(radit) +"is radit")
              name=item

              
              VocabRad=Radiobutton(Frameuse,text=item,variable=testvar, value=buttonval, command= lambda totaliteration=totaliteration, Raddat= name:Speakvoc(Raddat))
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
             RadChange=Radiobutton(Frame4, text="change page!", variable=testvar, value=100000, command= lambda totaliteration=totaliteration,listuse=newwordslist, usedwords=usedwords: WordsGen(listuse,totaliteration,usedwords))
             RadChange.pack(side=LEFT, padx=200)
             testlist=[]
             break
            

usedwords=[]
root = Tk()
root.withdraw()
WordsGen(passlist,totaliteration,usedwords)


    
    
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
   
        
        
