"""
  计算m、n两个数的平均值和m的平方乘以n的平方
  m和n的平均值为： 11.5
  m的平方乘以n的平方值为：16900
"""
# 任务
'''
1.定义变量m,初始值为 10； 变量n的初始值为 5
2.变量m的值加3，n的值加5
3.定义变量averageResult, 用于存放m和n的平均值
4.定义变量productResult, 用于存放m的平方乘以n的平方
'''
m,n = 10,5
m +=3 
n +=5
averageResult = (m + n)/2
# print(averageResult)
productResult = (m**2)*(n**2)
print(productResult)
