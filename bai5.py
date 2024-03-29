def ve_hinh_tam_giac(so_dong):
  """
  Hàm này vẽ hình tam giác với số dòng cho trước

  Tham số:
    so_dong: Số dòng của hình tam giác

  """
  for i in range(1, so_dong + 1):
    # In ra số dấu * bằng với số dòng hiện tại
    print("*" * i)

# Vẽ hình tam giác 1
ve_hinh_tam_giac(3)

print()

# Vẽ hình tam giác 2
ve_hinh_tam_giac(4)
