a = {}
b = input()
for i in b:
    if i not in a:
        a[i] = 0
    a[i] += 1
print(a)