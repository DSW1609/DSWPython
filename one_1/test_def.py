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

# i = input("请输入一组数字 用空格隔开：")
# L = [int(x) for x in i.split()]
# def pjz(L):
#     #一组数平均值
#     sum = 0
#     for y in L:
#         sum += y
#         ave = sum/len(L)
#     return ave
# print(pjz(L))

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
L = [1,2,3,4,5]    # 列表的循环左移K位
k = int(input("请输入往左移几位？"))
def zy(L):
    n = 0
    for i in range(k):
        L.append(L[n])
        n+=1
    for i in range(k):
        L.pop(0)
    return L
print(zy(L))