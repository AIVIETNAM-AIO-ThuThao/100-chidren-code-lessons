'''Bài 22. Viết chương trình nhập 2 số tự nhiên M, N và 
thông báo “ĐÚNG” nếu M, N cùng tính chẵn lẻ, ngược lại thì thông báo “SAI” '''
while True:
    try:
        a, b = map(int, input("Hãy nhập vào 2 số a, b: ").split())
        if (a+b) % 2 == 0:
            print("ĐÚNG")
        else:
            print("SAI")
        break
    except (TypeError, ValueError):
        print("Hãy nhập số mà thôi")



