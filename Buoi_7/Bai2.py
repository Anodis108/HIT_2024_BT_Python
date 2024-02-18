def chuyen_vi_matran(mang : list) -> list :
    '''
    Hàm in ma trận chuyển vị của mảng 2 chiều
    
    Parameters:
        mang: mảng 2 chiều
        
    Return:
        ma trận của mảng đã được chuyển vị
    '''
    
    row, col = len(mang), len(mang[0])
    ans = []
    for i in range(col):
        hang_rong = []
        for j in range(row):
            hang_rong.append(mang[j][i])
        ans.append(hang_rong)
    return ans

def nhap() -> list:
    '''
    Hàm nhập vào một ma trận và trả lại nó
    
    Parameters:
        col: số cột của mảng
        row: số hàng của mảng
        mang: mảng cần trả về 
    
    return:
        ma trận sau khi được nhập
    '''
    row, col = list(map(int, input().split(' ')))
    mang = []
    for i in range(row):
        hang = list(map(int, input().split(' ')))
        mang.append(hang)
    return mang

print(chuyen_vi_matran(nhap()))