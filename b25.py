'''Bài 25. Tìm giá trị lớn nhất trong 3 số nguyên a, b, c được nhập từ bàn phím'''
while True:
    try:
        a, b, c = map(int, input("Hãy nhập vào 3 số nguyên dương bất kỳ: ").split())
        max = a
        if b > max: max = b
        if c > a: max = c
        print(f"Số lớn nhất là {max}")
    except (TypeError, ValueError):
        print("Hãy nhập đúng loại dữ liệu là số nguyên")