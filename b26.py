'''Bài 26. Tìm giá trị lớn nhất trong 4 số nguyên a, b, c, d (nhập vào từ bàn phím)'''
while True:
    try:
        a, b, c, d = map(float, input("Hãy nhập 4 số bất kỳ: ").split())
        print(f"Số lớn nhất là: {max(a, b, c, d)}")
        break
    except (TypeError, ValueError):
        print("Hãy nhập số đúng định dạng")
