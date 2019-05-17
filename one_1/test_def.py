# def sushu(x):
#     #判断一个数是不是素数
#         for y in range(2,x):
#             if x % y == 0:
#                 return False
#             elif x == y+1:
#                 return True
#         if x == 1 or x == 2:
#             return True
# x = int(input("请输入一个数:"))
# print(sushu(x))
# 
# def sushu(x):
#     #100-200之间所有的素数
#         for y in range(2,x):
#             if x % y == 0:
#                 return False
#             elif x == y+1:
#                 return True
# L = []
# for x in range(100,200):
#     if sushu(x) == True:
#         L.append(x)
# print(L)
# 
# i = input("请输入一组数字 用空格隔开：")
# L = [int(x) for x in i.split()]
# def pjz(ave):
#     #一组数平均值
#     sum = 0
#     for y in L:
#         sum += y
#         ave = sum/len(L)
#     return ave
# print(pjz(L))
# 
# def zys(n):#求正整数的质因数
#     L = set([1])
#     while n > 1:
#         for i in range(2, n + 1):
#             if n % i == 0:
#                 n = int(n / i)
#                 L.add(i)
#                 break
#     return L
# while 1:
#     s = int(input('请输入一个正整数：'))
#     print("质因数："+' '.join([str(x) for x in zys(s)]))
#     break;
# L = [1,2,3,4,5]    # 列表的循环左移K位
# k = int(input("请输入往左移几位？"))
# def zy(L):
#     n = 0
#     for i in range(k):
#         L.append(L[n])
#         n+=1
#     for i in range(k):
#         L.pop(0)
#     return L
# print(zy(L))

# def huiwen(x):  # 判断一个整数是不是回文数
#     for i in range(int(len(x)/2)):
#         if x[i] == x[-(i+1)]:
#             return True
#         else:
#             return False
# x = input("请输入一个整数：")
# print(huiwen(x))

# def jch(n):     # 求阶乘
#     sum = 0
#     m = 1
#     for i in range(1,n+1):
#         m *= i
#         sum += m
#     return sum
# n = int(input("请输入n的值："))
# print(jch(n))

# def sxh():  #求所有的水仙花数
#     S = []  #保存水仙花数
#     for n in range(100,999):
#         if int(str(n)[0])**3+int(str(n)[1])**3+int(str(n)[2])**3 == n:
#             S.append(str(n))
#     print('所有水仙花数：'+' '.join(S))
#     return True
# sxh()

# def zdgys(m,n):   # 辗转相除法求最大公约数
#     x = m % n
#     while (x != 0):
#         m = n
#         n = x
#         x = m % n
#     return n
# def zdgbs(x, y):   # 求最大公倍数
#     if x > y:
#         max = x
#     else:
#         max = y
#     while (True):
#         if ((max % x == 0) and (max % y == 0)):
#             zdgbs = max
#             break
#         max += 1
#     return zdgbs
# m,n= input("请输入两个数(空格隔开)：").split()
# print(m,n+'的最大公约数:',zdgys(int(m),int(n)))
# print(m,n+'的最小公倍数:',zdgbs(int(m),int(n)))

i = 1

while i<=3:

    print("yes")

    i += 1

else:

    print("no")
