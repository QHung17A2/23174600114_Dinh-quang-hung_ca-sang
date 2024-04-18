
#a.
n=int(input("nhập số n: "))
fib_list=[0,1]
[fib_list.append(fib_list[-1]+fib_list[-2]) for _ in range(2,n+1)]
print("Danh sách chứa {n} số Fibonacci đầu tiên là: ",fib_list)
#b
num=[n for n in range(2,100) if all (n%i!=0 for i in range(2,int(n**0.5)+1))]
print("Danh sách chứa tất cả các số nguyên tố nhỏ hơn 100 là: ",num)
