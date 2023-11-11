#7
def tinh_tong_chu_so(N):
    chuoi_so = str(N)
    tong = 0
    for chu_so in chuoi_so:
        tong += int(chu_so)

    return tong

so_nguyen = int(input("Nhập số nguyên N:"))
ket_qua = tinh_tong_chu_so(so_nguyen)
print("Tổng các chữ số của", so_nguyen, "là:", ket_qua)