chuoi_van_ban = input("Nhập chuỗi văn bản: ")
tu_can_tim = input("Nhập từ cần tìm kiếm: ")

vi_tri = []
bat_dau = 0
while True:
    bat_dau = chuoi_van_ban.find(tu_can_tim, bat_dau)
    if bat_dau == -1:
        break
    vi_tri.append(bat_dau)
    bat_dau += 1

if vi_tri:
    print(f"Từ '{tu_can_tim}' được tìm thấy tại các vị trí: {vi_tri}")
else:
    print(f"Từ '{tu_can_tim}' không được tìm thấy trong chuỗi.")

cac_tu = chuoi_van_ban.split()
dem_tu = {}
for tu in cac_tu:
    dem_tu[tu] = dem_tu.get(tu, 0) + 1
tu_xuat_hien_nhieu_nhat = max(dem_tu, key=dem_tu.get)
print(f"Từ xuất hiện nhiều nhất trong chuỗi là: '{tu_xuat_hien_nhieu_nhat}'")
