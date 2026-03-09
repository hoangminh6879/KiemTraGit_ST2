# Nhập hai số từ bàn phím
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

# Tính toán
tong = a + b
hieu = a - b
tich = a * b

# Kiểm tra chia cho 0
if b != 0:
    thuong = a / b
else:
    thuong = "Không thể chia cho 0"

# In kết quả
print("Tổng:", tong)
print("Hiệu:", hieu)
print("Tích:", tich)
print("Thương:", thuong)