def ascending_order(numbers): 
    return(numbers.sort(reverse=True))  
    
nums=[]  
n= int(input("How many numbers do you want to enter?: "))  

for i in range(n): 
    num= int(input("Enter a number: "))  
    nums.append(num) 
    
ascending_order(nums) 
print(nums[0])