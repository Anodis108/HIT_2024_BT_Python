import math
a = int(input('số a '))
b = int(input('số b '))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)
if(a > b): 
    print(' a Lớn hơn b')
elif(a < b):
    print(' a Nhỏ hơn b ')
else:
    print('a == b')
print(a and b)
print(a or b)
print(a ^ b) # a xor b
print(not(a == b))
print(a >> 5)
print(a << 4)
print(a)
a = int(a)
while (a != 0):
    print(int(a % 2), end = '')
    a = int(a / 2)