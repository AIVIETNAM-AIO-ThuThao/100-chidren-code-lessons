'''Bài 51. Nhập 3 loại tiền và số tiền cần đổi. 
Hãy tìm tất cả các tổ hợp có được của 3 loại tiền trên cho số tiền vừa nhập.'''



while True:
    try: 
        n = int(input("The amount of money to be exchanged: "))
        if n <= 0:
            print("The amount of money to be exchanged must be positive. Try again! ")
            continue
        x, y, z = map(int, input("Enter three denominations: ").split())
        if (x == y or y == z or x == z
            or x <= 0 or y <= 0 or z <= 0):
            print("The denominations must be positive and distinct. Try again!")
            continue
        x, y, z = sorted([x, y, z], reverse=True)
        found = False
        for i in range(n // x + 1): 
            for j in range (n // y + 1): 
                for h in range (n // z + 1): 
                    if (i*x + j*y + h*z == n): 
                        print(f"{i} coins of {x}, {j} coins of {y}, {h} coins of {z}")
                        found = True
        if not found:
            print("No solution")
        break
    except (ValueError):            # không cần TypeError
        print("Enter valid values")


        