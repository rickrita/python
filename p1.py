a=str(input("請輸入正整數:"))
b=len(a)
c=[]
d=[]


def vvv(n,s):
  d=str(0)
  for A in range(s,n+1):
    d=d+a[A]
  return d


def aaa(k):
  if k > 1:
    for i in range(2, int(k/2)+1):
        if (k % i) == 0:

            break
    else:

        c.append(k)

  else:
    pass

BB=1
for AA in range(0,b):
  for BB in range(0,b):
    k=int(vvv(BB,AA))
    aaa(k)

if c==d:
  print("字串中最大的質數值為: ",end='')
  print("No prime found")
else:
  print("字串中最大的質數值為: ",end='')
  print(max(c))