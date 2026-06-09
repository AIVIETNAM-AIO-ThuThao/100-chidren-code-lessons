'''Bài 36. Bạn hãy nhập vào số n (Integer) rồi in ra màn hình 
kết quả của phép toán Cộng các số chẵn từ 1 đến n.'''
def sum_even_number(n):
    for i in range (n+1):
        sum = 0
        if i % 2 == 0:
            sum += i
    return sum
n = 20
print(f"Tổng các số chẵn từ 1 đến {n} là: {sum_even_number(n)}")