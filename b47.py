'''Bài 47. Viết chương trình tìm các số hoàn hảo nhỏ hơn n 
(Với n được nhập từ bàn phím)'''
n = int(input("Enter a positive integer n: "))

print(f"\nPerfect numbers less than {n}:")

for num in range(2, n):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num:
        print(num, end=" ")
