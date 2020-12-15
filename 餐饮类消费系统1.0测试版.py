
costs = 0
first = 100
print('*'*20)
while first>0:

    consumption = float(input("请输入单次消费金额(元):"))

    costs += consumption   # 累计消费金额

    answer = input('是否要继续输入(y/n)')

    if answer == 'y':
        continue

    sum = first -costs
    print(f"您此次消费金额是{costs}元")
    print(f"此次消费后剩余金额{sum}元")

    if sum <= 10:
        print("您的剩余金额已不足10元,为保证您的用户权益，请尽快充值")
        print('请至大厅服务处，为您办理充值业务')
        break

while True:
    # user_login = input('')

    user=input("请输入管理员账号")
    if user =="83nb":
        print('账号输入正确，等待确认后输入密码')

        psw=input("请输入管理员密码")
        if psw == '83nb':
            print("恭喜您账号和密码正确，登录成功！")

            print('现在准备进入充值管理系统.......')
            c=float(input("请输入充值人民币金额(元)："))
            change = sum + c
            print(f"本次充值后剩余金额是{change}元")
            answer = input('是否已为顾客办理完成(y/n)')
            if answer =='n':
                continue
            else:
                print('请为本次服务进行评价，等待您的再次光临，祝您生活愉快!')
                break
        else:
            print('非常抱歉，密码输入错误')
            continue



    else:

        print('管理员账号没有注册或输入错误，请重新输入')
        