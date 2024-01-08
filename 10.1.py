#sử dụng thư viện number 
import numpy  
a=float(input("số thứ nhẩt   "))
b=float(input("số thứ hai    "))
c=float(input("số thứ ba    "))
list1=[a,b,c]
list2=[float(x) for x in list1]
max=numpy.max(list2)
print ("số lớn nhất trong 3 số bạn nhập là:",max)