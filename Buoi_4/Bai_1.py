d, m, y = map(int, input().split())
all_day = 365
while (d > 31 | m > 12 ):
    d, m, y = map(int, input().split())
thang = [31,28,31,30,31,30,31,31,30,31,30,31]
if y % 4 == 0: thang[1] = 29; all_day = 366
a = sum(thang[:m - 1])
print(all_day - a - d + 1)