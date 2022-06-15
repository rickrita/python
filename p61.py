st = input()
def t2s(t):
    m,s = t.strip().split(":")
    return int(m) * 60 + int(s)
print(t2s(st))