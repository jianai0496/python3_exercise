scores = [57,49,85,67,50,54,83,95,94,88,100]
min_score = 101
max_score = 0
sum_score = 0

for i in scores:
    if i < min_score:
        min_score = i
    if i > max_score:
        max_score = i
    sum_score += i
print('最高分',max_score)
print('最低分',min_score)
print("平均分{:.3f}".format(sum_score/len(scores)))   
