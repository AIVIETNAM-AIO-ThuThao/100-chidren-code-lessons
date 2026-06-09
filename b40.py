'''Bài 40. Tính tổng các số chia hết cho 3 hoặc 5
Viết chương trình nhập 2 số nguyên dương M và N từ bàn phím(M<N). 
Tính và đưa ra màn hình tổng các số chia hết cho 3 hoặc 5 trong phạm vi từ M đến N.'''
while True:
    try:
        m, n = map(int, input("Enter two different positive integers: ").split())
        if m == n:
            print("m and n must be different!")
            continue
        if m > n:
            m, n = n, m
        total = 0
        for i in range(m, n+1):
            if i % 5 == 0 or i % 3 == 0:
                total += i
        print(f"The sum of all numbers divisible by 3 or 5 from {m} to {n} is {total}")
        break
    except (TypeError, ValueError):
        print("Please enter valid values")