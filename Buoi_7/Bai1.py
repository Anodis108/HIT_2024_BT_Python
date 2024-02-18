def MyMultiple(*args:int) -> float:
    '''
    Hàm này trả về tích các tham số truyền vào
    '''
    x = 1
    for i in args:
        x *= i
    return float(x)
print(MyMultiple(1, 2, 3, 4))
print(MyMultiple(5, 5, 5))
print(MyMultiple(1.2, 5))