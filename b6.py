'''Bài 6. Một khu đất hình chữ nhật có cạnh là rộng a và dài b. 
Người ta xây một khu vui chơi hình tròn tại vị trí trong khu đất như hình vẽ.
Hỏi rằng khu đất còn lại có diện tích bằng bao nhiêu. Biết rằng giá trị pi = 3.14'''
def remain_area(a, b):
    area_of_the_rectangle = a * b
    area_of_the_circle = 3.14 * ((a / 2) ** 2)
    return area_of_the_rectangle - area_of_the_circle

while True:
    try:
        a, b = map(float, input("Nhập chiều rộng và chiều dài: ").split())

        if a <= 0 or b <= 0:
            print("Các cạnh phải lớn hơn 0!")
            continue

        if a > b:
            a, b = b, a

        break

    except ValueError:
        print("Vui lòng nhập đúng 2 số!")

print(f"Diện tích còn lại là: {remain_area(a, b):.2f}")

