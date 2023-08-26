def check(sentence1, sentence2): 
    if(sorted(sentence1)==sorted(sentence2)): 
        print("The strings are anagrams") 
      
    else: 
        print("The strings are not anagrams")

flag= False
line1= input("Enter your first line: ") 
line2= input("Enter your second line: ")   
check(line1, line2) 
