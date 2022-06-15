m = int(input('請輸入階乘M:'))
sum = 1
i = 1
while(sum < m):
        i = i + 1
        sum = sum * i
print("超過M值為",m,"最小階乘為:",i)