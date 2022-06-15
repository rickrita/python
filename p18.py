pokLi1 = [ "A", "J", "Q", "K"]
pokLi2 = [ 1, 11, 12, 13 ]
total = 0

for i in range(5):
    pok = input("輸入五張牌:")
    if pok in pokLi1: total += pokLi2[pokLi1.index(pok)]
    else: total += int(pok)
print(total)