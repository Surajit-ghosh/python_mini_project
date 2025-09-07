#rock-paper-scissor game
import random
list=["rock","paper","scissor"]
while True:
    ccount=0
    ucount=0
    draw=0
    uc=int(input('''
Lets play a 5 round rock-paper-scissor game                 
1: Yes
2: No | Exit 
'''))
    if(uc==1):
        for i in range(1,6):
            uinput=int(input('''
             1 Rock
             2 Paper
             3 Scisor
'''))
            if uinput==1:
                uchoice="rock"
            elif uinput==2:
                uchoice="paper"
            elif uinput==3:
                uchoice="scissor"  
            else:
                uchoice="rock"    
            cchoice=random.choice(list)     
            if cchoice==uchoice:
                print("Your choice is : ",uchoice)
                print("Computer choice is : ",cchoice)
                print("Draw")
                print("")
                draw=draw+1
            elif(uchoice=="rock" and cchoice=="scissor")  or   (uchoice=="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="paper"):
               print("Your choice is : ",uchoice)
               print("Computer choice is : ",cchoice)
               print("You win")
               print()
               ucount=ucount+1
            else:   
               print("Your choice is : ",uchoice)
               print("Computer choice is : ",cchoice)
               print("You lost")
               print("")
               ccount=ccount+1
        if ucount>ccount:
            print('''After a 5 round rock-paper-scissor game
You win 
The score is''')
            print("Your point : ",ucount)   
            print("Computer point : ",ccount) 
            print("Draw matches are : ",draw)
        elif ucount<ccount:
            print('''After a 5 round rock-paper-scissor game
You Lost 
The score is''')
            print("Your point : ",ucount)   
            print("Computer point : ",ccount) 
            print("Draw matches are : ",draw) 
        elif ucount==ccount:
            print('''After a 5 round rock-paper-scissor game
The match is draw
The score is''')
            print("Your point : ",ucount)   
            print("Computer point : ",ccount) 
            print("Draw matches are : ",draw)         
    else:
        print("Thank you for your responce")
        break         