'''Bài 46. Kiểm tra xem số n nhập vào có phải là số hoàn hảo - tổng các ước số của nó (không kể nó)
 bằng N.'''
while True:
    try:
        n = int(input("Enter a postive integer greater than 1: "))
        if n <= 1:
            print("n must be greater than 1. Try again")
            continue
        total = 0
        for i in range (1,n):
            if n % i == 0:
                total += i
        if n == total:
            print(f"{n} is a perfect number")
        else:
            print(f"{n} is not a perfect number")
        break
    except (TypeError, ValueError):
        print("Enter a valid value")