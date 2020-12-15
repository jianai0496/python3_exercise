# 求列表中的最大值
largest = 0
def max_num(counts=[1,3,7,9,11,13]):    
    global largest
    for x in counts:
        if x >largest:
            largest = x
    print("所求列表的最大值是：",largest)
max_num()