#số hoàn hảo 
a=int(input("nhap so:"))
i=0
tong=0
while i<a:
    i=i+1
    if a%i==0 and i!=a:
        tong=tong+i
        if tong ==a :
          print("tổng các ước thực sự của số",a ,"bằng",tong,"bằng chính nó nên đây là số hoàn hảo ")

           
    