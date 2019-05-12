stu = []    # 用来保存所有学生信息
def menu():
    #显示菜单
    print(("=" * 30).center(30))
    print(("学生管理系统V1.0").center(18))
    print("1.添加学生信息",end='  ')
    print("2.删除学生信息")
    print("3.修改学生信息",end='  ')
    print("4.显示学生信息")
    print("5.学生平均成绩",end='  ')
    print("6.退出管理系统")
    print(("=" * 30).center(30))
def add_stu():
    #添加一个学生信息
    stu_name = input("请输入新学生的名字：")
    stu_sex = input("请输入新学生的性别：(男/女)")
    stu_score1 = int(input("请输入新学生的成绩1："))
    stu_score2 = int(input("请输入新学生的成绩2："))
    new_stu = {}
    new_stu['name'] = stu_name
    new_stu['sex'] = stu_sex
    new_stu['score1'] = stu_score1
    new_stu['score2'] = stu_score2
    # 存储到stu列表里
    stu.append(new_stu)
    print("添加成功！")
def del_stu(student):
    # 删除一个学生信息
    del_num = int(input("请输入要删除的序号：")) - 1
    del student[del_num]
    print("删除成功！")
def modify_stu():
    stu_id = int(input("请输入要修改的学生信息：")) - 1
    new_name = input("请输入新名字：")
    new_sex = input("请输入新性别：(男/女)")
    new_score1 = int(input("请输入新成绩1："))
    new_score2 = int(input("请输入新成绩2："))
    stu[stu_id]['name'] = new_name
    stu[stu_id]['sex'] = new_sex
    stu[stu_id]['score1'] = new_score1
    stu[stu_id]['score2'] = new_score2
    print("修改成功！")
def pj_stu():
    for temp in  stu:
        pj_score = (temp['score1']+ temp['score2'])/2
        print(temp['name'],"平均成绩",pj_score)
def show_stu():
    print("=" * 15)
    print("学生信息如下：")
    print("=" * 15)
    print("序号  姓名  性别  成绩1  成绩2")
    i = 1
    for temp in  stu:
        print(" %d   %s  %s   %s    %s" % (i, temp['name'], temp['sex'], temp['score1'], temp['score2']))
        i += 1
def main():
    while True:
        menu()    # 打印菜单
        key = input("请输入对应的数字：")
        if key == '1':
            add_stu()
        elif key == '2':
            del_stu(stu)
        elif key == '3':
            modify_stu()
        elif key == '4':
            show_stu()
        elif key == '5':
            pj_stu()
        elif key == '6':
            print("再见！")
            break
# 运行main
main()


