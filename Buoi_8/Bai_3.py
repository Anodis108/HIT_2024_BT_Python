class Matrix:
    def __init__(self, rows, cols, data) -> None:
        self.rows = rows
        self.columns = cols
        self.data = data
        
    def __mul__(self, other): # nhân 2 ma trận
        if self.columns != other.rows:
            raise ValueError("Số cột của ma trận thứ nhất phải bằng số hàng của ma trận thứ hai")
        
        result = Matrix(self.rows, other.columns, [[0 for i in range(other.columns)] for j in range(self.rows)])
        
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        
        return result
    
    def __add__(self, other): # Cộng 2 ma trận
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Kích thước ma trận không khớp")

        result = Matrix(self.rows, self.columns, [[0 for i in range(self.columns)] for j in range(self.rows)])

        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result
    
    def __sub__(self, other): # trừ 2 ma trận
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Kích thước ma trận không khớp")

        result = Matrix(self.rows, self.columns, [[0 for i in range(self.columns)] for j in range(self.rows)])

        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] - other.data[i][j]

        return result
    
    def __truediv__(self, other): # nhân ma trận trái với nghịch đảo ma trận phải
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Kích thước ma trận không khớp")

        if not other.is_invertible():
            raise ValueError("Ma trận thứ hai không có nghịch đảo")

        inverse = other.get_inverse()

        return self * inverse
    
    def __eq__(self, other): # so sánh
        if self.rows != other.rows or self.columns != other.columns:
            return False

        for i in range(self.rows):
            for j in range(self.columns):
                if self.data[i][j] != other.data[i][j]:
                    return False

        return True
    
    def __repr__(self):
        return f"Matrix({self.rows}, {self.columns}):\n{self.data}"
    
    def is_invertible(self):
        if self.rows != self.columns:
            return False

        for i in range(self.rows):
            if self.data[i][i] == 0:
                return False

        return True

    def get_inverse(self):
        if not self.is_invertible():
            raise ValueError("Ma trận không có nghịch đảo")

        inverse = Matrix(self.rows, self.columns, [[0 for i in range(self.columns)] for j in range(self.rows)])

        for i in range(self.rows):
            for j in range(self.columns):
                if i == j:
                    inverse.data[i][j] = 1 / self.data[i][i]
                else:
                    inverse.data[i][j] = -self.data[i][j] / self.data[i][i]

        return inverse
    
def main():
    matrix_a = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
    matrix_b = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])

    matrix_c = matrix_a + matrix_b

    print('Cộng', matrix_c)
    
    matrix_c = matrix_a - matrix_b

    print('Trừ',matrix_c)
        
    matrix_d = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])

    matrix_e = matrix_a * matrix_d

    print('Nhân', matrix_e)
    
    matrix_f = matrix_a / matrix_d

    print('Nhân ma trận trái với nghịch đảo ma trận phải:',  matrix_f)
    
    matrix_g = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])

    print('So sánh',matrix_a == matrix_g) 
    
if __name__ == "__main__":
    main()