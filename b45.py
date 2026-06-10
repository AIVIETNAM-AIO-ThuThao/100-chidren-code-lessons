'''Bài 45. Nhập vào một số nguyên không âm, 
kiểm tra xem nó có phải là số nguyên tố hay không?'''
while True:
    try:
        n = int(input("Enter a positive integer greater than 1: "))
        if n <= 1:
            print("n must be greater than 1")
            continue
        for i in range(2, int(n**2)+1):       #n**2 trả về float trong khi range chỉ nhận int
            if n%i == 0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is a prime number")
        break
    except(TypeError, ValueError):
        print("Enter a valid value")
    