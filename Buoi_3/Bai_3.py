n = int(input())
c = 1
while n:
    x, y, z = map(str, input().split())
    y = int(y)
    z = int(z)
    yz = y + z
    print(c, x, yz, end=' ')
    if (yz >= 190): print('Xuất sắc')
    elif (yz >= 150): print('Giỏi')
    elif (yz >= 100): print('Khá')
    else: print('Yếu')
    n -= 1
    c += 1