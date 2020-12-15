# 打印一個三角形
# print('*'*1)
# print('*'*2)
# print('*'*3)
# print('*'*4)
# print('*'*5)

# 用for 循環實現
# for i in range(1, 6):
#     print('*'*i, end='\n')


#  打印一個鈍角三角形，怎麽辦？
# for i in range(1, 6):
#     print(' '*(6-i)+'*'*(i))
#     print()


#  打印九九乘法表
# for i in range(1, 6):
# print(' '*(10-1)+'*'*(1))
# print(' '*(10-2)+'*'*(3))
# print(' '*(10-3)+'*'*(5))
# print(' '*(10-4)+'*'*(7))
# print(' '*(10-5)+'*'*(9))
# print(' '*(10-6)+'*'*(11))
# print(' '*(10-7)+'*'*(13))
# print(' '*(10-8)+'*'*(15))
# print(' '*(10-9)+'*'*(17))

# 聖誕樹
x = 10
y = 1
for i in range(x):
    print(' '*(x-i)+'%'*y)
    y += 2


for i in range(3):
    print(' '*(x-1)+'*'*3, end=' ')
    print()
