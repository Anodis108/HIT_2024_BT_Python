class HITer:
    '''
    Class này chứa danh sách tất cả HITer trong clb
    '''
    
    danhsach = []
    
    def __init__(self, id, ten, tuoi, gen) -> None:
        self.id = id
        self.ten = ten
        self.tuoi = tuoi
        self.gen = gen
        HITer.danhsach.append(self)
        
    def __str__(self) -> str:
        return f'ID: {self.id}, Ten: {self.ten}, Tuoi: {self.tuoi}, Gen: {self.gen}'    
    
    @classmethod
    def nhap(cls):
        print('Nhập thông tin HITer')
        id = input('ID: ')
        ten = input('TEN: ')
        tuoi = input('Tuổi: ')
        gen = input('Gen: ')
        return HITer(id, ten, tuoi, gen)

    @classmethod
    def indanhsach(cls):
        for i in cls.danhsach:
            print(i)
            
class Ban:
    danhSachBan = []
    
    def __init__(self, id_ban , ten_ban , truongban: HITer, thanhvien:list) -> None:
        self.id_ban = id_ban
        self.ten_ban = ten_ban
        self.truongban = truongban
        self.thanhvien = thanhvien
      
    @classmethod  
    def nhap(cls):
        id_ban = input('ID Ban: ')
        ten_ban = input('Ten ban: ')
        truongban = input('ID truong ban la: ')
        check = False
        for i in HITer.danhsach:
            if i.id == truongban:
                truongban = i
                check = True
                break
        if check == False: 
            print('ID sai, hãy nhập lại')
                
        thanhvien = []
        return Ban(id_ban, ten_ban, truongban, thanhvien)
    
    def __str__(self) -> str:
        return f'idBan: {self.id_ban}, Ten Ban: {self.ten_ban}, truongBan: {self.truongban}'
    
    # In ra danh sách thành viên của ban
    def dsHiter(self) -> None:
        for i in self.thanhvien:
            print(i)
    # Xóa 1 HITer khỏi ban    
    def xoa(self, id):
        for i in self.thanhvien:
            if i.id == id:
                self.thanhvien.remove(i)
                break
            
    # Thêm 1 HITer vào ban
    def add(self, HITer:HITer):
        check = True
        for i in self.thanhvien:
            if i.id == HITer.id:
                check = False
        if check:
            self.thanhvien.append(HITer)
        else:
            print('Thành viên này đã có trong danh sách')
            
def main():
    n = int(input('Số lượng HITer : '))
    for i in range(n):
        hiter = HITer.nhap()
        HITer.danhsach.append(hiter)
        
    m = int(input('Số lượng ban : '))
    for i in range(m):
        ban = Ban.nhap()
        Ban.danhSachBan.append(ban)
        
    # Thao tác với 1 ban bất kỳ
    ban = input('Nhập id ban cần xóa 1 HITer: ')
    for i in Ban.danhSachBan:
        if i.id_ban == ban:
            ban = i
            print(ban)
            
            # Xóa 1 HITer
            hiter = input('Nhập ID HITer cần xóa ')
            for j in ban.thanhvien:
                if j.id == hiter:
                    ban.xoa(j.id)
                    break
            
            # In ra ban sau khi xoa
            ban.dsHiter()
            
            # Thêm 1 HITer vào ban
            idhiter = input('Nhập ID hiter cần them: ')
            for j in HITer.danhsach:
                if j.id == idhiter:
                    ban.add(j)
                    break
            # In ra ban sau khi thêm
            ban.dsHiter()
            break
        
    # Thêm 1 HITer vào ban đó

if __name__ == '__main__':
    main()