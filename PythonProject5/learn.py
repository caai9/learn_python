# print("hello world")
# print(123)
# print(123)
# h = 1
# print(h)
# """
# 三个引号是多行注释
# """
# # ctrl + F 查找
# # ctrl + D 复制到下一行
# print("123","123","312",sep='///')#sep设置间隔
# # end用来设置以什么结尾，默认\n
# print("123","123","312",sep='///',end='\t')#sep设置间隔
# print("123","123","312",sep='///',end='\t')#sep设置间隔
#
# num = 1+2j
# print(num,type(num))#检测数据类型
# name = '''sssss
# ssss
# ssss
# sssdasd'''#三引号可表示多行字符串
# print(name)
# # 占位符
# # %s 字符串, %d 整数 %3d %06d(000123)
# # %.4f(1.2300（四位小数）)
# name = 'asd'
# num=123
# print('名字:%s,%d'%(name,num))
# print('名字:%s,%06d'%(name,num))
# #
# #
# #f格式化
# print(f'{'(> <)'}不知道写什么{123444}')
#
# print(5/2)
# print(5//2)#整除
# print(5%2)#取余
#
#
# # input（）输入函数(字符串类型)
# q=input("{> <}\n")
# print(q)
#
# print("sadsdsd\rqeqweqweqwe")#\r将当前位置移到本行开头
#
# print("qweweqw\\tqweqwdae")
#
# print(r"dad\qweqwwqee")
#
#
# a=123
# if a<10:
#     print(a)
# else:
#     print(a+1)
#
# print(a+1) if a<10 else print(a+1)#三目运算符
#
# while a!=200:
#     a+=1
#     print(a)
#
# i=1
# while i<=100:
#     print(f"{i}:123")
#     i+=1
#
#
#
# k=1
# total=0
# while k<=100:
#     total+=k
#     k+=1
# print(total)
#
# strs='qwertyuiop'
# for str in strs:
#     print(str,end=' ')
#     str+='1'
#
# print('\n')
# for m in range(1,4):
#     print(m)
# number=0
# for num in range(1,101):
#     number+=num
#     if number >=100:
#         break
# print(number)

#字符串编码的转换
# # 编码:encode():将其他编码的字符串转换成Unicode编码
# # 解码:decode():将Unicode编码（二进制数据）转换成其他编码的字符串
# a='hello'
# print(a,type(a))
# a1=a.encode()#编码
# print(a.encode(),type(a.encode()))#bytes以字节为单位进行处理
# a2=a1.decode()
# print(a2,type(a2))#解码

#
# st='这里是...'
# str11=st.encode("utf-8")
# print(str11,type(str11))
# str12=str11.decode('utf-8')
# print(str12,type(str12))


# a='wqe'
# b='asd'
# print(a+b)# "+"表示字符串拼接
#
# print(a*2)# "*"表示重复输出


# sad='adadasaddabplkqwesad'
# if 'kz' in sad:
#     print('yes')
# else :
#     print('no')
#
# if 'kz' not in sad:
#     print('yes')
# else:
#     print('no')
# print('a' in sad)
# print('a' not in sad)
#
# print(sad[9])
# print(sad[3:9:2])
# print(sad[-1:])
# print(sad[:-1])
# print(sad[-1:-5:-1])#步长正负表示方向，正数表示左->右,步长方向要与起始到终止的方向一致
#

## find:检测某个子字符串是否包含在字符串中，如果在返回子字符串的第一次出现的开始位置的下标，否则返回-1
# name = 'qqazzxxccvvbbnnmmllkkjjds'
# print(name.find('xc'))
# print(name.find('xc',7,9))# 7 , 9是从字符串搜寻的范围
#
# # index():检测某个子字符串是否包含在字符串中，如果在返回子字符串的第一次出现的开始位置的下标，否则报错
# name = 'qqazzxxccvvbbnnmmllkkjjds'
# print(name.index('cv'))

# count:计数某个子字符串在字符串中出现次数
# name = 'qqazzxxccvvbbnnbmmbllkkjjds'
# print(name.count('b'))
# print(name.count('p'))
#
#
# NAME=name.upper()  # 大写
# name_1=NAME.lower()# 小写
# print(NAME,name_1)
# print(NAME.isupper())#检测是否所有都为大写
# print(NAME.islower())#检测是否所有都为小写
#
# po=name.startswith('qqa')#:判断是否以某个子字符串开头
# po_1=name.startswith('qa',1)#:判断是否以某个子字符串开头
# print(po,po_1)
#
# # op=name.endswith('ds')#判断结尾
# # print(op)
#
# # print(name.replace('jds','djs'))    # .replace(旧内容，新内容，替换次数（默认全替换）)
#
# # split:指定分隔符来分割字符串
# st = 'hello_world'
# # print(st.split('_'))
# # print(st.split(','))
# # print(st.split('o'))
# # print(st.split('o',1))
# #
#
# # capitalize():大写第一个字符,其他小写
# St=st.capitalize()
# print(st.capitalize())

# li=[1,2,'q',4]
# for i in li:
#     print(i)
#
#
# li.append('poi')#整体添加到最后
# li.extend('poi')#打散之后添加到最后
# li.insert(1,'poi')#插入到指定位置
# print(li)

# name=['qwe','asd','xc']
# NAME=input('请输入:')
# # if NAME in name:
# #     print('重复')
# # else:
# #     print('可以')
# #     name.append(NAME)
# #     print(name)
# while NAME in name:
#     print('重复')
#     NAME = input('请重新输入')
# name.append(NAME)
# print(name)


# del name      #删除列表
#
# del name[2]
# print(name)

# nm=name.pop(1)    #储存删除的元素
# print(name)
# print(nm)

# name.remove('asd')    #默认删除第一个指定元素
# print(name)



# name.sort()     #默认从小到大排列
# print(name)
#
# name.reverse()  #倒置列表
# print(name)


# [print(i) for i in name]
# num=[1,2,3,4,5,6,7,8,9]
# [print(i) for i in range(1,11) if i%2==1]
#
# [print(i) for i in name if i=='qwe']
#
#
# li=[1,2,3,[4,5,6]]
# print(li[3])
# print(li[3][1])



# asd=(1,2,'zzz',4,'12',6)    #只有一个元素时，要末尾加‘,’,否则返回该元素类型
# print(type(asd))
# zzz=('zxc')
# zzz1=('zxc',)
# print(type(zzz),type(zzz1))
# print(asd[-1])  #元组不支持修改



# dic={'qaz':12,'qwe':23} #键名重复会覆盖
# print(dic)
#
# print(dic['qwe'])
# print(dic.get('qaz'))
# print(dic.get('waz','不存在'))#若不存在返回，‘不存在’
#
# dic['qwe']=33#若存在键名则修改，否则增添
# print(dic)

# del dic#删除整个字典
# del dic['qwe']
# print(dic)

# dic.clear()#清空字典
# print(dic)


# nnn=dic.pop('qwe')
# print(dic)
# print(nnn)

# dic.popitem()   #删除最后一个
# print(dic)


# print(len(dic))
#
#
#
# print(dic.keys())#返回键名
#
# for i,j in dic.keys(),dic.values():
#     print(i,j)

# print(dic.items(),type(dic.items()))#返回所有键值对
# dic1={} #定义空字典
#
#
#
# s1={1,2,3,3,3,4,2}  #集合，不能修改集合的值,但可以自动去掉重复元素
# s2=set()    #定义空集合
# print(s1,type(s1))
# s3={'1','q','f','b','lp','1','q'}#若非数字，则按随机顺序输出（哈希表）
# print(s3)
# s3.add('qwe')#一次只能添加一个,添加整体
# print(s3)
# s3.update('asdfghjkl','zxcvbnm')#拆分后添加
# s3.update((1,2,3))#拆分后添加
# print(s3)
#
# s3.remove(3)
# print(s3)
#
# s1.pop()#pop():若是数字int型，则删除第一个，否则随机删除(随机排序后的第一个元素)
# print(s1)
# s4={'1','2','3','4'}
# s4.pop()
# print(s4)
#
# #discard:若元素存在则删除元素，若没有不会报错
# s4={'1','2','3','4'}
# s4.discard('1')
# print(s4)
#
#
# a={1,2,3,4}
# b={3,4,5,6}
# print(a & b)    #'&':交集
#
# print(a | b)    #'|':并集


#
# print(int('213'))#只能转纯数字和正负号组成的字符串或数字（int）->整数
# print(int('-213'))#只能转纯数字和正负号组成的字符串或数字（int）->整数
# print(int(1.234))#只能转纯数字组成的字符串或数字（int）
#
# age = input('年龄:')
# if int(age) >= 18:
#     print("成年")


# print(float(-11))
# print(float(-11.123))
#
#
#
# li=[1,2,3,4]
# print(type(str(li)))#任何类型都能转换成str

# print(10+10)    #20
# print('10'+'10')#1010
# print('10+10')  #10+10

# print(eval('10+10'))#20,eval:执行运算并返回运算值

# #eval()可以实现list,dict,tuple,str之间的转换,但容易被恶意修改数据
# st1='[[1,2],[3,4],[5,6]]'
# li=eval(st1)
# print(li,type(li))
#
# st2="{'name':'asd','age':19}"
# dic=eval(st2)
# print(dic,type(dic))

# list:将可迭代对象（str,tuple,dict,set）转换成列表
# print(list('asdasdsa'))
# print(list({'3',3,'qwe'}))#依然是随机，同时会自动去重
# print(list({'name':'asd','age':'18'}))#list转换字典，只保留键名



#     #深浅拷贝
# li=[1,2,3,4]
# print(li)
# li2 = li
# print(li,li2)
# li.append(9)
# print(li,li2)
# #赋值相当于指向同一个位置
# #copy:创建新的对象，拷贝数据，嵌套层会指向原来的内存地址,（外层地址不同，内层地址相同），浅拷贝,优点：拷贝速度快，占用空间少，拷贝效率高
# import copy
# li = [1,2,3,[4,5,6]]
# li2=copy.copy(li)#第一个copy是库，第二个是copy函数,浅拷贝
# print(li,li2)
# print('id(li):',id(li),'id(li2):',id(li2))#内存地址不同，不是同一个对象
# li.append(8)
# print(li,li2)
# li2.append(898)
# print(li,li2)
# print(li[3])     #取出嵌套列表
# li[3].append(78) #嵌套层会指向原来的内存地址,即修改原列表的嵌套列表都会改变
# print(li,li2)
# print('id(li):',id(li),'id(li2):',id(li2),'id(li[3]):',id(li[3]),'id(li2[3]):',id(li2[3]))#内存地址不同，不是同一个对象

# #深拷贝(数据完全不共享)
# import copy
# li = [1,2,3,[4,5,6]]
# li2 = copy.deepcopy(li)#深拷贝
# print('li:',li,id(li))
# print('li2:',li2,id(li2))
# print('li[3]:',li[3],id(li[3]))
# print('li2[3]:',li2[3],id(li2[3]))
# li.append(8)
# print('li:',li,id(li))
# print('li2:',li2,id(li2))
#
# li[3].append(8123)
# print('li:',li,id(li))
# print('li2:',li2,id(li2))
# print('li[3]:',li[3],id(li[3]))
# print('li2[3]:',li2[3],id(li2[3]))


# # 可变类型:列表，字典，集合(地址不随内容改变而改变)
# li=[1,2,3,4]
# print("li原",li,id(li))
# li.append(6)
# print('li',li,id(li))

# #不可变对象:int,bool,float,complex,str,tuple(变量对应值不能被修改，若修改则生成新的值并分配新的地址)
# n=10
# print(n,id(n))
# n=15
# print(n,id(n))




# def qwe():
#     print('123')
# qwe()

# def log_in():
#     k=input(":")
#     print(k)
# log_in()

#
# def hello():
#     print('hello')
# hello()

# def buy():
#     return 'hello',12#返回多个值时，为元组形式，若无返回值,则返回NONE
# print(buy())
#
# def add(a,b):   #形参
#     return a+b
# print(add(5,6)) #实参



#     #函数参数
#     #1.必备参数（位置参数）
# def fun(name1,name2,name3):
#     print(name1)
#     print(name2)
#     print(name3)
# fun('q','w','e')
#
#     #2.默认参数(若无实参则调用默认值)
# def func(qwe='www',asd='asd',zcx='zxc'):#默认参数要放在位置参数后面
#     print(qwe)
#     print(asd)
#     print(zcx)
# func('pio','lkj',)
#
#     #3.可变参数(传入的值的数量可以改变,可以传入多个，也可以一个或不传)(以元组形式接收)
# def funa(*args):
#     print(args)
# funa()
# funa(1)
# funa(1,3)
#
#
# #     #4.关键字参数(以字典形式接收，其他同可变参数)
# # def funb(**kwargs):
# #     print(kwargs)
# # funb()#空字典
# # funb(name='fangyuan',age='500')#以键=值形式传参
#
#
#
#     #函数嵌套
#         #嵌套调用（在函数中掉用另一个函数）
# def study():
#     print('学习')
# def course():
#     study()
#     print("python")
# course()
#
#
#     #嵌套定义
# def study1():#外函数
#     print('学习')
#     def course1():#内函数（需要在外函数中调用）(内层不能调用外层)
#         print('python')
#     course1()
#     print('累了')
# study1()


#     #作用域（全局变量(函数外部定义) / 局部变量（函数内部定义,只在函数内有效））
#         #global关键字将变量声明为全局变量    用法:global 变量名
#         #nonlocal:将变量声明为外层变量（外层函数的局部变量，并且不能是全局变量）
# a=100       #全局变量
# def test1():
#     print(a)
# test1()
# def test2():
#     a=129   #局部变量
#     print(a)
# print('前',a)#100
# test1()#100
# test2()#129
# print('后',a)#100
#
#
# a=100       #全局变量
# def test1():
#     print(a)
# test1()
# def test2():
#     global a ,age   #声明为全局变量
#     a=129   #局部变量
#     print(a)
#     age = 18
# print('前',a)#100
# test1()#100
# test2()#129
# print('后',a)#129
# print('age:',age)

# a=10
# def outer():
#     a = 5
#     print('outer中的a（前）:',a)
#     def inner():    #局部变量先从本层寻找，若无，则从外层寻找
#         # a=190
#         print('inner中的a:',a)
#     inner()
#     print('outer中的的a(后):',a)
# outer()
#
# a=10
# def outer():
#     a = 5
#     print('outer中的a（前）:',a)
#     def inner():    #局部变量先从本层寻找，若无，则从外层寻找
#         nonlocal a  #nonlocal:   只对上一层进行修改，不对上上一层进行修改
#         a=190
#         print('inner中的a:',a)
#     inner()
#     print('outer中的的a(后):',a)
# outer()


#     #匿名函数   函数名 = lambda 形参:返回值     结果 = 函数名（实参）
# # name = lambda name1:print(name1)
# add = lambda a,b : a+b  #a+b是返回值不需要return
# k=add(2,4)
# print(k)
#
# funa = lambda : '好东西'   #无参数
# print(funa())
#
# funb = lambda name : name
# print(funb('qwe'))
#
# func = lambda name,age=18:(name,age)    #多个以元组形式
# print(func('asd'))
# print(func('asd',500))
#
# fune = lambda **kwargs : kwargs
# print(fune(name="qweqweqwe",age=12))

#
# comp = lambda  a,b : print('a>b') if a>b else print('a<b')
#
# comp(7,8)
# comp(77,8)





# import  builtins        #查看内置函数
# print(dir(builtins))


# print(min(-8,5,key=abs))    #求绝对值之后的最小值


# # zip():将可迭代对象中的参数打包成多个元组:(1,'a'),(2,'b'),(3,'c')
# li=[1,2,3]
# li2=['a','b','c']
# print(zip(li,li2))
#
#     #取出zip中的元素（方式一）
# for i in zip(li,li2):   #如果元素个数不一致，则按照长度最短的返回
#     print(i)
#     #转换成列表（方式二）
# print(list(zip(li,li2)))


# # map():将可迭代对象中的每一个元素进行映射，分别去执行
# # map(func,iter1):func:自己定义的函数,iter1:可迭代对象(iter1中每个值分别作为参数传入func中执行)
# li=[1,2,3,4]
# def add(a):
#     return a+8
# mp=map(add,li)#结果为对象形式，取出方法同zip
# print(mp)
# print(list(mp))


# # reduce:先取出列表中前两个元素传入函数，再将结果与第三个元素传入函数,直到全部元素都被使用
# from functools import reduce
# # reduce(function,sequence)#function:有两个参数的函数,sequence:可迭代对象
# def add(x,t):
#     return x*t
# li2=[1,2,3,4]
# k=reduce(add,li2)
# print(k)

# # 拆包
# #含义:对于函数中的多个返回数据，去掉元组等直接获取里面的数据的过程
# tua = (1,2,3,4)
# print(tua)
#     #方法一
# a,b,c,d = tua
# print(a,b,c,d)#元组内的个数必须与接收的个数相同
#
#     #方法二
# a,*b = tua
# print(a,b)
#
# def funa(a,b,*args):
#     print(a,b)
#     print(args,type(args))
# funa(1,2,45,45654,5,6546)



# 抛出异常 raise()
# 1.创建一个Exception('xxx')对象，xxx->异常提示信息
# 2.raise抛出这个异常对象

# # raise Exception('异常')
# raise Exception('123')
# def funa():
#     print('hhh')
#     raise Exception('这是异常')#raise执行后，代码不会继续往下执行
#     print('kkk')
# funa()

# def login():
#     mm  = input('请输入6位数的密码')
#     if len(mm) <  6 or len(mm) >= 7:
#         raise Exception('密码位数不对')
#     else:
#         return mm
# # print(login())
# try:    #捕获异常，程序可以继续执行
#     print(login())
# except Exception as e:  #将异常提示信息保存到e中
#     print(e)


    # 模块（一个py文件就是一个模块）
#     分类：1.内置模块，2.第三方模块，3.自定义模块
# import 模块名  ,会从头到尾执行一遍模块,调用时需要模块名,如:
                                # 模块名.函数()
                                # 模块名.变量
#from  模块名 import 功能   ,调用时不需要模块名
# from  模块名 import *    ,导入所有,若命名有冲突,则会报错

# import 模块名 as 别名

# 内置全局变量__name__
# if __name__ == '__main__':    作用:用来控制py文件在不同的应用场景执行不同的逻辑（只会在__name__ = "main"出现在当前执行文件时，才会执行）
# __name__
# 1.文件在当前程序执行:__name__== '__main__'  ,会执行
# 2.文件被其他文件导入:__name__== 模块名        ,不会执行

# if __name__ == "__main__":
#     print("zxc")          #会执行zxc

# import test
# test.test1()



# 包:项目结构中的文件夹/目录,包含有__init__.py的文件
#作用:将有联系的模块放到同一个文件夹下，有效避免模块名称冲突
# import导入包时，首先执行__init__.py文件的代码，再去执行其他模块中的函数
#导包方式1: import pack_01
#       2. from pack_01 import qweq
#          qweq.assd()

# import pack_01  #若在__init__中调用包内函数，则导包时就会直接执行

# __all__:本质上是一个列表,列表内元素代表要导入的模块

    #方法一:
# from pack_01 import * #此方法只能导入__init__.py中的函数
# qweq.assd()
    #方法二 :
# import pack_01.qweq
# pack_01.qweq.assd()
    # 或
# import pack_01.qweq as q
# q.assd()

    #方法三 :
# from pack_01.qweq import assd
# assd()
#
#
#


    #文件操作
# open():创建一个file对象，默认是以只读模式打开
# read(n):n表示从文件中读取的数据长度，若无n或n为负数则默认一次性读取所有内容
# write():将指定内容写入文件
# close():关闭文件

    # 属性
# 文件名.name:返回要打开的文件的文件名,包含路径
# 文件名.mode:返回文件访问模式
# 文件名.closed:检测文件是否关闭,关闭就返回true

# # 打开文件
# f=open('learn_test.txt')    #返回对象
# print(f.name)
# print(f.mode)
# print(f.closed)
# print(f.read())
# # 关闭文件
# f.close()
# print(f.closed)


    # 读写操作
# f=open('learn_test.txt')
# k=f.read(13)
# print(k)
# f.close()

# f=open(r'C:\Users\hszmx\Desktop\cmdsd.txt')
# k=f.read()
# print(k)
# f.close()

# readline():读取一行，执行完毕后会将文件指针移到下一行，准备再次读取
# f=open('learn_test.txt')
# k0=f.readline()
# print(k0)
# k1=f.readline()
# print(k1)
# k2=f.readline()
# print(k2)
# print(f.readline())
# print(f.readline())
# print(f.readline())
    #按行打印
    #方法一
# while True:
#     text = f.readline()
#     #读取不到内容，退出循环
#     if not text:
#         break
#     else:
#         print(text)

    #方法二
# for i in f :
#     print(i)
#
# f.close()

#readlines():按照行的方式，读取所有内容，返回一个列表，每一行是一个元素
# f=open('learn_test.txt')
# print(f.readlines())
# f.close()

# 访问模式(r:只读（文件必须存在） , w:只写（文件存在就会先清空原有内容，若不存在就创建新文件）)
# + :表示可以同时读写文件，但会影响效率
# r+ :可读写文件，文件必须存在
# w+ :先写在读，文件存在就会先清空原有内容，若不存在就创建新文件
# a  :追加，文件存在在原有内容基础上添加内容，若不存在就创建新文件
#文件指针:标记从哪个位置读取数据
# f=open('learn_test.txt','w+')
# f.write('cnasm')    #写入后，文件指针在最后
# print(f.tell())
# f.seek(0)
# print(f.read())
# f.close()

# f=open('learn_test.txt','a')
# f.write('21ewdscxvv')
# f.close()

# tell():显示文件指针当前位置
# seek(offset,whence):移动文件指针到指定位置
# offset:表示要移动的字节数
# whence:起始位置，表示移动字节的参考位置,默认是0(文件开头),    1（代表当前位置），2（文件结尾）

# f=open('learn_test.txt','r+')
# f.seek(5)
# f.write('cnmsdsdd')    #写入后，文件指针在最后
# print(f.tell())
# f.seek(0)
# print(f.read())
# f.close()




# # 递归函数(必须要有明确的结束条件)
#
# def plus(n):
#     if n==1:
#         return 1
#     return n + plus(n-1)
# k=plus(100)
# print(k)
#
# def funa(n):
#     if n<=2:
#         return 1
#     return funa(n-1)+funa(n-2)
# print(funa(6))



    # 闭包
# def outer():
#     n = 10
#     def inner():
#         print(n)
#     return inner
# # print(outer())  #返回内函数的内存地址
# outer()()   #调用
#
# k=outer()
# k() #调用内函数

# def outer(m):
#     n = 10
#     def inner(k):
#         print(n+m+k)
#         return ('eweq')
#     return inner
# outer(22)(3)
# print(outer(22)(3))

    #装饰器(闭包函数)(不修改原程序，不改变调用方法)
# def test02():
#     print('qwes')
# def test(fn):
#     fn()
# test(test02)
#
# def sum12(a,b,fn):
#     fn(a,b)
#
#     return a+b
# def cheng(a,b):
#     print(a*b)
# print(sum12(2,5,cheng))

# def send():
#     print('sss')
# def outer(fn):
#     def inner():
#         fn()
#     return inner
# outer(send)()

# # 语法糖
# # 格式:@装饰器名称
# def outer22(fn):
#     def inner():
#         print('qweee')
#         fn()
#     return inner
# @outer22
# def send():
#     print('sss')
# send()



