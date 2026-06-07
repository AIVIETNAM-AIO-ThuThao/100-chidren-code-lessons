'''Bài 30. Nhập vào thời gian 1 công việc nào đó là x giây. 
Hãy chuyển đổi và viết ra màn hình số thời gian trên dưới dạng giờ, phút, giây.'''
while True:
    try:
        x = int(input("Hãy nhập số giây: "))
        hour = x // 3600
        remain = x % 3600
        minute = remain // 60
        second = remain % 60
        print(f"{hour} giờ, {minute} phút, {second} giây")
        break
    except (TypeError, ValueError):
        print("Nhập số")

        
