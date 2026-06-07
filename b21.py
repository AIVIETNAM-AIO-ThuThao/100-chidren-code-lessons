'''Bài 21. Viết chương trình nhập vào 1 số nguyên dương n từ bàn phím. 
Hãy cho biết số đó là số chẵn hay số lẻ'''
a = float(input("Hãy nhập vào 1 số nguyên lớn hơn 0:"))
while True:
    try:
        if a < 0:
            print("Hãy nhập vào 1 số lớn 0")
            continue
        if a % 2 == 0:
            print(f"{a} là số chẵn")
        else:
            print(f"{a} là số lẻ")
            break
    except ValueError:
        print("Hãy nhập số")