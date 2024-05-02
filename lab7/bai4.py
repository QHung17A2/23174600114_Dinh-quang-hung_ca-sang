kho={
    "banana":6,
    "apple":5,
    "orange":32,
    "pear":15
}
gia_tien={
    "banana":4,
    "apple":2,
    "orange":1.5,
    "pear":3
}
hoa_don = {}
tong_tien = 0
mua_hang = {
    "banana": 2,
    "orange": 3,
    "pear": 1
}
for mat_hang, so_luong in mua_hang.items():
    if mat_hang in kho and kho[mat_hang] >= so_luong:
        don_gia = gia_tien[mat_hang]
        thanh_tien = don_gia * so_luong
        tong_tien += thanh_tien
        kho[mat_hang] -= so_luong
        hoa_don[mat_hang] = {
            "so_luong": so_luong,
            "don_gia": don_gia,
            "thanh_tien": thanh_tien
        }

print("Hóa đơn mua hàng:")
for mat_hang, thong_tin in hoa_don.items():
    print("Mặt hàng: {}, Số lượng: {}, Đơn giá: ${}, Thành tiền: ${}".format(mat_hang, thong_tin["so_luong"], thong_tin["don_gia"], thong_tin["thanh_tien"]))
print("Tổng số tiền của hóa đơn: ${}".format(tong_tien))

print("\nSố lượng của các mặt hàng trong kho:")
for mat_hang, so_luong in kho.items():
    print("{}: {}".format(mat_hang, so_luong))