cost,time = map(int,input("輸入月租模式及通話時間:").split())
if cost == 186:
    if time*0.09<186*2:
        print("通話費為:",round(time*0.09*0.9))
    else:
        print("通話費為:",round(time*0.09*0.8))
elif cost == 386:
    if time*0.08<386*2:
        print("通話費為:",round(time*0.08*0.8))
    else:
        print("通話費為:",round(time*0.08*0.7))
elif cost == 586:
    if time*0.07<586*2:
        print("通話費為:",round(time*0.07*0.7))
    else:
        print("通話費為::",round(time*0.07*0.6))
elif cost == 986:
    if time*0.06<986*2:
        print("通話費為:",round(time*0.06*0.6))
    else:
        print("通話費為:",round(time*0.06*0.5))