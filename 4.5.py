#5
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return a * b // ucln(a, b)
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
result_bcnn = bcnn(num1, num2)
print(f"Bội chung nhỏ nhất của {num1} và {num2} là: {result_bcnn}")