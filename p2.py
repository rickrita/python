electricity = float(input())
if electricity <= 120:
    print("summer month",electricity*2.10)
    print("Non-summer month",electricity*2.10)
elif  330 >= electricity >120:
    print("summer month",(electricity-120)*3.02+120*2.10)
    print("Non-summer month",(electricity-120)*2.68+120*2.10)
elif  500 >= electricity >330:
    print("summer month",(electricity-330)*4.39+120*2.10+210*3.02)
    print("Non-summer month",(electricity-330)*3.61+120*2.10+210*2.68)
elif  700 >= electricity >500:
    print("summer month",(electricity-500)*4.97+120*2.10+210*3.02+170*4.39)
    print("Non-summer month",(electricity-500)*4.01+120*2.10+210*2.68+170*3.61)
elif  electricity >700:
    print("summer month",(electricity-700)*5.63+120*2.10+210*3.02+170*4.39+200*4.97)
    print("Non-summer month",(electricity-700)*4.50+120*2.10+210*2.68+170*3.61+200*4.01)        