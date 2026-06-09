'''Bài 42. Viết chương trình in ra tất cả các ước của một số n nhập từ bàn phím. 
Mỗi ước được ghi trên một dòng'''
while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("n must be greater than 0")
            continue
        for i in range(1, n+1):
            if n % i == 0:
                print(f"{i} is a divisor of {n}")
        break
    except(TypeError, ValueError):
        print("Enter a valid value")