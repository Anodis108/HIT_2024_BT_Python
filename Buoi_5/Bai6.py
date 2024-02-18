_dict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6}
counter = 0
save_del = []
for key, value in _dict.items():
    if 2.5 <= value <= 3.5:
        counter = counter + 1
    elif value <= 2:
        save_del.append(key)
for i in save_del:
    del _dict[i]
print(counter, _dict)
