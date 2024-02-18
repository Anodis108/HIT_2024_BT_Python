n = int(input())
k = int(input())
while n:
    a = input()
    x = a[a.__len__() - 1: a.__len__() - 1 - k: -1]
    y = a[: a.__len__() - k]
    print(y + x)
    n -= 1