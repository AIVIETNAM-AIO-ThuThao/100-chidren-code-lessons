'''Bài 35. Tính tổng Sn từ 1 đến n
Bạn hãy nhập vào số n (int) rồi in ra màn hình kết quả của phép toán cộng từ 1 đến n'''
while True:
    try:
        n = int(input("Hãy nhập 1 số bất kỳ và tui sẽ cho bạn số tổng: "))
        if n <= 0:
            print("N lớn hơn 0 mới thích nè")
            continue
        total = 0
        for i in range(1, n+1):
            total += i
        print(total)
        break
    except (ValueError, TypeError):
        print("Nhập số từ bàn phím số nha")