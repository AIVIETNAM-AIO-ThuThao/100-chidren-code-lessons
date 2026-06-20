'''Bài 53. Giải bài toán:
Trăm trâu, trăm cỏ
Trăm trâu trăm cỏ
Trâu đứng ăn năm
Trâu nằm ăn ba
Trâu già ba con một bó. Hỏi có bao nhiêu con mỗi loại?''' 

def solve():
    found = False #gán biến cờ
    for standing in range(100//5):
        for laying in range(100//3):
            old = 100 - standing - laying
            if old >=0 and \
                15*standing + 9*laying + old == 300:         #tối ưu hóa để không phải kiểm tra hết toàn bộ giá trị của chú trâu già, khà khà khà
                    print(f'Số trâu đứng là {standing}; trâu nằm là {laying}; trâu già {old}')
                    found = True        # thay đổi cờ
    if not found:
        print("No solution exists")
    return None         #thừa, có thể bỏ
solve() 






