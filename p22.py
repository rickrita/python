a = int(input("輸入查詢組數 N 為:"))
b = {"123 456":9000,"456 789":5000,"789 888":6000,"336 558":10000,"775 666":12000,"566 221":7000}
for i in range(a):
    acc_pas = input()
    print(b[acc_pas]) if acc_pas in b else print("error")