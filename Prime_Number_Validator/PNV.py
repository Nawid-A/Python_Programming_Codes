flag= False
num= int(input("Type a number: "))  
 
for i in range(2, num): 
    if(num % i) == 0:  
        flag = True 
        break 
 
if flag: 
    print(num, "is not prime") 
else: 
    print(num, "is prime")
 