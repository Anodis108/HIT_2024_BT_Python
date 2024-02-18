a, b, c = map(int, input().split())
print('Tam Giác ' if (a + b > c) and (a + c > b) and (b + c > a) else 'Khong phải tam giác')