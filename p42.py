a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

res = b*b - 4*a*c
if res > 0:
    print(int((-b + pow(b*b - 4*a*c,0.5))/(2*a)))
    print(int((-b - pow(b*b - 4*a*c,0.5))/(2*a)))
elif res == 0:
    print(int(-b / (2*a)))
else:
    print("無解")