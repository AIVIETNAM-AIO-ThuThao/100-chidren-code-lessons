'''Bài 18. Tìm nghiệm cho phương trình ax + b = 0'''
linear = lambda a, b: -b/a
a, b = map(float, input("Nhập vào 2 số a, b trong pt ax + b = 0: ").split())
if a == 0:
    if b != 0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình có vô số nghiệm")
else:
    x = linear(a, b)
    print(f"Phương trình có 1 nghiệm: {x}")