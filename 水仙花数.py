n=int(input())
a=int(n/100)  #取得百位整数
b = int(n/10 % 10)  # 取得十位整数
c = n % 10  # 取得个位整数
result = a**3+b**3+c**3
if n==result:
    print(n,end='')
    print('是水仙花数')
else:
    print(n, end='')
    print('不是水仙花数')



