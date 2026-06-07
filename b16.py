'''Bài 16. Kiểm tra xem 3 số nhập vào có phải là 1 tam giác cân không'''

while True:
    try:
        a, b, c = map(float, input("Hãy nhập vào độ dài 3 cạnh:").split())
        if a <= 0 or b <= 0 or c <=0:
            print("Độ dài phải lớn hơn 0")
            continue
        if a + b > c and a + c > b and b + c > a:
            if a == b or a == c or b == c:
                print("Đây là tam giác cân")
            else:
                print("Không phải là tam giác cân")
            break
        else:
            print("Không phải là tam giác")

    except ValueError:
        print("Vui lòng nhập đúng định dạng")