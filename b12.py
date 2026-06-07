'''Bài 12. Nhập vào 2 cạnh của một hình chữ nhật. 
In ra màn hình diện tích và chu vi của nó.'''
while True:
    try:
        a, b = map(float, input("Hãy nhập vào chiều dài và chiều rộng của hình chữ nhật: ").split())
        if a <= 0 or b <= 0:
            print("Kích thước phải là số dương!")
            continue
        if a < b:
            a, b = b, a
        print(f"Diện tích: {a * b}; Chu vi: {(a + b)*2}") # đưa print ra ngoài khối if để chỉ phải in 1 lần cho 2 TH
        break
    except ValueError:
        print("Hãy nhập số hợp lệ")
