count= 0 
vowels=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
sentence= input("Enter text: ") 
n= len(sentence) 

for i in range(n): 
    if sentence[i] in vowels:
        count+=1
print (count)