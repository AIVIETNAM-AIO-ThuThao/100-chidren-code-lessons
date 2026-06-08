'''Bài 29. Tìm số ngày của năm N, biết rằng năm nhuận là năm chia hết cho 400; hoặc chia hết cho 4 
nhưng không chia hết cho 100'''
while True:
    try:
        year = int(input("Hãy nhập vào số năm: "))
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
            print(f"Số ngày của năm {year} là 366 ngày")
        else: 
            print(f"Số ngày của năm {year} là 365 ngày")
        break
    except (TypeError, ValueError):
        print("Hãy nhập năm bằng số")