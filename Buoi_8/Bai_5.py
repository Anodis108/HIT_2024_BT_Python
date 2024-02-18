from math import gcd

class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    @staticmethod
    def hon_so_to_phan_so(hon_so):
        phan_nguyen, tu_so, mau_so = int(hon_so.split())
        tu_so = phan_nguyen * mau_so + tu_so
        return PhanSo(tu_so, mau_so)

    def rut_gon(self):
        ucln = gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln
        return self

class HonSo:
    def __init__(self, phan_nguyen, phan_so):
        self.phan_nguyen = phan_nguyen
        self.phan_so = phan_so

    @staticmethod
    def phan_so_to_hon_so(phan_so):
        phan_nguyen = phan_so.tu_so // phan_so.mau_so
        phan_so.tu_so %= phan_so.mau_so
        return HonSo(phan_nguyen, phan_so)

class Math(PhanSo, HonSo):
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        if isinstance(self.a, PhanSo) and isinstance(other.a, HonSo):
            self.a = self.hon_so_to_phan_so(str(other.a))
        elif isinstance(self.a, HonSo) and isinstance(other.a, PhanSo):
            other.a = self.phan_so_to_hon_so(other.a)
        tu_so = self.a.tu_so * other.a.mau_so + other.a.tu_so * self.a.mau_so
        mau_so = self.a.mau_so * other.a.mau_so
        return PhanSo(tu_so, mau_so).rut_gon()

    def __mul__(self, other):
        if isinstance(self.a, PhanSo) and isinstance(other.a, HonSo):
            self.a = self.hon_so_to_phan_so(str(other.a))
        elif isinstance(self.a, HonSo) and isinstance(other.a, PhanSo):
            other.a = self.phan_so_to_hon_so(other.a)
        tu_so = self.a.tu_so * other.a.tu_so
        mau_so = self.a.mau_so * other.a.mau_so
        return PhanSo(tu_so, mau_so).rut_gon()

# Nhập phân số và hỗn số
tu_so, mau_so = map(int, input("Nhập tử số và mẫu số của phân số: ").split())
phan_so = PhanSo(tu_so, mau_so)
phan_nguyen, tu_so, mau_so = map(int, input("Nhập phần nguyên, tử số và mẫu số của hỗn số: ").split())
hon_so = HonSo(phan_nguyen, PhanSo(tu_so, mau_so))

# Đổi a thành hỗn số và b thành phân số
a = Math(hon_so)
b = Math(phan_so)

# In lại a, b lên màn hình
print("a (hỗn số):", a.a.phan_nguyen, a.a.phan_so.tu_so, a.a.phan_so.mau_so)
print("b (phân số):", b.a.tu_so, b.a.mau_so)

# In ra kết quả của a+b, b+a, a*b và b*a
print("a + b =", (a+b).tu_so, "/", (a+b).mau_so)
print("b + a =", (b+a).tu_so, "/", (b+a).mau_so)
print("a * b =", (a*b).tu_so, "/", (a*b).mau_so)
print("b * a =", (b*a).tu_so, "/", (b*a).mau_so)