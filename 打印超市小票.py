total ,count= 0, 0
print('==========================================')
print('Na.:201911010001')
print('收银员：Lisa')
print('品名                       单价  数量  金额')
print('------------------------------------------')
print("195积木英雄工厂            6.00   1     "  ,end='')
print(6.00*1)
total = total+6.00*1
count = count + 1
print("电竞专用耳机               40.00  2    ",end='')
print(40.00*2)
total = total+40.00*2
count = count + 2
print('-------------------------------------------')
print("合计:",end="")
print(count,end="")
print("                                 ",end="")
print(total)
print("税费:",end='')
print("                                  ", end="")
print(total*0.12)
print('==========================================')
