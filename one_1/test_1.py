# for a in range(0,4):
#     for b in range(0,9):
#         c=18-5*a-2*b
#         if a+b+c==10:
#             print("5元",a,"张","2元",b,"张","1元",c,"张")
# import math
# s=1
# n=1.0
# t=1.0
# pi=0
# while math.fabs(t)>1e-7:
#     pi=pi+t
#     n=n+2
#     s=-s
#     t=s/n
# pi=pi*4
# print(pi)
# L = [2, 3, 4, 5, 6, 7, 8, -1, -2, -3]
# B = []
# for i in L:
#     if i > 0:
#      B.append(i)
# print(B)

# print("---猜数字游戏开始---")
# i=1
# for i in range(0,3):
#     n = input("请输入一个数字:")
#     num = int(n)
#     if(num<5):
#         print("猜小了！")
#         if (i == 2):
#             print("游戏失败！")
#             break;
#         continue;
#     elif(num>5):
#         print("猜大了！")
#         if (i == 2):
#             print("游戏失败！")
#             break;
#         continue;
#     elif(num == 5):
#         print("恭喜猜对了！")
#         break;
#     i+=1

# L = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 9]
# L2 = []
# for i in L:
#     if i not in L2:
#         L2.append(i)
# print(L2)

# n = input("请输入一个数字")
# print(int(n, 2))

# L = [50, 55, 56, 70, 80]
# L2 = len(L)
# L3 = []
# sum = 0
# for i in L:
#     sum += i
#     if i < 60:
#         L3.append(i)
# L.sort(reverse=True)
# L4 = len(L3)
# print("最高分：", max(L))
# print("最低分：", min(L))
# print("平均数：", sum/L2)
# print("不及格人数：", L4)
# print("从高到低排序：", L)
#
# L = []
# num = 1
# n = int(input("请输入学生总人数："))
# for i in range(n):
#     print('请输入第', num, '个学生的成绩：', end="")
#     score = input()
#     L.append(score)
#     num += 1
# # L.sort(reverse=True)
# print("最好成绩是："+max(L))

# n = int(input("请输入N=: "))
# a = 1
# b = 1
# sum = 0
# for i in range(n):
#     sum += a
#     a, b = b, a + b
# print("前", n, "项和是", sum, "!")
# x = {1:1, 2:2}
# x[3] = 3
# x=(i**2 for i in range(100))
# print(x)
# print(type({}))
# print('Hello'.upper())