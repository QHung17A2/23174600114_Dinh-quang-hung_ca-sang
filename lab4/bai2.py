
n=int(input("nhập số nguyên từ bàn phím: "))
count=1
a=n
while True:
    a=a//10
    if a==0:
     break
    count+=1
print(f"số {n} có {count} chữ số")
