# X = set(['小王','大王','小李','大李','小张'])
# M = set(['小王','大王','小李','大李'])
# Y = set(['小王','大王','小李'])
# T=set([])
# N=set([])
# for name in X:
#     if name in M and name in Y:
#         T.add(name)
# for name in X:
#     if name not in M and name not in Y:
#         N.add(name)
# print('美术、音乐两个特长班都参加的学生是：'+' '.join(T))
# print('一个特长班也没参加的学生是：'+' '.join(N))
# S = set(['大一','大二','大三','大四','大五','大六','大七','大八','大九','大十'])   # 总人
# C = set(['大一','大二','大三','大四','大五','大六'])   # 长跑
# T = set(['大一','大二','大三','大四','大五'])     # 跳远
# Q = set(['大一','大二','大三','大四'])     # 铅球
# D = set([])
# L = set([])
# for name in S:
#     if name in C and name in T and name in Q:
#         D.add(name)
#     if name in C and name in T or name in C and name in Q or name in T and name in Q:
#         L.add(name)
# print('三项都参加的学生是：'+' '.join(D))
# print('至少参加两项的学生是：'+' '.join(L))

# A = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','m','o','p','q','r','s','t','u','v','w','x','y','z'])
# Z = set(['0','1','2','3','4','5','6','7','8','9'])
# Y = []#存储小写字母
# Y2 = []#存储数字
# N = []#存储非小写字母和数字
# S = input('请输入字符串：')
# for i in S:
#     if i in A:
#         Y.append(i)
#     elif i in Z:
#         Y2.append(i)
#     else:
#         N.append(i)
# if Y and Y2 and len(N)==0:#如果Y和Y2不为空 N为空 也就是S同时包含小写字母和数字 输出yes
#     print(S+'是由小写字母和数字构成的')
# else:
#     print(S+'不是由小写字母和数字构成的')

# S = input('请输入一个字符串：')
# A = []
# B = []
# A.append(S[::2])
# B.append(S[1::2])
# print(''.join(A)+''.join(B))

# Z = input('请输入一串字符：')
# D = {}  # 建一个空字典
# Di = '' # 存放大写字母
# Xi = '' # 存放小写字母
# for i in Z: # 遍历Z
#      if i >= 'a' and i <= 'z':  # 如果i为小写字母
#          Di = i.upper();    # 给Di值为i的大写字母
#          if i in D or Di in D:  # 如果i 或Di 在D中
#              D[Di] +=1  # Di的值+1
#          else:
#              D[Di] = 1  # Di的值=1
#      else:
#          Xi = i.lower();
#          if i in D or Xi in D:
#              D[i] +=1
#          else:
#              D[i] = 1
# for key in D:
#     print(key+'出现的次数是:',D[key],end=', ')

# S = input('请输入一个字符串:')
# L = []  # 定义一个空集合
# for i in S: # 遍历S
#     L.append(i) # 存到L生成集合
# Z = L[-1]   # 获取最后一位元素的值
# L.insert(0,Z)   # 插入到下标为0的位置
# L.pop()     # 删除最后一位
# print(''.join(L))   # 输出

# T = (1,3,5,7,9)     # 创建集合，包含奇数个数字
# TZ = len(T)//2    # 获取长度，整除 得到中间位置的下标
# print(T[TZ])    # 输出下标为TZ的元素

# import string
# import random
# S = string.digits   # 生成0-9
# Z = string.ascii_letters    # 生成所有英文字母
# for i in range(5):
#     SJ = random.randint(0, 5)   # 生成随机数0,5
#     SZ = random.randint(0, 21)  # 生成随机数0,21
#     print(S[SJ:SJ+4]+Z[SZ:SZ+4])




