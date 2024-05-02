
#a,
sinh_vien={}
for i in range(10):
    ten_sv=input("Nhập tên của sinh viên {}: ".format(i+1))
    diem_thi=float(input("Nhập điểm thì của sinh viên {}: ".format(i+1)))
    sinh_vien[ten_sv]=diem_thi
print("Danh sách sinh viên là:",sinh_vien)    
xep_loai={'A':0,'B':0,'C':0,'D':0,'F':0} 
for ten_sv,diem_thi in sinh_vien.items():
    if diem_thi>= 8.5:
        xep_loai['A']+=1
    elif diem_thi>=7.0:
        xep_loai['B']+=1
    elif diem_thi>=5.5:
        xep_loai['C']+=1  
    elif diem_thi>=4.0:
        xep_loai['D']+=1 
    else:
        xep_loai['F']+=1        
for ten_sv,diem_thi in sinh_vien.items():
    xep_loai_hoc_luc=''
    if diem_thi>=8.5:
        xep_loai_hoc_luc='A'
    elif diem_thi>=7.0:
        xep_loai_hoc_luc='B'
    elif diem_thi>=5.5:
        xep_loai_hoc_luc='C'
    elif diem_thi>=4.0:
        xep_loai_hoc_luc='D'  
    else:
        xep_loai_hoc_luc='F'
    print("{}:{}".format(ten_sv,xep_loai_hoc_luc))        
print("Xếp loại học lực: ",xep_loai_hoc_luc)   
#b.
print("Thống kê mỗi loại học lực là:")
for xep_loai_hoc_luc,so_luong in xep_loai.items():
    print("{}:{}".format(xep_loai_hoc_luc,so_luong))            
