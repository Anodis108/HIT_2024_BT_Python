class PhanSo:
    def __init__(self, tu : int, mau : int):
        self.tu = tu
        self.mau = mau
    
    def __mul__(self, other) -> tuple:
        # In ra lỗi nếu mẫu bằng 0
        if self.mau == 0 or other.mau == 0:
            raise ValueError("Multiplication by zero is not allowed.")
        
        x = self.tu * other.tu
        y = self.mau * other.mau
        
        # Chuyển về phân số tối giản
        gcd = self.GCD(max(x, y), min(x, y))
        x,y = x//gcd, y//gcd
        
        return PhanSo(x,y) # return new obj PhanSo

    def __str__(self) -> str:
        return 'Phân số cần hiện là {}/{}'.format(self.tu, self.mau)
    
    def GCD(self, x : int, y : int) -> int:
        ''' 
        Hàm trả về ước chung lớn nhất của tử và mẫu
        
        parameters:
            x: tử số
            y: mẫu số
            
        Returns:
            Ước chung lớn nhất của x và y
        '''
        if y == 0:
            return x
        return self.GCD(y, x % y)
        
def main():
    n = int(input())
    a = PhanSo(1, 1)
    for i in range(n):
        tu, mau = list(map(int, input().split(' ')))
        a = a * PhanSo(tu, mau)
    print(a)

if __name__ == '__main__':
    main()