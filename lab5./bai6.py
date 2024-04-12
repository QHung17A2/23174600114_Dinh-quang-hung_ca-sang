string = input("Nhập chuỗi: ")
special_chars = {}
for char in string:
  if not char.isalnum():
    special_chars.setdefault(char, 0)
    special_chars[char] += 1
total_chars = len(string)
for char, count in special_chars.items():
  percentage = round(count / total_chars * 100, 2)

  print(f"- Ký tự '{char}':")
  print(f"  + Số lần xuất hiện: {count}")
  print(f"  + Tỷ lệ phần trăm: {percentage}%")
  