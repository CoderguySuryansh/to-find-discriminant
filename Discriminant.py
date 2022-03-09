import math

a=int(input("enter coeffecient of x^2:"))
b=int(input("enter coeffecient of x:"))
c=int(input("enter constant:") ) 


d = (b**2) - (4*a*c)
print("Discriminant of given equation :",d)

sol1 = (-b-math.sqrt(d))/(2*a)
sol2 = (-b+math.sqrt(d))/(2*a)

print('The solution are ',sol1,'and',sol2)
