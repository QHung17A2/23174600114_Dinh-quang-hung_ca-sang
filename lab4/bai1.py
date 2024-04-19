#a.
a=1
print("số nguyên tố nhỏ hơn 100 là: ")
while a<100:
    check= True
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            check=False
            break
    if check:
        print(a,end=" ")
    a+=1
#b.
a=1
print("các số chính phương nhỏ hơn 100 là: ")
while a*a<100:
    print(a*a,end="      ")
    a+=1
#c.
a,b=0,1
print("   số Fibonacci nhỏ hơn 1000 là: ")
while b<1000:
    a,b=b,a+b
    print(a,end=" ")    