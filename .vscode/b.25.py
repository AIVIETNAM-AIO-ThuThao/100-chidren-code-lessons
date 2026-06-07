'''Bài 25. Tìm giá trị lớn nhất trong 3 số nguyên a, b, c'''
while True:
    try:
        a, b, c = map(int, input("Hãy nhập vào 3 số nguyên: ").split())
        max = a
        if b > max: max = b
        if c > max: max = c
        print(f"{max} là số lớn nhất")
        break
    except (ValueError, TypeError):
        print("Hãy nhập số đúng")
