str=input("nhập chuỗi: ")
chu_thuong=0
chu_so=0
chu_hoa=0
ky_tu_dac_biet=0
for char in str:
    if char.islower():
        chu_thuong+=1
    elif char.isupper():
        chu_hoa+=1
    elif char.isdigit():
        chu_so+=1
    else:
        ky_tu_dac_biet+=1
print("Chữ hoa trong chuỗi là:",chu_hoa)
print("Chữ thường trong chuỗi là:",chu_thuong)
print("Chữ số trong chuỗi là:",chu_so)
print("Ký tự đặc biệt trong chuỗi là:",ky_tu_dac_biet)            