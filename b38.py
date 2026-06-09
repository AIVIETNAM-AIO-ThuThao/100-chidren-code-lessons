'''Bài 38. Bạn hãy nhập vào số n (int) 
rồi in ra màn hình kết quả của phép toán giai thừa n!'''
while True:
    try:
        n = int(input("Enter a positive integer greater than 0: "))
        if n <= 0:
            print("Please enter a positive interger")
            continue
        factorial = 1
        for i in range (1, n + 1):
            factorial *=i
        print(f"The factorial of n is {factorial}")
        break
    except(TypeError, ValueError):
        print("Unvalid Error. Please try again")