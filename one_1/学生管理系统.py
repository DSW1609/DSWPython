stu = []    # 用来保存所有学生信息
def menu():
    #显示菜单
    print(("=" * 30).center(30))
    print(("学生管理系统V2.0").center(18))
    print("1.添加学生信息",end='  ')
    print("2.删除学生信息")
    print("3.修改学生信息",end='  ')
    print("4.显示学生信息")
    print("5.导入学生信息",end='  ')
    print("5.导出学生信息")
    print("6.退出管理系统")
    print(("=" * 30).center(30))
def add_stu():
    #添加一个学生信息
    stu_name = input("请输入新学生的名字：")
    stu_sex = input("请输入新学生的性别：(男/女)")
    stu_score = int(input("请输入新学生的成绩："))
    new_stu = {"name":stu_name,"sex":stu_sex,"score":stu_score}
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
    new_score = int(input("请输入新成绩："))
    stu[stu_id]['name'] = new_name
    stu[stu_id]['sex'] = new_sex
    stu[stu_id]['score'] = new_score
    print("修改成功！")
def show_stu():
    print("=" * 15)
    print("学生信息如下：")
    print("=" * 15)
    print("序号  姓名  性别  成绩")
    i = 1
    for temp in  stu:
        print(i, temp['name'], temp['sex'], temp['score'])
        i += 1
def dr_stu():
    file = input("请输入文件路径：")
    fp = open(file,"r")
    data = fp.read();
    stu.append(data)
    print("导入成功")
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
            dr_stu()
        elif key == '6':
            print("再见！")
            break
# 运行main
main()


