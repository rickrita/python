mylist = [1,3,9,7,5]
max = sorted(mylist)
min = sorted(mylist, reverse=True)

b = "".join([str(_) for _ in min])
a = "".join([str(_) for _ in max])
ans = int(b) - int(a)
print("最大值數值與最小值數列差為", ans)