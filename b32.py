'''Giải hệ phương trình tuyến tính:
ax + by = m
cx + dy = n'''
def solv_cramer_system (a, b, m, c, d, n):
    det = a*d - b*c
    Dx = d*m - b*n
    Dy = a*n - c*m
    if det == 0 and Dx == 0 and Dy == 0:
        return "The system of equations has infinitely many solutions"
    elif det == 0 and (Dx != 0 or Dy != 0):
        return "The system of equations has no solution"
    else:
        x = Dx/det
        y = Dy/det
    return x, y         #packing thành tuple

while True:
    try:
        a, b, m, c, d, n = map(int, input("Hãy nhập vào 6 số a, b, m, c, d, n của hệ ax + by = m và cx + dy = n: ").split())
        result = solv_cramer_system(a, b, m, c, d, n)
        if isinstance(result, tuple):  # Kiểm tra nếu là nghiệm
            x, y = result
            print(f"The system of equations has a unique solution:\n x = {x} \n y = {y}")
            break
        else:
            print(result)
    except (TypeError, ValueError):
        print("Hãy nhập đúng định dạng")
