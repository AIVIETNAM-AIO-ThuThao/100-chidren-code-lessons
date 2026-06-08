'''Bài 34. Viết chương trình in ra các số lẻ nhỏ hơn hoặc bằng n'''
while True:
    try:
        n = int(input("Hãy nhập vào 1 số tùy ý: "))
        if n < 0:
            print("Hãy nhập số lớn hơn 0")
            continue
        for i in range(n+1):
            if i % 2 != 0:
                print(i, end=" ")  # In trên cùng dòng
        break
    except (TypeError, ValueError):
        print("Hãy nhập vào số nguyên")