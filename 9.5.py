#xây dựng hàm tính A
import math  
def A(x,n):
    return math.pow(math.pow(x,2)+x+1,n) +math.pow(math.pow(x,2)+x+1,n) 
print(A(1,2))
