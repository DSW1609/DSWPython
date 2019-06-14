# file = "D:\DSW\Python\pyfile.txt"
# fp = open(file,'w')
# s = ["22\n","33\n","44\n","11\n","15"]
# fp.writelines(s)
# fp.close()
# fp2 = open(file,'r')
# data = fp2.read().split('\n')
# fp2.close()
# data.sort(reverse=True)
# print(' '.join(data))

# import os
# import os.path
# os.chdir(r"D:\DSW\Python")
# fnlist = [fn for fn in os.listdir(os.getcwd())
#           if os.path.isfile(fn) and fn.endswith('.txt')]
# for f in fnlist:
#     newname = f[:-4] + '_new.txt'
#     os.rename(f,newname)

file = "D:\DSW\Python\TXTcs\yingwen.txt"
fp = open(file,'r')
data = fp.readline()
fp.close()
N = []
for i in data:
    if i>='A' and i <='Z':
        i = i.lower()
        N.append(i)
    else:
        i = i.upper()
        N.append(i)
print(''.join(N))
