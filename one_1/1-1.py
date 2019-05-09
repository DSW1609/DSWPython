L = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59]  # list是一种有序的集合，可以随时添加和删除其中的元素。
print(L[0])  # 通过索引来获取list中的指定元素。
print(L[-1])  # 倒叙获取list中指定的值。
L.append('Paul')  # 插入新元素 默认放到最后
L.insert(0, 3)  # 插入元素到第一行
print(L)
L.pop(0)  # 根据索引删除指定元素
L[2] = 'Rell'  # 根据索引替换制定元素
#L.sort()#原地排序，默认升序，加上可选参数为降序,只能单一类型
#L.sort(reverse=True)#降序
T = ('Adam', 'Lisa', 'Bart')  # tuple是另一种有序的列表 tuple一旦创建完毕，就不能修改了。
Tb = ('Adam', 'Lisa', ['Bart', 'Paul'])  # 一个“可变”的tuple。
D = {'Adam': 99, 'Lisa': 99, "Bart": 99}  # 花括号 {} 表示这是一个dict,无序 key: value对应。key不能重复。
for key in D:
    print(key+':', D[key])  # 由于通过 key 可以获取对应的 value，因此，在循环体内，可以获取到value的值。
print('Adam:', D['Adam'])  # 使用 D[key] 的形式来查找对应的 value
D['Adam'] = 100  # 要把新同学'Paul'的成绩 72 加进去，用赋值语句：如果 key 已经存在，则赋值会用新的 value 替换掉原来的 value：
S = set(['Adam', 'Lisa', 'Bart'])  # set 持有一系列元素，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。
print('Adam' in S)  # 访问 set中的某个元素实际上就是判断一个元素是否在set中。
for name in S:
    print(name)  # 遍历set
S.add('Pual')#更新元素如果添加的元素已经存在于set中，add()不会报错，但是不会加进去了。
S.remove('Bart')  # 删除指定元素，如果删除元素不存在会报错。
R=r'c\n' #  转义字符 原样输出
print(R)
#列表推导式
import string #导入string这个模块
print (string.digits) #输出包含数字0~9的字符串
print (string.ascii_letters) #包含所有字母(大写或小写)的字符串
print (string.ascii_lowercase) #包含所有小写字母的字符串
print (string.ascii_uppercase) #包含所有大写字母的字符串