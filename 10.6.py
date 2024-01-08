#giải phương trình bậc 2
import math
def phuongtrinhb2(a,b,c):
 if a == 0:
  x=-c/b
  return x 
 else:
  if math.pow(b,2)-4*a*c==0:
   print ("phương trình có nghiệm kép là:", -b/(2*a)) 
  elif math.pow(b,2)-4*a*c<0:
   print("phương trình vô nghiệm") 
  else:
   x1= (-b+math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
   x2=(-b-math.sqrt(math.pow(b,2)-4*a*c))/(2*a) 
   print ("phương trình có nghiệm x1 là ",x1)
   print ("phương trinhg có nghiệm x2 là ",x2)
print(phuongtrinhb2(1,2,1))     
