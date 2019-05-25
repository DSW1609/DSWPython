def menu():
    print("====欢迎使用简易计算器====")
    print('1.加',end = ' '*2)
    print('2.减',end = ' '*2)
    print('3.乘',end = ' '*2)
    print('4.除')
    print('5.求余',end = ' '*10)
    print('6.取整')
def jia(a, b):
    print(a,'+',b,'=',a+b)
    return a,b
def jian(a, b):
    print(a,'-',b,'=',a-b)
    return a,b
def cheng(a, b):
    print(a,'*',b,'=',a*b)
    return a,b
def chu(a, b):
    print(a,'/',b,'=',a/b)
    return a,b
def qy(a, b):
    print(a,'%',b,'=',a%b)
    return a,b
def qz(a, b):
    print(a,'//',b,'=',a//b)
    return a,b
def main():
    while True:
        menu()
        a = int(input('请输入数字：'))
        b = int(input('请输入数字：'))
        I = int(input('请选择要进行的操作:(1-6)'))
        if I == 1:
            jia(a,b)
        elif I == 2:
            jian(a, b)
        elif I == 3:
            cheng(a, b)
        elif I == 4:
            chu(a, b)
        elif I == 5:
            qy(a, b)
        elif I == 6:
            qz(a, b)
        S = input('是否继续运算？(Y/N)')
        if S == 'Y' or S == 'y':
            continue
        else:
            print('再见！')
            break
main()

