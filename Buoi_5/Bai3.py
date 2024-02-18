a = input().split(' ')
max_count = 0
count = dict()
ans = set()
for i in a:
    if i not in count:
        count[i] = 0
    count[i] += 1
    max_count = max(max_count, count[i])
for key, value in count.items():
    if value == max_count:
        ans.add((key, value))
    else:
        continue
print(tuple(ans))