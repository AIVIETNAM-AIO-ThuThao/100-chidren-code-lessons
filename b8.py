'''Bài 8. Viết chương trình Python cho phép nhập vào một kí tự c bất kì. 
Kiểm tra kí tự vừa nhập vào có thuộc Alphabet hay không. 
Nếu có thì in ra “la ki tu Alphabet” ngược lại in ra “khong phai la ki tu alphabet"'''
c = input("Hãy nhập 1 ký tự: ")
if (c >='a' and  <='z'or c >='A' and c<='Z'):
    print("Là kí tự Alphabet")
else:
    print("Không phải là kí tự Alphabet")