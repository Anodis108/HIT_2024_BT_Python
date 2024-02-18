n = int(input("Nhập số lượng phần tử của mảng a: "))

a = []
for i in range(n):
    x = input(f"Nhập phần tử thứ {i + 1} của mảng a: ")
    a.append(x)

b = tuple(filter(lambda x: x.isdigit(), a))

print("Các phần tử của tuple b:")
for item in b:
    print(item)

count = sum(1 for item in b if item.isdigit())
print("Số lượng phần tử trong b có dạng số:", count)
