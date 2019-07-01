stu = []    # 用来保存所有学生信息
dc = []     # 用来保存导出数据时的返回值
def menu():
    #显示菜单
    print(("=" * 30).center(30))
    print(("学生管理系统V2.0").center(18))
    print("1.添加学生信息",end='  ')
    print("2.删除学生信息")
    print("3.修改学生信息",end='  ')
    print("4.显示学生信息")
    print("5.导入学生信息",end='  ')
    print("6.导出学生信息")
    print("7.退出管理系统",end='  ')
    print("*请先导入学生信息！")
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
def del_stu(stu):
    # 删除一个学生信息
    del_num = int(input("请输入要删除的序号：")) - 1
    del stu[del_num]
    print("删除成功！")
def modify_stu(stu):
    # 修改学生信息
    stu_id = int(input("请输入要修改的序号：")) - 1
    new_name = input("请输入新名字：")
    new_sex = input("请输入新性别：(男/女)")
    new_score = int(input("请输入新成绩："))
    stu[stu_id]['name'] = new_name
    stu[stu_id]['sex'] = new_sex
    stu[stu_id]['score'] = new_score
    print("修改成功！")
def show_stu():
    # 输出所有学生信息
    print("=" * 15)
    print("学生信息如下：")
    print("=" * 15)
    print("学号    姓名    性别    成绩")
    i = 1701
    for temp in  stu:
        print("%d   %s    %s     %s" % (i, temp['name'], temp['sex'], temp['score']))
        i += 1
def dr_stu():
    # 导入所有学生信息
    global stu
    with open(r"D:\DSW\Python\file\stu.data") as file:
        data = file.read()
    stu = eval(data)
    print("导入成功")
def dc_stu():
    # 导出新添加的学生信息
    with open(r"D:\DSW\Python\file\stu.data","w") as file:
        file.write(str(stu))
    # 添加到列表,退出时验证是否为空
    dc.append(1)
def main():
    # 循环输出菜单
    while True:
        menu()    # 打印菜单
        key = input("请输入对应的数字：")
        if key == '1':
            add_stu()
        elif key == '2':
            if len(stu):    # 验证stu列表是否为空，为空提示先导入学生信息
                del_stu(stu)
            else:
                print("请先导入学生信息")
                continue
        elif key == '3':
            if len(stu):
                modify_stu(stu)
            else:
                print("请先导入学生信息")
                continue
        elif key == '4':
            if len(stu):
                show_stu()
            else:
                print("请先导入学生信息")
                continue
        elif key == '5':
            dr_stu()
        elif key == '6':
            dc_stu()
            print("导出成功")
        elif key == '7':
            # 检测dc是否为空
            if len(dc):
                print("再见！")
            else:
            # 为空时调用导出函数保存到文件
                dc_stu()
                print("已为您自动保存！")
                print("再见！")
            break
        else:
            print("输入错误请重新输入！")
            continue
# 运行main
main()


