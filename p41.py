a = int(input("搭了幾次電梯:"))
floor = 1
money = 0
for i in range(a):
    newfloor = int(input())
    if newfloor > floor:
        money += (newfloor-floor)*20
    elif newfloor < floor:
        money += (floor-newfloor)*10
    floor = newfloor
print(money, "元")