set1 = {x for x in input().split(' ')}
set2 = {x for x in input().split(' ')}
print(set1 & set2 if (set1 & set2) != 0 else 'Nothing')
print(set1 | set2)
print(set1 - set2)
print(set1 ^ set2)
