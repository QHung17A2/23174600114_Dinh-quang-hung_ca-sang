
# Nhập số hàng và số cột của ma trận
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

# Nhập ma trận từ người dùng
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        a = int(input(f"Nhập phần tử [{i+1}][{j+1}]: "))
        row.append(a)
    matrix.append(row)

# In ra ma trận
print("Ma trận vừa nhập:")
for row in matrix:
    print(row)

# Tính tổng của tất cả các phần tử trong ma trận
total = 0
for row in matrix:
    total += sum(row)
print("Tổng của tất cả các phần tử trong ma trận:", total)

# Nhập ma trận thứ hai
print("Nhập ma trận thứ hai để tính tích:")
m2=int(input("Nhập số hàng của ma trận thứ hai: "))
n2=int(input("Nhập số cột của ma trận thứ hai: "))
matrix2 = []
for i in range(m2):
    row = []
    for j in range(n2):
        b = int(input(f"Nhập phần tử [{i+1}][{j+1}]: "))
        row.append(b)
    matrix2.append(row)

# Tính tích của hai ma trận
if len(matrix[0]) != len(matrix2):
    print("Không thể nhân hai ma trận này.")
else:
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix2[0])):
            sum_2 = 0
            for k in range(len(matrix2)):
                sum_2 += matrix[i][k] * matrix2[k][j]
            row.append(sum_2)
        result.append(row)
    print("Tích của hai ma trận:")
    for row in result:
        print(row)

# Ma trận chuyển vị
print("Ma trận chuyển vị:")
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for row in transpose:
    print(row)
