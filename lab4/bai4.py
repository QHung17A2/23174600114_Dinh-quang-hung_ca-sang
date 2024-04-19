
while True:
    a,b=map(int,input("Nhập lần lượt 2 số là: ").split())
    print("1.phép tính tổng")
    print("2.phép tính hiệu")
    print("3.phép tính tích")
    print("4.phép tính thương")
    print("5.phép tính lũy thừa")
    print("6.phép tính căn bậc hai")
    lua_chon=int(input("Lựa chọn của bạn là:"))
    if  lua_chon == 1:
        print("Tổng =", a + b)
    elif lua_chon == 2:
        print("Hiệu =", a - b)
    elif  lua_chon == 3:
        print("Tích =", a * b)
    elif  lua_chon == 4:
        if b == 0:
            print("Không thể chia cho số 0")
        else:
            print("Thương =", a / b)
    elif lua_chon == 5:
        print("Lũy thừa =", a ** b)
    elif  lua_chon == 6:
        if a < 0:
            print("Không thể tính căn bậc hai của số âm")
        else:
            print("Căn bậc hai của số thứ nhất =",a**0.5)
        if b < 0:
            print("Không thể tính căn bậc hai của số âm")
        else:
            print("Căn bậc hai của số thứ hai =", b**0.5)
    else:
        print("Lựa chọn không hợp lệ")
    tiep_tuc = input("Bạn có muốn tiếp tục không ạ(có/không) : ")
    if tiep_tuc != 'có':
        break