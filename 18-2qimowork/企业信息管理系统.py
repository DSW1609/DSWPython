YG = []  # 保存员工信息
def menu():
    print(("=" * 30).center(30))
    print(("企业管理系统").center(18))
    print("1.添加员工")
    print("2.修改员工")
    print("3.删除员工")
    print("4.显示数据")
    print("5.导入数据")
    print("6.导出数据")
    print("7.退出系统")
def add_YG():
    global YG
    #添加一个员工信息
    YG_Num = int(input("请输入新员工的工号："))
    YG_Name = input("请输入新员工的姓名：")
    YG_Age = int(input("请输入新员工的年龄："))
    new_YG = {"Num":YG_Num,"Name":YG_Name,"Age":YG_Age}
    # 存储到员工列表
    YG.append(new_YG)
    print("添加成功！")
def xg_YG(YG):
    while True:
        xg_Name = input("请输入要修改的员工姓名：")
        for new in YG:
            if xg_Name == new.get("Name"):
                new_Num = int(input("请输入的新工号："))
                new_Age = int(input("请输入的新年龄："))
                new = {"Num":new_Num,"Name":xg_Name,"Age":new_Age}
                return new
            else:
                print(xg_Name,"不存在，请重新输入！")
                continue
def main():
    YG_info = []
    while True:
        menu()    # 打印菜单
        print(YG)
        key = input("请输入对应的数字：")
        if key == '1':
            YG_info = add_YG()
        elif key == '2':
            YG_info = xg_YG()
# 运行main
main()
