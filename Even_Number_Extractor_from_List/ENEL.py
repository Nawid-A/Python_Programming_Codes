nums=[] 
n= int(input("How many numbers will you enter?: "))  

for i in range(n): 
    num= int(input("Enter a number: "))  
    if(num%2==0): 
        nums.append(num)
 
print(nums)