print("----成绩管理----")
L = []  # 学生总成绩
L2 = []  # 不及格成绩
L3 = 0  # 不及格人数
sum = 0  # 成绩总分
num = 1  # 1-n
n = int(input("请输入学生总人数："))
for i in range(n):  # 输入成绩
    print('请输入第', num, '个学生的成绩：', end="")
    score = int(input())
    L.append(score)  # 存到L中
    num += 1
for i in L:    # 遍历L,求成绩总分
    sum = sum+i
    if i < 60:      # 存不及格人数
        L2.append(i)
L3 = len(L2)    # 求L2长度，相当于求不及格人数
L.sort(reverse=True)    # 对L排序
for i in range(100):
    print("----请输入1-5---")
    print("1.最高分")
    print("2.最低分")
    print("3.平均数")
    print("4.不及格人数")
    print("5.从高到低排序")
    s = int(input())
    if s == 1:
        print("最高分：", max(L))
    elif s == 2:
        print("最低分：", min(L))
    elif s == 3:
        print("平均数：", sum /n)
    elif s == 4:
        print("不及格人数：", L3)
    elif s == 5:
        print("从高到低排序：", L)
    else:
        print("请正确输入!")
        continue
    print("是否退出管理系统Y/N")
    x = input()
    if x == 'Y':
        break
    else:
        continue


