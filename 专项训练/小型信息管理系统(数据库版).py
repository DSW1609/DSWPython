import os.path
import sqlite3
class stuDB:
    def __init__(self):
        self.con = ""
        self.cur = ""
    def connect(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        try:
            sql = "create table stu(no integer,name text,sex text,age integer)"
            self.cur.execute(sql)
        except:
            pass
    def close(self):
        self.con.commit()
        self.cur.close()
        self.con.close()
    def show(self):
        formatstr = "{:5}\t{:5}\t{:5}\t{:5}"
        print(formatstr.format("工号","姓名","性别","年龄"))
        sql = "select * from stu "
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for row in rows:
            print(formatstr.format(str(row[0]).strip(),row[1],row[2],str(row[3]).strip()))
    def __enterAge(self):
        while True:
            age = int(input("年龄："))
            if 20 <= age <= 60:
                break
            else:
                print("输入错误，年龄应在20到60之间")
        return age
    def __exists(self,no):
        sql = "select * from stu where no = ?"
        result = self.cur.execute(sql,(no,))
        rows = result.fetchall()
        if len(rows) > 0:
            return True
        else:
            return False
    def __insert(self,no,name,sex,age):
        if self.__exists(no):
            print("该工号已经存在")
        else:
            try:
                sql="insert into stu(no,name,sex,age) values(?,?,?,?)"
                self.cur.execute(sql,(no,name,sex,age))
                if self.cur.rowcount > 0:
                    print("插入成功")
                else:
                    print("插入失败")
            except :
                print("错误")
    def __update(self,no,name,sex,age):
        if not self.__exists(no):
            print("该员工不存在")
        else:
            try:
                sql="update stu set name = ?,sex = ?,age = ? where no = ?"
                self.cur.execute(sql,(name,sex,age,no))
                if self.cur.rowcount > 0:
                    print("修改成功")
                else:
                    print("修改失败")
            except:
                print("错误")
    def __delete(self,no):
        if not self.__exists(no):
            print("该员工不存在")
        else:
            sql = "delete from stu where no = ?"
            self.cur.execute(sql,(no,))
            if self.cur.rowcount > 0:
                print("删除成功")
            else:
                print("删除失败")
    def insert(self):
        no = input("工号：")
        name = input("姓名：")
        sex = input("性别：")
        age = self.__enterAge()
        if no != "" and name != "" and sex != "" :
            self.__insert(no,name,sex,age)
        else:
            print("请将信息输入完整")
    def delete(self):
        no = input("请输入要删除的工号：")
        if no != "":
            self.__delete(no)
    def update(self):
        no = input("请输入要修改的工号:")
        name = input("姓名：")
        sex = input("性别：")
        age = self.__enterAge()
        if no != "" and name != "" and sex != "":
            self.__update(no,name,sex,age)
        else:
            print("请将信息输入完整")
    def export(self):
        try:
            fn = input("请输入要导出的文件路径与名称:")
            with open(fn,"w") as fp:
                self.cur.execute("select * from stu")
                rows = self.cur.fetchall()
                for row in rows:
                    fp.write(str(row[0]) + ',' + row[1] + ',' + row[2] + ',' + str(row[3]) + '\n')
                print("导出完毕")
        except Exception as err:
            print(err)
    def load(self):
        try:
            fn = input("请输入要导入的文件路径:")
            if os.path.exists(fn):
                with open(fn,"r") as fp:
                    while True:
                        s = fp.readline().strip("\n")
                        if s == "":
                            break
                        st = s.split(",")
                        self.__insert(int(st[0]),st[1],st[2],int(st[3]))
                    print("导入完毕")
            else:
                print("文件不存在")
        except Exception as err:
            print(err)
    def process(self,db):
        self.connect(db)
        print(("信息管理系统V3.0").center(20))
        print("1.显示员工信息", end='  ')
        print("2.插入员工信息")
        print("3.删除一个员工", end='  ')
        print("4.修改员工信息")
        print("5.导出员工数据", end='  ')
        print("6.导入员工数据")
        print("7.退出管理系统")
        while True:
            print("请选择:显示|插入|删除|修改|导出|导入|退出")
            s = input(">").strip().lower()
            if s == "显示":
                self.show()
            elif s == "插入":
                self.insert()
            elif s == "删除":
                self.delete()
            elif s == "修改":
                self.update()
            elif s == "导出":
                self.export()
            elif s == "导入":
                self.load()
            elif s =="退出":
                print("再见！")
                break
            else:
                print("输入错误请重新输入！")
        self.close()
emd = stuDB()
emd.process("D:/DSW/Python/file/stu.db")