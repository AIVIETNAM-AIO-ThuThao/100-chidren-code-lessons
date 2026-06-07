'''Bài 5: Theo quy định của nhà trường, mỗi trường hợp không đeo thẻ học sinh sẽ bị trừ a điểm thi đua
nói chuyện trong lớp bị trừ b điểm ; mỗi trường hợp đi học muộn bị trừ c điểm. 
Sổ đầu bài ghi nhận: có t trường hợp không đeo thẻ, n TH nói chuyện riêng, và m TH đi học muộn.
Hãy nhập các giá trị a, b, c, t, n, m từ bàn phím và tính tổng điểm bị trừ thi đua trong tháng đó.'''

TH = input("Hãy nhập lần lượt số TH không đeo thẻ, nói chuyện riêng, đi học muộn: ")
diem = input("Hãy nhập lần số điểm bị trừ khi ko đeo thẻ, nói chuyện riêng, đi học muộn: ")

lst = list(TH) + list(diem)
print(lst)
a = int(lst[0])
b = int(lst[1])
c = int(lst[2])
t = int(lst[3])
n = int(lst[4])
m = int(lst[5])
print(f"Tổng số điểm bị trừ là: {t*a + n*b + m*c}")


# Làm quen với map: map(hàm áp dụng, iterable)
a, b, c, t, n, m = map(int, list(TH) + list(diem)) #cho phép toán tử bên trong map
print(f"Tổng số điểm bị trừ là: {t*a + n*b + m*c}") # nếu ko khớp số lượng: 
#ValueError: not enough values to unpack


a, b, c, t, n, m = map(int, list(diem)*2)
print(list(diem)*2)
print(f"Tổng số điểm bị trừ là: {t*a + n*b + m*c}")