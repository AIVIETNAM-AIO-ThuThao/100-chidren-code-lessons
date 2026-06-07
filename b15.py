'''Bài 15, Kiểm tra 3 số a, b, c xem có phải là tam giác đều không'''
while True:
    try:
        a, b, c = map(float, input("Hãy nhập vào độ dài của 3 cạnh của tam giác: ").split())
        if a <= 0 or b <= 0 or c <=0:
            print("Cạnh của tam giác phải có chiều dài lớn hơn 0")
            continue
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                print("Tam giác đều")
            else:
                print("Tam giác không đều")
        else:
            print("Không phải là tam giác")
        
    except ValueError:
        print("Vui lòng nhập đúng định dạng")
