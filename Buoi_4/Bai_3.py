# Cacsh 2
a = input()
b = []
i = 0
while i < len(a):
    if (a[i] >= '0' and a[i] <= '9'):
        x = i
        while (a[x] >= '0' and a[x] <= '9') or a[i] == '-':
            x += 1
            if x == len(a): 
                break
        if a[i - 1] == '-':
            b.append(a[i-1:x])
        else:
            b.append(a[i:x])
        i = x - 1 
    i += 1
print(b)
print(sum([int(i) for i in b]))

# cachs 2 
string = input()
total = 0
i = 0
while i < len(string):
    if string[i].isdigit():
        start = i
        while i < len(string) and string[i].isdigit():
            i += 1
        number = int(string[start:i])
        if string[i-1] == '-':
            total -= number
        else:
            total += number 
        print(total) 
    i += 1
print(total)