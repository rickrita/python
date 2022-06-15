suject_list= ["國文", "英文", "微積分", "體育", "程式設計"]
total_score, maxscore, minscore = 0, 0, 100
for suject in suject_list:
    score = int(input(suject+":"))
    total_score += score
    if score > maxscore:
        maxscore = score
        maxsuject = suject
    if score < minscore:
        minscore = score
        minsuject = suject
print("平均分數：", (total_score/len(suject_list)))
print("最高分科目：", maxsuject, maxscore, "分")
print("最低分科目：", minsuject, minscore, "分")