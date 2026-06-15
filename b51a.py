'''Bài 51. Có 3 loại tờ giấy bạc 500đ, 200đ, 100đ. 
Viết chương trình tìm tất cả các phương án để có được số tiền 1700đ từ 3 loại giấy bạc trên'''
def exchange_money(money, a, b, c):
    x, y, z = sorted([a, b, c], reverse=True)
    for i in range(money // x + 1):
        for j in range(money // y + 1):
            h = (money - i*x - j*y) // z
            if i*x + j*y + h*z == money and h >= 0:
                print(f"{money} needs {i} banknotes of {x}, {j} banknotes of {y}, {h} banknotes of {z}")

exchange_money(1700, 500, 200, 100)