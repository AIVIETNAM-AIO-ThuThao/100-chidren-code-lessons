'''Bài 20. Giải phương trình bậc 2'''


delta = lambda a, b, c: b**2 - 4*a*c
x1 = lambda b, a, delta_value: (-b + delta_value**0.5)/(2*a)
x2 = lambda b, a, delta_value: (-b - delta_value**0.5)/(2*a)
double_root = lambda a, b: -b/(2*a)
while True:
    try:
        a, b, c = map(float, input("Hãy nhập vào 3 số a, b, c của hpt: 'ax2 + bx + c = 0': ").split())
        if a == 0:
            print("giá trị a phải khác 0")
            continue
        d = delta(a, b, c)
        if d > 0:
            print(f"PT có 2 nghiệm phân biệt: x1 = {x1(b, a, d)}; x2 = {x2(b, a, d)}")
            break
        if d == 0:
            print(f"Phương trình có 1 nghiệm kép: x = {double_root(a, b)}")
            break
        else:
            print("PT vô nghiệm")
            break
    except ValueError:
        print("Hãy nhập vào giá trị hợp lệ")

