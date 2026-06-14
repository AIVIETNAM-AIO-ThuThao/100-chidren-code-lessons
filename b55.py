'''Bài 55. Tính n! (dùng chương trình con)'''
def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac

while True:
    try:
        n = int(input("Enter a positive integer greater than 1: "))
        if n <= 1:
            print("n must be greater than 1")
            continue
        print(f"Factorial of {n} is {factorial(n)}")
        break
    except (TypeError, ValueError):
        print("Please enter a valid value")