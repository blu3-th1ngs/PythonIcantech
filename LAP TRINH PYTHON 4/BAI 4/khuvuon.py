class Game:
    tien = 5000
    so_luong = 0

    def __init__(self, ten):
        self.ten = ten
        self.nuoc = 0
        self.anh_sang = 0
        Game.so_luong += 1
        Game.tien -= 200

    @property  
    def tinh_trang(self):  
        if (self.nuoc == None and self.anh_sang == None):  
            return 'đã bán'  
        elif (self.nuoc == 0 and self.anh_sang == 0):  
            return 'hạt mầm'  
        elif (self.nuoc > 0 and self.anh_sang > 0):  
            return 'sống'  
        else:  
            return 'chết'

    @property  
    def gia_thanh(self):  
        if (self.nuoc == None and self.anh_sang == None):  
            return 0  
        return max(0, self.nuoc + self.anh_sang*10)  
      
    @gia_thanh.setter  
    def gia_thanh(self, value):  
        nuoc_tang_them, anh_sang_tang_them = value  
        if (nuoc_tang_them > 100 or anh_sang_tang_them > 10):  
            self.nuoc = -1  
            self.anh_sang = -1  
        elif self.check_tinh_trans():  
            self.nuoc += nuoc_tang_them  
            self.anh_sang += anh_sang_tang_them  

    @gia_thanh.deleter  
    def gia_thanh(self):  
        Game.tien += self.gia_thanh  
        self.nuoc = None  
        self.anh_sang = None

    @staticmethod  
    def cham_cay():
        ten = input("Tên cây bạn muốn chăm là: ")
        for i in range(Game.so_luong):
            if game[i].ten == ten and game[i].check_tinh_trans():
                nuoc_tang_them = int(input("Bạn muốn tưới bao nhiêu ml nuốc?"))
                anh_sang_tang_them = int(input("Bạn sẽ để cây ngoài trời mấy tiếng?"))
                if game[i].nuoc is not None and game[i].anh_sang is not None:
                    game[i].gia_thanh = (nuoc_tang_them, anh_sang_tang_them)
                print(game[i])
                return True
            else:
                print("Cây đã bán hoặc không tồn tại. Hãy nhập lại tên.")
                return False
        print("Cây không tồn tại hoặc không còn sống. Hãy nhập lại tên.")
        return False

    @staticmethod
    def ban_cay():
        ten = input("Cây bán tên là: ")
        for i in range(Game.so_luong):
            if game[i].ten == ten and game[i].check_tinh_trans():
                del game[i].gia_thanh
                break
            else:
                print("===== Hãy nhập lại tên ====")
                return False
        return True

    def check_tinh_trans(self):
        if self.tinh_trang == 'sống' or 'hạt mầm':
            return True
        else:
            return False

    def get_info(self):
        return f"Cây {self.ten} có tính trạng là {self.tinh_trang}, chiều cao là: {self.gia_thanh} mm"


game = []
while True:
    print("Chọn một trong các tùy chọn sau:")
    print("1. Thêm cây mới")
    print("2. Chăm sóc cây")
    print("3. Bán cây")
    print("4. Xem danh sách các cây")
    print("5. Thoát chương trình")
    print(f"Bạn đang có {Game.tien} đồng")

    choice = input("Nhập lựa chọn của bạn (1-5): ")
    if choice == "1":
        ten = input("Bạn muốn đặt cây tên là: ")
        game.append(Game(ten=ten))
        print(f"Bạn đã thêm cây {ten} thành công")
    elif choice == "2":
        Game.cham_cay()
    elif choice == "3":
        Game.ban_cay()
    elif choice == "4":
        for i in range(Game.so_luong):
            print(f"{i+1}.{game[i].get_info()}")
    elif choice == "5":
        break
    else:
        print("Lựa chọn không hợp lệ. Hãy chọn lại.")