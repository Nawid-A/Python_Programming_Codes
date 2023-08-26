import random 

choices= ["giraffe", "rhino", "cheetah", "elephant", "aardvark", "snake", "goat"]  
description= ["Long necked creature", "A headbutt from this animal would be like a stab!","Who needs an engine when you're the fastest?", "You better remember this one because they will never forget", "The true ant bully", "Folklore hates them, but you would probably do the same if you had no legs", "Mohammed Ali, Ronaldo, Sidney Crosby, Lebron James..."]
guess=""  
count=0 
final=False
 
word= random.choice(choices)  
place= int(choices.index(word)) 
print("Hint: "+ description[place])
 
while(guess!=word):  
    if(count<3):
        guess=input("Enter your guess: ")  
        count+=1  
    else:  
        final=True
        break
 
if final: 
    print("You ran out of tries, loser")  

else:
    print ("You won!")
