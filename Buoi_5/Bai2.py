def find_largest_subnet(input_set, target_sum):
    max_subnet = set()
    max_sum = 0
    
    def find_subset(current_set, remaining_elements, current_sum):
        nonlocal max_subnet, max_sum # cho biết đây ko phải biến cục bộ của hàm mà là biến đc tham chiếu từ ngoài vào
        if current_sum <= target_sum and current_sum > max_sum:
            max_subnet = current_set.copy()
            max_sum = current_sum
        print(current_set)
        for elem in remaining_elements:
            new_set = current_set.copy()
            new_set.add(elem)
            new_sum = current_sum + elem
            if new_sum > target_sum:
                continue

            find_subset(new_set, remaining_elements - {elem}, new_sum)
            
    find_subset(set(), input_set, 0)
    
    return max_subnet
input_set = {*map(int, input().split(' '))}
target_sum = int(input())
print(input_set)
largest_subset = find_largest_subnet(input_set, target_sum)

print("Tập hợp con lớn nhất có tổng không vượt qua", target_sum, "là:", largest_subset)
