'''Bài 44. Nhận từ bàn phím n lần nhập số, 
đếm các số lớn hơn 10 và nhỏ hơn 20 và thông báo kết quả ra màn hình'''
while True:
    try:
        n = int(input("Enter a postive integer: "))
        if n <= 0:
            print("n must be greater than 0")
        for i in range(1, n+1):
            count = 0
            try:
                a = int(input("Enter a integer: "))
                if a > 10 and a < 20:
                    count += 1
            except (TypeError, ValueError):
                print("Please enter an integer")
        print(f"The count of numbers greater than 10 and less than 20 is {count}")
        break
    except (TypeError, ValueError):
        print("Enter valid number")


                