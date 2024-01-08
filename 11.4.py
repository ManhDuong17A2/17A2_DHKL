#nhập dữ liệu đến khi nào chán thì thôi and sử lí dữ liệu
danh_sach = []
k=[0]
for i in k:
    k.append(i+1)
    phan_tu = int(input(f"Nhập phần tử thứ {i + 1}: "))
    danh_sach.append(phan_tu)
    a=input("bạn có muốn nhập dữ liệu tiếp không? nếu có vui lòng nhập '1',nếu không vui lòng nhập '0'")
    if a=="0":
        break
print(danh_sach)
tong=sum(danh_sach)
print (tong)
sodem=int(input("nhập số bạn muốn đếm:  "))
print("số",sodem,"xuất hiện",danh_sach.count(sodem),"lần trong list")
danhsachmoi=[]
for i in danh_sach:
    if i>sodem:
        a=i
        danhsachmoi.append(a)
print ("các số lớn hơn ",sodem,"trong list:",danhsachmoi)
         