s1=input("nhập chuỗi 1:")
s2=input("nhập chuỗi 2:")
if len(s1) != len(s2):
  print(f"Không thể biến đổi '{s1}' thành '{s2}'")
  exit()
diff_count = 0
for i in range(len(s1)):
  if s1[i] != s2[i]:
    diff_count += 1
if diff_count > 1:
  print(f"Không thể biến đổi '{s1}' thành '{s2}'")
else:
  print(f"Có thể biến đổi '{s1}' thành '{s2}'")