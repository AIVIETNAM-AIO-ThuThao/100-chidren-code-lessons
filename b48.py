'''Bài 48. Số chính phương là số mà căn bậc hai của nó là 1 số nguyên dương. 
nhập vào một số nguyên dương n và cho biết 
n có phải là số chính phương hay không?'''
n = int(input("Enter a postive integer: "))
if (n**0.5).is_integer():           # or if int(n**0.5)**2 == n
    print(f"{n} is a perfect square")
else:
    print(f"{n} is not perfect square")