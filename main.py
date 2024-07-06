'''
1 for rock
2 for paper
3 for scissors
'''
import random
#you choose
youDict={"r":1,"p":2,"s":3}
#Amit choose
reverseDict={1:"Rock✊",2:"Paper✋",3:"Scissor✌️"}
#get the Amit choose
Amit=random.choice([1,2,3])
#get the user choice
youstr=input("Your turn! Enter 'r' for Rock✊, 'p' for Paper✋, 's' for Scissor✌️:\n").lower()

if youstr in youDict:
    Pooja=youDict[youstr]
    print(f"Pooja choose {reverseDict[Pooja]}\nAmit choose {reverseDict[Amit]}")
    
    if (Amit==Pooja):
        print("tie🤪")
    else:
        if (Amit==1 and Pooja ==2): #-1
            print("You win😎")
        elif(Amit==1 and Pooja ==3): #2
            print("You loss😞")

        elif (Amit==2 and Pooja ==1): #1
            print("You loss😞")
        elif(Amit==2 and Pooja ==3): #-1
            print("You win😎")

        elif (Amit==3 and Pooja ==1): #2
            print("You win😎")
        elif(Amit==3 and Pooja ==2): #1
            print("You loss😞")

        # elif(you!=1,you!=2,you!=3):
        #     print("please enter R for rock\np for paper\ns for scissors")


