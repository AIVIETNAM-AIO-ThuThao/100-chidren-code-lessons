'''Bài 54. Tính a^n (dùng chương trình con)'''
def power(base, exponent):
    return base ** exponent

while True:
    try:
        a, n = map(float, input("Enter a non-zero base and a non-negative exponent:").split())
        if a == 0 and n < 0:
            print("a must be non-zero and n must be equal or great than 0. Try again")
            continue
        print(f"{a} raised to the power of {n} is {power(a, n):.2f}")
        break
    except (TypeError, ValueError):
        print("Please enter valid values")
    
