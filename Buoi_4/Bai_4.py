a = int(input())
b = map(int, input().split())
even = 0
odd = 0
for i in b:
    if(i % 2 == 0): 
        even += i
    else:
        odd += i
if even > odd: print("even")
elif even < odd: print("odd")
else: print('equal')