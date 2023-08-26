temp= int(input("What is the temperature?: ")) 
option= input("Fahrenheit or Celsius(F/C): ") 

if(option=='F' or option=='f'): 
    result= (temp-32)*5/9  
    print(str(result)+ " Celsius")
     
elif(option=='C' or option=='c'): 
    result= (temp*9/5)+32  
    print(str(result)+ " Fahrenheit")