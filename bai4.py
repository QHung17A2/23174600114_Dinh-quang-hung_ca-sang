a.
def is_prime(n):
  """
  Hàm kiểm tra số n có phải là số nguyên tố hay không
  Args:
    n: Số nguyên cần kiểm tra
  Returns:
    True nếu n là số nguyên tố, False nếu không
  """
  if n <= 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

for i in range(100, 1001):
  if is_prime(i):
    print(i)

b.
 for i in range(1, 1001):
  print(i ** 2)

c.
a, b = 0, 1
while b < 100:
  print(a)
  a, b = b, a + b

d.
def tinh_tong_uoc_so(n):
  """
  Hàm này tính tổng các ước số của n (không bao gồm chính n)

  Tham số:
    n: Số nguyên dương

  Trả về:
    Tổng các ước số của n
  """
  tong_uoc_so = 1
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      tong_uoc_so += i + n // i
  return tong_uoc_so

def main():
  """
  Hàm chính để in ra các số hoàn hảo bé hơn 500
  """
  for i in range(2, 500):
    if tinh_tong_uoc_so(i) == i:
      print(i)

if __name__ == "__main__":
  main()
 
 e.
 def tinh_so_nguc_giac(n):
  """
  Hàm này tính số ngũ giác thứ n

  Tham số:
    n: Số nguyên dương

  Trả về:
    Số ngũ giác thứ n
  """
  return n * (3 * n - 1) // 2

def main():
  """
  Hàm chính để tính tổng các số ngũ giác trong đoạn từ 1 đến 200
  """
  tong = 0
  for i in range(1, 201):
    tong += tinh_so_nguc_giac(i)
  print(tong)

if __name__ == "__main__":
  main()
