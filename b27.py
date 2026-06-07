'''Bài 27. Tìm giá trị nhỏ nhất trong 5 số thực a, b, c, d, e từ bàn phím'''
while True:
    try:
        a, b, c, d, e = map(float, input("Hãy nhập vào 5 số: ").split())
        print(f"Số nhỏ nhất là {min(a, b, c, d, e)}")
        break
    except (TypeError, ValueError):
        print("Hãy nhập đúng kiểu dữ liệu")