from math import *
def area(side1,side2): 
    return(int(side1)*int(side2)/2)  
 
def hypo(side1,side2): 
    return(sqrt((int(side1)*int(side1))+(int(side2)*int(side2)))) 
    
def peri(side1,side2,side3): 
    return(int(side1)+int(side2)+int(side3))

x= input("Enter the base of the triangle: ") 
y= input("Enter the height of the triangle: ") 
 
result= area(x, y)  
hypotenuse= hypo(x, y) 
perimeter= peri(x, y, hypotenuse) 

print("The area of the triangle is: "+str(result)) 
print("The Hypotenuse is: "+str(hypotenuse)) 
print("The perimeter is: "+str(perimeter))