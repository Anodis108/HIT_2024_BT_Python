championLOL = ["Yasuo", "Lee Sin", "Zed", "Master Yi", "Garen", "Tryndamere"]
dataLOL = [
    {"price": 6300, "Ulti": "Trăn trối"},
    {"price": 4800, "Ulti": "Nộ Long Cước"},
    {"price": 4800, "Ulti": "Dấu Ấn Tử Thần"},
    {"price": 450, "Ulti": "Chiến Binh Sơn Cước"},
    {"price": 450, "Ulti": "Công Lý Demacia"},
    {"price": 1350, "Ulti": "Từ Chối Tử Thần"}	
]
shop_champion = {}
for i in range(0,len(championLOL)):
    shop_champion[championLOL[i]] = dataLOL[i]
champion = input("Nhap champion ban muon tim:")
if champion in shop_champion:
    print(champion,":", shop_champion[champion]["price"])
else:
    print("Khong co champion trong cua hang. Co the ban da so huu roi. :>")