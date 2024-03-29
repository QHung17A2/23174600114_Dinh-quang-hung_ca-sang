def tinh_tong_s1(n):
  """
  Hàm tính tổng S1 = 1 + 2 + 3 + ... + n
  Args:
    n: Số nguyên dương
  Returns:
    Tổng S1 = 1 + 2 + 3 + ... + n
  """
  if n <= 0:
    return "n phải là số nguyên dương!"
  return n * (n + 1) // 2

def tinh_tong_s2(n):
  """
  Hàm tính tổng S2 = 1/1 + 1/2 + 1/3 + ... + 1/n
  Args:
    n: Số nguyên dương
  Returns:
    Tổng S2 = 1/1 + 1/2 + 1/3 + ... + 1/n
  """
  if n <= 0:
    return "n phải là số nguyên dương!"
  tong = 0
  for i in range(1, n + 1):
    tong += 1 / i
  return tong

def tinh_tong_s3(n):
  """
  Hàm tính tổng S3 = 1/√2 + 1/√4 + 1/√6 + ... + 1/√2n
  Args:
    n: Số nguyên dương
  Returns:
    Tổng S3 = 1/√2 + 1/√4 + 1/√6 + ... + 1/√2n
  """
  if n <= 0:
    return "n phải là số nguyên dương!"
  tong = 0
  for i in range(1, n + 1):
    tong += 1 / math.sqrt(2 * i)
  return tong

def tinh_tong_s4(n):
  """
  Hàm tính tổng S4 = 1/1 - 1/2 + 1/3 - 1/4 + ... + (-1)^n/n
  Args:
    n: Số nguyên dương
  Returns:
    Tổng S4 = 1/1 - 1/2 + 1/3 - 1/4 + ... + (-1)^n/n
  """
  if n <= 0:
    return "n phải là số nguyên dương!"
  tong = 0
  for i in range(1, n + 1):
    tong += (-1)**(i-1) / i
  return tong