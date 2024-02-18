l = list(input().split())
a = int(input())
k = int(len(l)/a)
b = []
for i in range(a):
    b.append(l[k* i : k * (i + 1)])
print(b)