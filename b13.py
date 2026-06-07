'''Bài 13. Nhập vào bán kính của hình tròn. 
In ra màn hình diện tích và chu vi của nó. (kết quả làm tròn 2 chữ số thập phân) '''
PI = 3.14 
def calculate(r):
    area = PI * r ** 2
    circumference = 2 * PI * r
    return area, circumference

while True:
    try:
        r = float(input("Hãy nhập vào bán kính của hình tròn: "))
        if r <= 0:
            print("Bán kính phải là số dương lớn hơn 0")
            continue
        else:
            break
    except ValueError:
        print("Hãy nhập số hợp lệ")

area, circumference = calculate(r)          # tuple unpacking theo return của hàm calculate
print(f"Diện tích: {area:.2f}; Chu vi: {circumference:.2f}")