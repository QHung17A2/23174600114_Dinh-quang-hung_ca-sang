
n=input("nhập dãy các số cách nhau 1 dấu cách:").split()
n=[float(num) for num in n]
max=max(n)
min=min(n)
print(f"Số lớn nhất trong các số là:{max}")
print(f"Số bé nhất trong các số là:{min}")
