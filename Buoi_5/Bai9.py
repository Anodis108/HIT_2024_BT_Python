import random
n = int(input("Nhap so tai khoan can lap:"))
user_names = [] 
for i in range(2021600001,2021600001+n):
    user_names.append(str(i))
head_title = ["CNTT","KHMT", "KTPM", "HTTT"]
password = []
print(user_names)
for i in user_names : 
    password.append(random.choices(head_title)[0] + i)
accounts = {}
for i in range(n):
    accounts[f'Account{i+1}'] = {'Username':user_names[i],'Password':password[i]}
for i in accounts:
    print(i,":",accounts[i])