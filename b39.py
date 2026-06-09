'''Bài 39. Bạn hãy nhập vào cơ số a và số mũ n (int) 
rồi in ra màn hình kết quả của phép toán a mũ n.'''
while True:
    try:
        a, n = map(int, input("Enter the base 'a' and the exponent 'n': ").split())
        if a == 0 and n <= 0:
            print("Enter a non-zero value for base 'a' and a positive value for exponent 'n'")
            continue
        factorial = a**n
        print(f"Two raised to the power of five equals {factorial}")
        break
    except (TypeError, ValueError):
        print("Invalid value. Please try again")