def doc_toa_do() -> tuple:
    '''
    Hàm đọc tọa độ của 2 điểm A, B từ input.txt
    
    Returns:
        tuple: (Tọa độ điểm A, tọa độ điểm B)
    '''
    with open('input.txt', 'r') as f:
        line1 = f.readline().strip()
        line2 = f.readline().strip()
    
    diem_a = line1.split()[1:]
    diem_b = line2.split()[1:]
    
    toa_do_A = (float(diem_a[0]), float(diem_a[1]))
    toa_do_B = (float(diem_b[0]), float(diem_b[1]))
    
    print(type(toa_do_A))
    return toa_do_A, toa_do_B
    
def tinh_khoang_cach(toa_do_A : tuple, toa_do_B : tuple) -> float:
    '''
    Hàm tính khoảng cách giữa 2 điểm A, B
          
    Parameters:
        toa_do_A: tọa độ điểm A
        toa_do_B: tọa độ điểm B
    return:
        Khoảng cách giữa 2 điểm A, B
    '''
    x_A, y_A = toa_do_A
    x_B, y_B = toa_do_B
    
    khoang_cach = ((x_A - x_B) ** 2 + (y_A - y_B) ** 2) ** 0.5
    
    return khoang_cach

def solve() -> None:
    '''
    Hàm thực hiện viết tọa độ vào output.txt
    
    Parameters:
        toa_do_a: x, y của A
        toa_do_b: x, y của B
        khoang_cach: khoảng cách giữa 2 điểm A, B
    
    Returns:
        none
    '''
    toa_do_a, toa_do_b = doc_toa_do()
    khoang_cach = tinh_khoang_cach(toa_do_a, toa_do_b)  
    
    print("A(", toa_do_a[0], ",", toa_do_a[1], ")")
    print("B(", toa_do_b[0], ",", toa_do_b[1], ")")
    print("AB =", round(khoang_cach, 2))
    
    with open('output.txt', 'w') as f:
        f.write("A {}, {}\n".format(toa_do_a[0], toa_do_a[1]))
        f.write("B {}, {}\n".format(toa_do_b[0], toa_do_b[1]))
        f.write("AB {}\n".format(round(khoang_cach, 2)))
        
if __name__ == "__main__":
    solve()