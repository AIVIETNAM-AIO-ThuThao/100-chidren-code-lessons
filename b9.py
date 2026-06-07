'''Bài 9. Tính tiền điện
Nhập vào họ tên một chủ hộ, chỉ số điện kế tháng trước (chiso1) và chỉ số điện kế tháng này (chiso2), tính tiền điện tháng này cho hộ, biết rằng:
Mỗi kw trong 60 kw đầu tiên có đơn giá là 5 nghìn đ,
Từ kw thứ 61 đến kw thứ 160 có đơn giá 8 nghìn đ,
Từ kw thứ 161 trở lên có đơn giá 10 nghìn đ.'''
def bill(chi_so1, chi_so2):
    total = chi_so2 - chi_so1
    if total <= 60:
        money = total * 5
    elif total <= 160:
        money = 60 * 5 + (total - 60) * 8
    else:
        money = 60 * 5 + 100 * 8 + (total - 160) * 10
    return money

while True:
    house_owner = input("Hãy nhập tên chủ hộ: ").strip()        # loại bỏ space trước và sau
    if house_owner == "":
        print("Không được để trống tên!")
        continue
    valid = True            # gắn cờ trạng thái giả định
    for word in house_owner.split():
        if not word.isalpha():
            valid = False
            break
    if not valid:
        print("Tên chỉ được chứa chữ cái!")
        continue

    break
print("Tên hợp lệ:", house_owner)

chi_so1, chi_so2 = map(float, input("Hãy nhập chỉ số điện tháng trước và tháng này: ").split)

print(f"Tiền điện phải trả của {house_owner}: {bill(chi_so1, chi_so2):.1f} nghìn đồng")

# Kiểm tra tên hợp lệ khi không gắn cờ:
while True:
    house_owner = input("Hãy nhập tên chủ hộ: ").strip()

    if house_owner == "":
        print("Không được để trống tên!")
        continue

    if not all(word.isalpha() for word in house_owner.split()): # pythonic
        print("Tên chỉ được chứa chữ cái và khoảng trắng!")
        continue
    break

print("Tên hợp lệ:", house_owner)