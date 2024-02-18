class PyCon:
    id = 0
    def __init__(self, name, age) -> None:
        PyCon.id += 1
        self.id = PyCon.id
        self.name = name
        self.age = age
    
    def nhap(self):
        self.name= input()
        self.age = int(input())
        
    @classmethod
    def averAge(cls, pycons):
        return sum(i.age for i in pycons)/len(pycons)
    
    def __str__(self) -> str:
        return f"Id: {self.id} || Tên:{self.name} || Tuổi: {self.age}"
    
def main():
    n = int(input())
    pycons = []
    for i in range(n):
        a = PyCon('','')
        a.nhap()
        pycons.append(a)
        print(a)
    print(PyCon.averAge(pycons))

if __name__ == "__main__":
    main()
    