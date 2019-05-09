# L = [2, 3, 4, 3, 2, 1, 2, 2, 4, 2]
# for i in range(5):
#     L.remove(2)
# print(L)

# L = [2, 3, 4, 3, 2, 4, 3, 2, 1, 5]
# L2 = list(set(L))
# L2.sort(key=L.index)
# print(L2)

# num2 = list(input("请输入一个二进制数："))    # 从右到左,第 1 位 乘以 2的0次方，第2位乘以2的1次方，第N位乘以2的n-1
# sum = 0     # 给和一个默认值0
# j = 0       # j是次方,从0开始
# Lnum2 = len(num2)   # 二进制数的长度
# n = 1       # n是配合Lmum2用索引方法倒序获得二进制每一位上的数
# for i in range(Lnum2):      # 开始循环
#     sum += int(num2[Lnum2-n])*2**j      # sum依次相加每个数乘以2的j次方
#     n += 1
#     j += 1
# print("您输入的数字转换成十进制为：", sum)

# x = (3,)
# print(type(x))
# 颜色组合
# T = ('红色', '黄色', '蓝色', '绿色', '紫色')
# n = 0
# m = 1
# z = 0
# while z < 5:
#     x = T[n]
#     for y in T[m:5]:
#         print(x+y, end=' ')
#     n += 1
#     m += 1
#     z += 1
# dict
# A = list(input("请输入一串字符："))
# D = {}
# for x in A:
#     D[x] = A.count(x)
# print(D)

# print("----密码加密系统----")
# print("1.加密文字", end=' ')
# print("2.解密文字")
# C = []
# x = ''
# m = int(input("请输入1-2："))
# if m == 1:
#     j1 = input("请输入要加密的文字:")
#     for i in j1:
#         if (i >= 'A' and i <= 'M') or (i >= 'a' and i <= 'm'):
#             x += chr(ord(i) + 13)
#         elif (i >= 'N' and i <= 'Z') or (i >= 'n' and i <= 'z'):
#             x += chr(ord(i) - 13)
#     C.append(x)
#     print("加密后您输入的文字是："+''.join(C))
# elif m == 2:
#     j2 = input("请输入要解密的文字:")
#     for i in j2:
#         if (i >= 'A' and i <= 'M') or (i >= 'a' and i <= 'm'):
#             x += chr(ord(i) + 13)
#         elif (i >= 'N' and i <= 'Z') or (i >= 'n' and i <= 'z'):
#             x += chr(ord(i) - 13)
#     C.append(x)
#     print("解密后您输入的文字是："+''.join(C))
#字母转ASSIC码
# D = {}
# for i in range(26):
#     x = chr(i+ord('a'))
#     y = ord(x)
#     D[y] = x
# print(D)

# print("----密码加密系统----")
# C = []
# while True:
#     x = ''
#     j = input("请输入要加密的文字:")
#     K = int(input("您想把每个英文字母变为其后面的第几个字母1-25："))
#     for i in j:
#         if (i >= 'A' and i <= 'M') or (i >= 'a' and i <= 'm'):
#             x += chr(ord(i) + K)
#         elif (i >= 'N' and i <= 'Z') or (i >= 'n' and i <= 'z'):
#             x += chr(ord(i) - K)
#     C.append(x)
#     print(''.join(C))
#     Y = input("是否继续加密文字? Y/N ")
#     if Y=='Y':
#         C.clear()
#         continue
#     else:
#         print("再见！")
#         break
# S = {201710080225:'小明',201710080224:'大明',201710080223:'小红',201710080222:'大红',201710080221:'小蓝'}
# L = []
# for i in S:
#     L.append(i)
# L.sort()
# for key in L:
#     print(key,S[key])
# S = {'小明':'男','大明':'女','小红':'男','大红':'女','小蓝':'男'}
# for key in list(S.keys()):
#     if S[key] == '男':
#         del S[key]
# for key in S:
#     print(key+':'+S[key])

# url = '''
# <ul><li><a href = "http://www.qq.com"><img src = "http://img01.jpg"/>图片1</a></li>
# <ul><li><a href = "http://qzone.qq.com"><img src = "http://img02.jpg"/>图片2</a></li>
# <ul><li><a href = "http://dsw1609@github.io"><img src = "http://img03.jpg"/>图片3</a></li>
# '''
# start = url.find('<img src = ')
# while start != -1:
#     start_link = url.find('"',start)
#     end_link = url.find('"',start_link+1)
#     print("图片地址：",url[start_link+1:end_link])
