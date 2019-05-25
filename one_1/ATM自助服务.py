M = 5000   # M用来保存总金额 给定初始存款金额
PSW = '123456'    # 初始密码
Z = {'王嘉辉':19990918,'苗佳林':19981012}    # 保存姓名和账号
def menu():
    # 显示菜单
    print("="*6+'ATM自助服务'+"="*6)
    print('1.存款',end= ' '*11)
    print('2.取款')
    print('3.转账汇款',end= ' '*4)
    print('4.查询余额')
    print('5.修改密码', end=' ' * 4)
    print('6.退出取卡')
def cunkuan(m):
    # 存款
    global M
    M = M + m
    print("存款成功,当前卡内余额:",M)
    return M
def gaimi():
    # 修改密码
    global PSW
    PSW = input("请输入新密码：")
    PSW2 = input("请再次输入：")
    if PSW == PSW2:
        print("密码修改成功请重新登录!")
        main()
def qukuan(q):
    # 取款
    global M
    while True:
        if M < q:
            q = int(input("余额不足请重新输入:"))
            continue
        else:
            break
    M = M - q
    print("取款成功,当前卡内余额:",M)
    return M
def zhunzhang():
    # 转帐
    global M
    global name
    global zhanghao
    while True:
        NAME = input("请输入被转帐人的姓名：")
        ZHANGHAO = int(input("请输入被转账人的账号："))
        if NAME in Z and Z[NAME] == ZHANGHAO:
            jine = int(input("请输入转账金额："))
            while True:
                if M < jine:
                    jine = int(input("余额不足请重新输入："))
                    continue
                else:
                    break
        else:
            print("姓名或账号输入错误请重新输入！")
            continue
        M = M - jine
        print("转帐成功!")
        return M
def chakan():
    # 查看余额
    global M
    print("卡内余额:",M)
    # print("卡内余额▇▇▇(用力刮开查看)")
def main():
    global PSW
    psw = input("请输入密码：")
    count = 1
    while count < 3:
     if psw == PSW:
        menu()
        while True:
            I = int(input("请选择1-6："))
            if I == 1:
                m = int(input("请输入您要存的金额："))
                cunkuan(m)
            elif I == 2:
                q = int(input("请输入您要取出的金额："))
                qukuan(q)
            elif I == 3:
                zhunzhang()
            elif I == 4:
                chakan()
            elif I == 5:
                gaimi()
            elif I == 6:
                print("请取卡！")
                count = 3
                break;
     else:
        psw = input("密码错误，请重新输入：")
        count+=1
        if count == 3:
            print("密码错误输入三次，已锁定！")
            break;
main()