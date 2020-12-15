ticket=1     #1--->有车票  0----> 没有车票
knifelength = 15   #刀子的可通过安检长度，小于等于10，表示合法，否则不合法
if ticket == 1:
    if knifelength <10:
        print('请您收好车票，旅途愉快')
else:
    print('对不起，您还没有车票，请先购票')