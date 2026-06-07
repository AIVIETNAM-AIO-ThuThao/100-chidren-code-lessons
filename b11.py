'''Bài 11. Hình vuông. 
Nhập vào 1 cạnh của một hình vuông. In ra màn hình diện tích và chu vi của nó'''
while True:
    try:
        side = float(input("Hãy nhập độ dài cạnh của hình vuông: "))
        if side > 0:
            print(f"Số có hợp lệ không? {side > 0}")
            break
        else:
            print("Độ dài cạnh phải là một số dương.")
            
    except ValueError:
        print("Hãy nhập lại một số hợp lệ.")
print(f"Diện tích hình vuông: {side ** 2:.1f}")
print(f"Chu vi hình vuông: {4 * side:.1f}")