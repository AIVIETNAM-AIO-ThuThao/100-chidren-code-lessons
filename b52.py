'''Bài 52. Vừa gà vừa chó, bó lại cho tròn, ba mươi sáu con, một trăm chân chẵn. Hỏi mấy gà, mấy chó?'''
def solv_chicken_and_dog():
    found = False
    for chicken in range(37):
        dog = 36 - chicken
        if dog >= 0 and dog*4 + chicken*2 == 100:
            print(f"The number of chicken is {chicken}; the number of dog is {dog}")
            found = True
    if not found:
        print("No solution exists")
    return None
solv_chicken_dog()