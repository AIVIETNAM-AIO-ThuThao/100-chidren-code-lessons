#Bài 3. Viết chương trình nhập vào hai số. Hoán đổi giá trị của hai số đó.
a = int(input("Nhập số thứ nhất:"))
b = int(input("Nhập số thứ hai:"))
a,b = b,a       #packing
print("Số thứ nhất là ",a, ". Số thứ 2 là ", b)
