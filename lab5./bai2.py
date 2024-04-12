str1=input("nhập chuỗi thứ nhất:")
str2=input("nhập chuỗi thứ hai:")
chuoi_con=""  
min_chuoi="" 
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            k = 0
            while (i + k) < len(str1) and (j + k) < len(str2) and str1[i+k] == str2[j + k]:
                chuoi_con += str1[i + k]
                k += 1 
            if len(chuoi_con) > len(min_chuoi):
                min_chuoi = chuoi_con
            chuoi_con = ""
print("Chuỗi ký tự con chung của 2 chuỗi đã cho và có độ dài ngắn nhất là:", min_chuoi)