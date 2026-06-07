'''Bài 17.'''
def Pytago(x, y, z):
    result = x**2 == y**2 + z**2
    return result

while True:
    try:
        a, b, c = map(float, input("Nhập vào 3 cạnh của tam giác: ").split())
        if a <= 0 or b <= 0 or c <=0:
            print("Cạnh của tam giác phải lớn 0")
            continue
        if a + b > c and a + c > b and b + c > a:
            if Pytago(a, b, c) or Pytago(b, a, c) or Pytago(c, a, b):
                print("Tam giác vuông")
            else:
                print("Không phải tam giác vuông")
            break
        else:
            print("Không phải là tam giác")
    except ValueError:
        print("Vui lòng nhập đúng định dạng")