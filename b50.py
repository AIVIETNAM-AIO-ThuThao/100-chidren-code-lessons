'''Bài 50. Viết chương trình tìm tất cả các số có 3 chữ số 
sao cho tổng tất cả các chữ số bằng tích của chúng.'''
numbers = []
for x in range(1, 10):
    for y in range(10):
        for z in range(10):
            if x + y + z == x * y * z:
                numbers.append(x*100 + y*10 + z)
print(f"All three-digit numbers such that \
the sum of their digits equals the product of their digits are {numbers}")
