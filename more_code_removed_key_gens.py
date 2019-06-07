  
def genfirst():
                 try:
                     isfirsttime
                     return True
                 except:
                     return False
             def checkfirst(isfirsttime):                
                if isfirsttime==False:
                     for item in categories:
                             newkey=random.choice(list(tempdict))
                             print("key is" + newkey)
                     isfirsttime=not isfirsttime
                     print(str(isfirsttime) + "isfirsttime")
                     return newkey, True
                else:
                     pass
           






             isfirsttime=genfirst()
             genkey=checkfirst(isfirsttime)[0]
           #  firstgen(isfirsttime)
             print("this is genkey --" + genkey)
             print("first time now = " + str(isfirsttime))







