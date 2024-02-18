number_list = set(float(i) for i in input().split())

if 11 in number_list:
    print("Da co so 11 trong day so. Khong can them.")
else: 
    number_list.add(11)
    print("Danh sach ban dau chua co . Va da duoc them vao sau khi kiem tra.")

sorted_number_list = sorted(number_list)
check_list = []
for i in number_list:
    if ( 11 - i ) in number_list:
        elemt = (i,11-i)
        if (i,11- i) not in check_list and (11-i,i) not in check_list:
            check_list.append(elemt)
res_tuple = tuple(check_list)
print(res_tuple)
print("tong la: ",len(res_tuple)*11)