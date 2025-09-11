so_gio_lam=float(input("Nhap so gio làm mỗi tuần: "))
luong_gio=float(input("Nhap thù lao trên mỗi giờ làm tiêu chuẩn : "))
gio_tieu_chuan=44
gio_vuot_chuan=max(0,so_gio_lam-gio_tieu_chuan )
thuc_linh=luong_gio*gio_tieu_chuan+luong_gio*1.5*gio_vuot_chuan
print(f"số tiền thực lĩnh là: {thuc_linh}")