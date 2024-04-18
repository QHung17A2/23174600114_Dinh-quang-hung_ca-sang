n=int(input("nhập số nguyên n: "))
mang_so=[]
for i in range(n):
    a=int(input("nhập vào phần tử: "))
    mang_so.append(a)
print(mang_so) 
print("Các số nguyên tố trong mảng vừa nhập là: ")
for b in mang_so:
    if b > 1:
        for i in range(2,int(b**0.5)+1):
            if b%i==0 and b%1==0:
                break
        else:       
            print(b)
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i
if sum==a:
    print("Các số hoàn hảo trong mảng vừa nhập là:",sum)        