import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp =='s':
        if you =='w':
            return False
        elif you =='g':
            return True
   
    elif comp =='w':
        if you =='s':
            return True
        elif you =='g':
            return False
    elif comp =='g':
        if you =='s':
            return False
        elif you =='w':
            return True        
print("comp turn: enter snake(s) water(w) or gun(g)?")
randNo = random.randint(1,3)
if randNo ==1:
    comp ='s'
elif randNo ==2:
    comp = 'w' 
elif randNo ==3:
    comp = 'g'     
you = input("your turn: enter snake(s) or water(w) or gun(g)")  
a=gamewin(comp,you)  
if a==None:
    print("game is tie")
elif a==True:
    print("congrates you win")  
else:
    print("sorry, you lose ") 