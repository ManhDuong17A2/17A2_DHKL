#Sử dụng hàm pow
import math  
x=float(input("nhập x:"   ))
n=float(input("nhập n:"   ))
A=math.pow(math.pow(x,2)+x+1,n)+math.pow(math.pow(x,2)-x+1,n)
print ("giá trị của biểu thức là:",A)