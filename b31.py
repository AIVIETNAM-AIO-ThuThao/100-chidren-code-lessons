'''Bảng của đồng hồ điện tử gồm một dãy ba số h, p và s thể hiện tương ứng giờ, phút và giây của thời điểm hiện tại. 
Cứ sau mỗi giây giá trị của bộ ba số h, p và s này sẽ thay đổi thành 3 số h1, p1 và s1 tương ứng với thời điểm mới. 
hãy tìm 3 số h1, p1 và s1 và in kết quả ra màn hình'''
while True:
    try:
        h, p, s = map(int, input("Hãy nhập vào số giờ, phút, giây của hiện tại: ").split())
        if not (0 <= h <= 23 and 0 <= p <= 59 and 0 <= s <= 59):
            print("Nhập sai số!")
            continue
        s += 1          #gán tăng số giây trước
        if s == 60:
            s = 0
            p += 1
            if p == 60:
                p = 0
                h += 1
                if h == 24:
                    h = 0
        print (f"Sau 1 s ta có: {h}: {p}: {s}")
    except (ValueError, TypeError):
        print("Hãy nhập đúng định dạng số!")
