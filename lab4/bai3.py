n = int(input("Nhập số nguyên n từ bàn phím: "))
if n <= 10:
    print("Vui lòng nhập lại!")
else:
    a = 1
    S1 = 0
    S2 = 0
    S3 = 0
    S4 = 0
    while a <= n:
        S1 = S1 + (6**a)
        S2 = S2 + (1/3**(2*a+1))
        S3 = S3 + (-1)**a * (a - 1)**2
        S4 = S4 + (a*(a+1)*(a+2))
        a += 1
    print("Tổng của S1 là:", S1)
    print("Tổng của S2 là:", S2)
    print("Tổng của S3 là:", S3)
    print("Tổng của S4 là:", S4)
