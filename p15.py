num = str(input("輸入一組四位數字為:"))
x = [int(a) for a in str(num)]
b = (x[0]+7)%10
c = (x[1]+7)%10
d = (x[2]+7)%10
e = (x[3]+7)%10
print(d,e,b,c)