'''Bài 43. Viết chương trình nhập vào 1 số nguyên dương n, 
hãy cho biết n có bao nhiêu ước và thông báo kết quả ra màn hình.'''
while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("n must be greater than 0")
            continue
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        print(f"The number of divisors of {n} is {count}")
    except(ValueError, TypeError):
        print("Please enter a valid value")