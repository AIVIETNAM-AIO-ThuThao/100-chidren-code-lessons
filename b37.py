'''Bài 37. In ra màn hình kết quả của phép toán Cộng các số lẻ từ 1 đến n.'''
while True:
    try:
        n = int(input("Input a positive integer: "))
        if n < 1:
            print("Please enter a number greater than or equal to 1")
            continue
        
        total = sum(range(1, n+1, 2))
        print(f"The sum of all odd numbers from 1 to {n} is {total}")
        break
    except (TypeError, ValueError):
        print("Please enter a valid format")