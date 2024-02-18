def nhap() -> list:
    '''
    Hàm nhập vào một mảng số int 1 chiều
    
    Parameters:
        t: độ dài mảng
        lst: mảng cần nhập
    
    Returns:
        mảng sau khi được xử lý cộng dồn
    
    '''
    t = int(input())
    lst = list(int(i) for i in input().split())
    for i in range(1, len(lst)):
        lst[i] += lst[i-1]
    return lst

def solve(x : int, mang : list) -> int:
    '''
    Hàm trả về phần tử thứ x của mảng
    
    Parameters:
        x : phần tử cần được trả vè
        mang: mảng chứa phần tử
    
    Return:
        phần tử thứ x của mảng
    '''
    return mang[x]

def main():
    '''
    Thực hiện các thao tác của bài
    
    Parameters:
        mang: mảng cần được nhập
        k: Số trường hợp cần thực hiện
        x: bài cần in ra tổng các phần tử từ đầu đến x
    Returns:
        None
    '''
    mang = nhap()
    k = int(input())
    for i in range(k):
        x = int(input())
        print(solve(x, mang))

if __name__ == '__main__':
    main()