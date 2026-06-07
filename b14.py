'''Bài 14. Nhập vào ba số a, b, c bất kì. K.tra xem đó có thể là độ dài ba cạnh của 1 tam giác hay không, 
nếu không thì in ra màn hình 'Không là 3 cạnh của một tam giác '. 
Ngược lại, thì in diện tích và chu vi của tam giác ra màn hình. '''

while True:
    try:
        a, b, c = map(float, input("Nhập vào độ dài 3 cạnh a, b, c: ").split())
        
        if a <= 0 or b <= 0 or c <= 0:
            print("Độ dài cạnh phải là số dương lớn hơn 0")
            continue
        if a + b > c and a + c > b and b + c > a:
            chuvi= a + b + c
            p = chuvi / 2
            dientich = (p * (p - a) * (p - b) * (p - c)) ** 0.5 # công thức Heron để tính diện tích
            print(f"Diện tích: {dientich:.2f} mét vuông; Chu vi: {chuvi:.2f} mét")
        else:
            print("Không là 3 cạnh của một tam giác")
            break
        
    except ValueError:
        print("Hãy nhập số hợp lệ") 