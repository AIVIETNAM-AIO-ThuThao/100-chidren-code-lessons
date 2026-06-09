'''Bài 41. Nhập 2 số nguyên dương M và N từ bàn phím(M<N). 
Tính và đưa ra màn hình tổng các số chia hết cho 2 và 3 trong phạm vi từ M đến N.'''
while True:
    try:
        m, n = map(int, input("Enter two different positive integers: ").split())
        if m <= 0 or n <= 0:
            print("m and n must be greater than 0")
            continue
        if m > n:
            m, n = n, m
        total = 0
        for i in range(m, n+1):
            if i % 2 == 0 and i % 3 == 0:
                total += i
        print(f"the sum of all numbers divisable by 2 and 3 from {m} to {n} is {total}")
        break
    except(TypeError, ValueError):
        print("Enter valid values")