'''Bài 7. Viết chương trình Python cho phép nhập vào 3 số thực là điểm số của 3 môn thi. 
In ra màn hình “Qua mon” nếu điểm trung bình >= 5.0 ngược lại in ra “Khong qua mon”. 
Điểm trung bình lấy 4 chữ số thập phân'''

try:
    a, b, c = map(float, input("Nhập điểm số 3 môn thi: ").split())
    average = (a + b + c)/3 
    print(f"Điểm trung bình là {average:.4f}")
    print(f"Điểm sau khi làm tròn là {round(average, 4)}")
    if (a + b + c)/3 >= 5.0:
        print("Qua môn")
    else:
        print("Không qua môn")
except ValueError:
    print("Hãy nhập đúng dữ liệu là số")