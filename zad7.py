import math

a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))

delta = b*b - 4*a*c
print("Delta = " +str(delta))
if delta > 0:
   x1=-(b+math.sqrt(delta))/(2*a)
   x2=-(b-math.sqrt(delta))/(2*a)
   print("Roots for "+ str(a) +"*x^2+"+str(b)+"*x+"+str(c)+" :")
   print("x1: "+str(x1))
   print("x2: "+str(x2))
elif delta == 0:
   x1 = -(b/(2*a))
   print("Roots for "+ str(a) +"*x^2+"+str(b)+"*x+"+str(c)+" :")
   print("x1=x2: "+str(x1))
else:
   print("No roots!")