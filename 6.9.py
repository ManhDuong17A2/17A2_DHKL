#1.9
lai_suat=float(input("Lãi suất 1 năm (%) :"))
tien_gui=int(input("Số tiền gửi :"))
so_thang_gui=int(input("Số tháng gửi :"))
tien_lai=(tien_gui*so_thang_gui)*(lai_suat/12)
tong_so_tien=tien_gui+tien_lai
print("tiền lãi =",tien_lai)
print("Tiền vốn + Lãi =",tong_so_tien)