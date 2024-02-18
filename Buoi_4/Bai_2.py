a = list(map(int, input().split()))
b = [i for i in a if i % 2 == 1]
print(sorted(b))