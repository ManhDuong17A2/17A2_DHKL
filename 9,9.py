#tính chu vi diện tích 
import math 
Scn= lambda x,y: x*y
Pcn=lambda x,y:x*2+y*2
St=lambda r: math.pow(r,2)*3.14
Pt=lambda r: 2*r*3.14
print ("diện tích hình chữ nhật là:",Scn(3,4))
print ("chu vi hình chữ nhật là:",Pcn(3,4))
print ("diện tích hình tròn là:",St(3))
print ("chu vi hình tròn là:",Pt(3))