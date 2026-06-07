'''Bài 23. Viết chương trình nhập vào 2 số nguyên, 
kiểm tra xem chúng có phải là ước của nhau không'''
while True:
    try:
        a, b = map(int, input("Hãy nhập vào 2 số nguyên: ").split())
        if a == 0 or b == 0:
            print("a và b phải khác 0")
            continue
        if a % b == 0 or b % a == 0:
            print(f"{a} và {b} là ước của nhau")
        else:
            print(f"{a} và {b} không phải là ước của nhau")
        break
    except (TypeError, ValueError):
        print("Hãy nhập số đúng")