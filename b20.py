'''Bài 20. Giải phương trình bậc 2'''


delta = lambda a, b, c: b**2 - 4*a*c
x1 = lambda b, a, c: (-b + delta(a, b, c)**0.5)/(2*a)  #gọi hàm trong hàm
x2 = lambda b, a, c: (-b - delta(a, b, c)**0.5)/(2*a)
double_root = lambda a, b: -b/(2*a)
while True:
    try:
        a, b, c = map(float, input("Hãy nhập vào 3 số a, b, c của hpt: 'ax2 + bx + c = 0': ").split())
        if a == 0:
            print("giá trị a phải khác 0")
            continue
        elif delta(a, b, c) > 0:           #dùng elif sẽ báo lỗi do phía trên có d = ...
            print(f"PT có 2 nghiệm phân biệt: x1 = {x1(b, a, c):.1f}; x2 = {x2(b, a, c):.1f}")
        elif delta(a, b, c) == 0:
            print(f"Phương trình có 1 nghiệm kép: x = {double_root(a, b):.1f}")
        else:
            print("PT vô nghiệm")
        break               #đẩy break ra ngoài để đảm bảo sẽ thoát khỏi vòng lặp
    except ValueError:
        print("Hãy nhập vào giá trị hợp lệ")