def translate(phrase):  
    translation=""
    for letter in phrase:  
        if(letter.lower() in "aeiou"):  
            if(letter.isupper()): 
                translation= translation+ "G"  #Checks vowel and replaces it with an uppercase G instead if needed
            else:
                translation= translation+"g"   
        else: 
            translation= translation+letter 
    return translation 
 
 
print (translate(input("Enter your phrase: ")))
        