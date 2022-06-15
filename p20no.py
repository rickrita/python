from array import *
a = input("輸入查詢學號為:")
T = [[123, 'Tom', 'DTGD'], [456, 'Cat','CSIE'], [789, 'Nana', 'ASIE'], [321,'Lim','DBA'], [654,'Won','FDD']]
if a == "123":
    print("學生資料為",a,T[0][1],T[0][2])
elif a == "456":
    print("學生資料為",a,T[1][1],T[1][2])
elif a == "˙789":
    print("學生資料為",a,T[2][1],T[2][2])
elif a == "321":
    print("學生資料為",a,T[3][1],T[3][2])
elif a == "654":
    print("學生資料為",a,T[4][1],T[4][2])