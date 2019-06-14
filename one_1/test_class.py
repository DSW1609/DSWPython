# class Student:
#     def __init__(self,name,age,scores):
#         self.name = name
#         self.age = age
#         self.scores = scores
#     def get_name(self):
#         if isinstance(self.name,str):
#             return self.name
#     def get_age(self):
#         if isinstance(self.age,int):
#             return self.age
#     def get_scores(self):
#         M = max(self.scores)
#         if isinstance(M,int):
#             return M
# wjh = Student('王嘉辉',20,[99,99,100])
# print('姓名:',wjh.get_name(),end=' ')
# print('年龄:',wjh.get_age(),end=' ')
# print('最高成绩:',wjh.get_scores())
#
# class Course:
#     def __init__(self):
#         self.id = 1
#         self.name = 'Python'
#         self.teacher = 'zhang'
#         self.__address = 'jifang4'
# kecheng = Course()
# print('==课程信息==')
# print('编号:',kecheng.id)
# print('名称:',kecheng.name)
# print('教师:',kecheng.teacher)
# print('地点:',kecheng._Course__address)  # 正确写法

# from math import pi
# class Circle:
#     def __init__(self, r):
#         self.r = r  # 半径
#     def zhouchang(self):
#         return 2 * pi * self.r
#     def area(self):
#         return pi * self.r ** 2
# bj = Circle(int(input('请输入圆的半径：')))
# print('周长:',bj.zhouchang())
# print('面积:',bj.area())

class Animal:
    def __init__(self,color):
        self.__color = color
    def call(self):
        print("叫声:嗷嗷")
    def out(self):
        print("颜色",self.__color)
        self.call()
class Fish(Animal):
    def __init__(self,color,tail):
        Animal.__init__(self,color)
        self.__tail = tail
    def call(self):
        print("叫声:凸凸")
    def out(self):
        Animal.out(self)
        print("尾巴",self.__tail)
c1 = Animal('red')
c1.out()
c2 = Fish('blue','三角形')
c2.out()

