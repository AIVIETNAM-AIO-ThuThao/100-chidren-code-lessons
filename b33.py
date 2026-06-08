'''Bài 33. Nhập vào tâm và bán kính của một đường tròn. 
Sau đó nhập vào một điểm A(x, y) bất kì và kiểm tra xem nó có thuộc đường tròn hay không?'''
import math
while True:
    try:        
        r = float(input("Hãy nhập bán kính r của đường tròn: "))
        if r <= 0:
            print("r phải lớn hơn 0")
            continue
        a, b = map(float, input("Hãy nhập vào 2 số a, b là tọa độ của tâm đường tròn: ").split())
        x, y = map(float, input("Hãy nhập vào 2 số x, y là tọa độ của điểm A: ").split())
        d = math.sqrt((x-a)**2 + (y-b)**2)
        if d > r:
            print("Point A does not belong to the circle")
        else:
            print("Point A belongs to the circle")
        break
    except (ValueError, ValueError):
        print("Nhập đúng dữ liệu nàooo!")

