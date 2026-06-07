'''Bài 24. Tìm giá trị nhỏ nhất trong 2 số nguyên a và b (a, b được nhập từ bàn phím).'''
while True:
    try:
        a, b = map(int, input("Hãy nhập vào 2 số nguyên a, b: ").split())
        if a > b:
            print(f"{b} là số nhỏ nhất")
        else:
            print(f"{a} là số nhỏ nhất")
        break
    except(TypeError, ValueError):
        print("Hãy nhập số")



while True:
    try:
        x, y = map(int, input("Hãy nhập vào 2 số x, y: ").split())
        print(f"{y if x > y else x} là số nhỏ nhất")
        break
    except (TypeError, ValueError):
        print("Hãy nhập số")