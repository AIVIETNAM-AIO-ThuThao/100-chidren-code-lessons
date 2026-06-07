'''Bài 19. '''
a, b = map(float, input("Hãy nhập vào 2 số a và b trong pt 'ax + b >0': ").split())
if a == 0:
    if b <= 0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình có vô số nghiệm")
else:
    print(f"Phương trình có 1 nghiệm là: x > {-b/a:.2f}")






def giai_bat_phuong_trinh(a, b, loai=">"):
    """
    Giải bất phương trình ax + b > 0 (hoặc ≥, <, ≤)
    loai: ">", ">=", "<", "<="
    """
    if a == 0:
        if b > 0:
            return "Vô số nghiệm" if ">" in loai else "Vô nghiệm"
        elif b < 0:
            return "Vô nghiệm" if ">" in loai else "Vô số nghiệm"
        else:  # b == 0
            return "Vô số nghiệm" if ">=" in loai or "<=" in loai else "Vô nghiệm"
    
    nghiem = -b / a
    
    if a > 0:
        if loai == ">":
            return f"x > {nghiem}"
        elif loai == ">=":
            return f"x ≥ {nghiem}"
        elif loai == "<":
            return f"x < {nghiem}"
        else:  # <=
            return f"x ≤ {nghiem}"
    else:  # a < 0
        if loai == ">":
            return f"x < {nghiem}"
        elif loai == ">=":
            return f"x ≤ {nghiem}"
        elif loai == "<":
            return f"x > {nghiem}"
        else:  # <=
            return f"x ≥ {nghiem}"

# Ví dụ sử dụng
print(giai_bat_phuong_trinh(2, -4, ">"))   # 2x - 4 > 0 → x > 2.0
print(giai_bat_phuong_trinh(-3, 6, ">="))  # -3x + 6 ≥ 0 → x ≤ 2.0
print(giai_bat_phuong_trinh(1, 5, "<"))    # x + 5 < 0 → x < -5.0