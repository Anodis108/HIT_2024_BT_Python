def flatten(list1):
    list2 = []
    for i in list1:
        if isinstance(i, list):
            list2 += flatten(i)
        else:
            list2.append(i)
    return list2

def group(list1:list):
    dic_group = {}
    for i in list1:
        if str(i) not in dic_group:
            dic_group[str(i)] = []
        dic_group[str(i)].append(i)
    return [value for key, value in dic_group.items()]
a = [0, 10, [20, 30], 40, 40, [60, 70, 80], [90, 100, 110, 120]]
a = flatten(a)
print(a)
print(group(a))