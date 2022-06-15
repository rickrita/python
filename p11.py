a,b = map(int,input("月及日:").split())
if a == 1:
    if b < 21:
        print("Capricorn")
    else:
        print("Aquarius")
elif a == 2:
    if b < 19:
        print("Aquarius")
    else:
        print("Pisces")
elif a == 3:
    if b < 21:
        print("Pisces ")
    else:
        print("Aries")
elif a == 4:
    if b < 21:
        print("Aries")
    else:
        print("Taurus")
elif a == 5:
    if b < 22:
        print("Taurus")
    else:
        print("Gemini")
elif a == 6:
    if b < 22:
        print("Gemini")
    else:
        print("Cancer")
elif a == 7:
    if b < 23:
        print("Cancer")
    else:
        print("Leo")
elif a == 8:
    if b < 23:
        print("Leo")
    else:
        print("Virgo")  
elif a == 9:
    if b < 23:
        print("Virgo")
    else:
        print("Libra")  
elif a == 10:
    if b < 24:
        print("Libra")
    else:
        print("Scorpio")  
elif a == 11:
    if b < 23:
        print("Scorpio")
    else:
        print("Sagittarius")
elif a == 12:
    if b < 22:
        print("Sagittarius")
    else:
        print("Capricorn")