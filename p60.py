word = input("請輸入一串小寫英文")
vo = ["a","e","i","o","u"]
for char in word:
    if char in vo:
        word= word.replace(char, ".")
print(word)