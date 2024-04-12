str1 = input("Nhập một chuỗi từ bàn phím: ")
str2 = ""
for i in str1:
    if i.isnumeric():
        str2 += i
print("Chuỗi chỉ gồm số sau khi tách từ chuỗi ban đầu là:", str2)
so_str2=int(str2)
for i in range(2,int(so_str2**0.5)+1):
    if so_str2%i==0 and so_str2%1==0:  
     break
print("chuỗi số đã tách là số nguyên tố ")