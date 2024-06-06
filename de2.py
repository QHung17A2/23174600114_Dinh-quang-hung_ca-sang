import random
import csv

# Hàm để mô phỏng tung đồng xu với xác suất tùy chỉnh
def lat_xu(xac_suat_mat_ngua=0.7):
    return random.choices(['Ngửa', 'Sấp'], [xac_suat_mat_ngua, 1 - xac_suat_mat_ngua])[0]

# Hàm để tính xác suất xuất hiện của mỗi kết quả
def tinh_xac_suat(ket_qua):
    tong_lan_lat = len(ket_qua)
    xac_suat = {
        'Ngửa': ket_qua.count('Ngửa') / tong_lan_lat,
        'Sấp': ket_qua.count('Sấp') / tong_lan_lat
    }
    return xac_suat

# Hàm chính để chạy mô phỏng
def mo_phong_lat_xu(so_lan_lat=1000, xac_suat_mat_ngua=0.7):
    ket_qua = []
    tap_hop_ket_qua = set()
    xac_suat_ket_qua = {}

    for _ in range(so_lan_lat):
        ket_qua_lat = lat_xu(xac_suat_mat_ngua)
        ket_qua.append(ket_qua_lat)
        tap_hop_ket_qua.add(ket_qua_lat)

    xac_suat_ket_qua = tinh_xac_suat(ket_qua)

    # Lưu kết quả vào file CSV với mã hóa UTF-8
    with open('ket_qua_lat_xu.csv', 'w', newline='', encoding='utf-8') as csvfile:
        truong_du_lieu = ['Lần Lật', 'Kết Quả', 'Xác Suất Ngửa', 'Xác Suất Sấp']
        writer = csv.DictWriter(csvfile, fieldnames=truong_du_lieu)
        writer.writeheader()

        for i, ket_qua_lat in enumerate(ket_qua):
            writer.writerow({
                'Lần Lật': i + 1,
                'Kết Quả': ket_qua_lat,
                'Xác Suất Ngửa': xac_suat_ket_qua['Ngửa'],
                'Xác Suất Sấp': xac_suat_ket_qua['Sấp']
            })

    print(f"Mô phỏng hoàn thành. Kết quả đã được lưu vào 'ket_qua_lat_xu.csv'.")

# Chạy mô phỏng
mo_phong_lat_xu()