'''Bài 28. Bạn hãy nhập vào hai số nguyên (int) 
và một phép toán (str) rồi in ra màn hình kết quả của phép toán.'''
while True:
    try:
        a, b = map(int, input("Hãy nhập 2 số nguyên: ").split())
        operator = input("Hãy nhập 1 trong các phép toán (+, -, *, /): ") #str là 1 hàm built in nên ko được dùng
        if operator == '/': total = a/b          #thêm dấu nháy để python biết đó là string
        elif operator == '+': total = a + b
        elif operator == '-': total = a - b
        elif operator == '*': total = a*b
        else:
            print("Chỉ được chọn 1 trong 4 phép toán đã cho")
            continue
        print(f"{total}")
        break
    except (TypeError, ValueError):
        print("Hãy nhập đúng yêu cầu")
    except ZeroDivisionError:
        print("Lỗi: Số thứ 2 phải khác 0! Vui lòng nhập lại.")


# with match-case
while True:
    try:
        x, y = map(int, input("Hãy nhập 2 số nguyên x, y: ").split())
        operator = input("Hãy nhập 1 trong các phép toán (+, -, *, /): ")
        
        match operator:
            case '+':
                total = x + y
            case '-':
                total = x - y
            case '*':
                total = x * y
            case '/':
                total = x / y
            case _:  # mặc định khi không khớp case nào
                print("Chỉ được chọn 1 trong 4 phép toán đã cho")
                continue
        
        print(f"{a} {operator} {b} = {total}")
        break
    except ValueError:
        print("Hãy nhập đúng 2 số nguyên, cách nhau bằng khoảng trắng!")
    except ZeroDivisionError:
        print("Lỗi: Số thứ 2 phải khác 0! Vui lòng nhập lại.")