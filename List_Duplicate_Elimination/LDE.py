def get_unique_elements(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

nums=[] 
n= int(input("How many numbers?: ")) 
 
for i in range(n): 
    num= int(input("Enter a number: ")) 
    nums.append(num)   
    
unique=get_unique_elements(nums)

print(unique)
