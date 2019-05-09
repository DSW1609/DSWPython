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

i = input("请输入一组数字 用空格隔开：")
L = [int(x) for x in i.split()]
def pjz(L):
    sum = 0
    for y in L:
        sum += y
        ave = sum/len(L)
    return ave
print(pjz(L))