
str=input("nhập vào dãy số cách nhau bằng dấu cách: ")
s=list(map(int,str.split()))
if len(s)<2:
    print("dãy số chỉ có 1 or không số nên kh thể tạo thành cấp số cộng")
else:
    d=s[1]-s[0]    
    check=True
    for i in range(2,len(s)):
        if s[i]-s[i-1]!=d:
            check=False
            break
if check:
    print("dãy số",s,"tạo thành cấp số cộng")
else:
    print("dãy số",s,"không tạo thành cấp số cộng")       
         
