'''Bài 49. Viết chương trình tìm tất cả các số có 3 chữ số abc
 sao cho abc = a^3+b^3+c^3'''
numbers = []
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if a*100 + b*10 + c == a**3 + b**3 + c**3:
                numbers.append(a*100+b*10+c)
if numbers:
    print(
        f"All three-digit numbers that are "
    f"equal to the sum of the cubes of their digits are {numbers}"
        )
else:
    print("No solution found")