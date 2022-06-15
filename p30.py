ans = input()
guess = input()
while guess != "0000":
    a, b = 0, 0
    for num in guess:
        if num in ans:
            if guess.index(num) == ans.index(num):
                a += 1
            else:
                b += 1
    print(f"{a}A{b}B")
    guess = input()