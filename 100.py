# import heapq
# import time
# from functools import wraps
# from math import degrees  # day5
# from operator import index
# from turtledemo.penrose import start
#
# from markdown_it.rules_inline import image
# from pygments.lexer import words

# weight =int( input('请输入体重'))
# match weight:   #同C中的switch case
#     case 200 : k=200
#     case 300 : k=300
#     case _ :     k=666  #case后要有空格
# print(k)


# x=float(input('请输入x\n'))
# if x>1:
#     y=3*x-5
# elif x>-1:
#     y=x+2
# else:
#     y=5*x+3
# print(y)


# grade = int(input('请输入成绩\n'))
# if grade>=90:
#     print('A')
# elif grade>=80:
#     print('B')
# elif grade>=70:
#     print('C')
# elif grade>=60:
#     print('D')
# else:
#     print('E')


               # day6
# import time
# for _ in range(0,3600):
#     print("hello world")
#     time.sleep(1)
# total=0
# for i in range(2,101,2):
#     total+=i
# print(total)
# print(sum(range(2,101,2)))
#
# i=2
# total=0
# while i<=100:
#     total+=i
#     i+=2
# print(total)
# i=2
# total=0
# while True:
#     total+=i
#     if i==100:
#         break
#     i += 2
# print(total)

# for i in range(1,10):
#     for j in range(i,10):
#         print(f'{i}*{j}={i*j}',end='\t')
#     print()
# cnt=0
# x=int(input("请输入x\n"))
# if x<2:
#     raise Exception('x必须大于2')
# for i in range(2,x):
#     if x%i==0:
#         cnt=1
#         break
# if cnt==0:
#     print('不是素数')
# else:
#     print('是素数')

# x0=int(input('第一个:'))
# x1=int(input('第二个:'))
# for i in range(min(x0,x1),0,-1):
#     if x0 % i ==0 and x1 % i ==0:
#         print(i)
#         break
# import random
# x=random.randrange(1,100)
# y=int(input('请猜\n'))
# cnt=1
# while x!=y:
#     if y > x:
#         print('大了')
#     if y < x:
#         print('小了')
#     y = int(input('请猜\n'))
#     cnt+=1
# print('对了',cnt)



               # day7
# num=[1,1]
# for i in range(2,20):
#     k=num[i-1]+num[i-2]
#     num.append(k)
#     print(k)
#
# a,b=0,1
# for _ in range(20):
#     a,b=b,a+b
#     print(a)

# for i in range(100,1000):
#     ge=i%10
#     shi=i//10%10
#     bai=i//100
#     if ge**3+shi**3+bai**3==i:
#         print(i)

# x=int(input('请输入'))
# num=[]
# while x !=0:
#     kk=x%10
#     x=x//10
#     num.append(kk)
# for i in num:
#     print(i,end='')

# x=input('请输入')
# num=list(x)
# for i in num[-1::-1]:
#     print(i,end='')

# num=int(input('num='))
# reverser_num = 0
# while num > 0:
#     reverser_num = reverser_num * 10 + num % 10
#     num//=10
# print(reverser_num)

# for i in range(0,21):
#     for j in range(0,100,3):
#         for l in range(0,34):
#             money=5*i+j//3+l*3
#             num=i+j+l
#             if num==100 and money==100:
#                 print(i,j,l)
#
# for i in range(0,21):
#     for j in range(0,100,3):
#             money=5*i+j//3+(100-i-j)*3
#             if  money==100 and 100-i-j>=0:
#                 print(i,j,100-i-j)

# import random
# money_total = 1000
# while money_total > 0:
#     xia_zhu_money = int(input('请下注\n'))
#     while xia_zhu_money > money_total:
#         print('nm哪来的钱')
#         xia_zhu_money = int(input('请下注\n'))
#     ju_shu = 1
#     score0 = random.randrange(1,7)
#     score1 = random.randrange(1,7)
#     score = score0 + score1
#     print(f'骰子一:{score0},骰子二:{score1},总和:{score}')
#     if ju_shu ==1 and (score ==7 or score==11):
#         money_total += xia_zhu_money
#         print("玩家胜")
#         print()
#         print(money_total)
#     elif ju_shu ==1 and (score == 2 or score == 3 or score ==12):
#         money_total-=xia_zhu_money
#         print("庄家胜")
#         print()
#         print(money_total)
#     elif ju_shu == 1:
#         ju_shu = 2
#         score2 = 0
#         while ju_shu == 2 and score2 != 7 and score2 != score:
#             print('继续')
#             score0 = random.randrange(1, 7)
#             score1 = random.randrange(1, 7)
#             score2 = score0 + score1
#             print(f'骰子一:{score0},骰子二:{score1},总和:{score2}')
#             if score2 == 7:
#                 money_total -= xia_zhu_money
#                 print("庄家胜")
#                 print()
#                 print(money_total)
#                 break
#             elif score2 == score:
#                 money_total += xia_zhu_money
#                 print("玩家胜")
#                 print()
#                 print(money_total)
#                 break
# print('破产')

                #day8
# import random
# f1=0
# f2=0
# f3=0
# f4=0
# f5=0
# f6=0
# for _ in range(6000):
#     k=random.randrange(1,7)
#     if k == 1:
#         f1+=1
#     elif k == 2:
#         f2+=1
#     elif k == 3:
#         f3+=1
#     elif k == 4:
#         f4+=1
#     elif k == 5:
#         f5+=1
#     elif k == 6:
#         f6+=1
# print(f1,f2,f3,f4,f5,f6)


# import random
# count = [0]*6
# for _ in range(6000):
#     k = random.randrange(1, 7)
#     count[k-1]+=1
# print(count)

                #day9
# languages = ['Python','Java','C++']
# languages.append('JavaScript')
# print(languages)
# languages.insert(1,'SQL')
# print(languages)
# if 'Java' in languages:
#     languages.remove('Java')
#     print(languages)
# temp = languages.pop(1)
# print(languages)
# print(temp)
# languages.clear()
# print(languages)

# languages = ['Python','Java','C++','Python']
# languages.remove('Python')
# print(languages)
# del languages[1]
# print(languages)

# languages = ['Python','Java','C++','Python']
# print(languages.index('C++'))
# print(languages.index('Python'))
# print(languages.index('Python',1))
# print(languages.count('Python'))    #出现次数

# languages.sort()               #排序
# print(languages)
# languages = ['Python','Java','C++','Python']
# languages.reverse()            #反转
# print(languages)



# items = []
# for i in range(1,100):
#     if i%3==0 or i%5==0:
#         items.append(i)
# print(items)
#
# items = [ i for i in range(1,100) if i%3==0 or i%5==0]
# print(items)

# nums1 = [1,2,3,4,5,6,7,8,9]
# nums2 = [num**2 for num in nums1]
# print(nums2)

# nums1 = [2,4,55,66,34,677,234,12,4645]
# nums2 = [num for num in nums1 if num>50]
# print(nums2)

# score = [[22,66,77],[66,77,88],[99,88,88]]
# print(score[0])
# print(score[0][2])

# scores = []
# for _ in range(5):
#     temp = []
#     for _ in range(3):
#         score=int(input('请输入三个成绩\n'))
#         temp.append(score)
#     scores.append(temp)
# print(scores)
#
# import random
# scores = [[random.randrange(60,101) for  _ in range(3)] for  _ in range(5)]
# print(scores)
# import  random
# scores = [random.randrange(1,34) for _ in range(6)]
# blue = random.randrange(1,17)
# scores.append(blue)
#
# for _ in range(7):
#     k=int(input('请猜一个球\n'))
#     if k in scores:
#         scores.remove(k)
# if scores == []:
#     print("中了")

# import random
# red_balls = list(range(1,34))
# selected_balls = []
# for _ in range(6):
#     index = random.randrange(len(red_balls))
#     selected_balls.append(red_balls.pop(index))
# selected_balls.sort()
# for ball in selected_balls:
#     print(f'\033[031m{ball:0>2d}\033[0m',end=' ')
# blue_ball = random.randrange(1,17)
# print(f'\033[034m{blue_ball:0>2d}\033[0m')

# import random
# red_balls = [i for i in range(1,34)]
# blue_balls = [i for i in range(1,17)]
#
# selected_balls = random.sample(red_balls,6)     #sample():随机选取多个元素(不重复)
# selected_balls.sort()
# for ball in selected_balls:
#     print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# blue_ball  =random.choice(blue_balls)             #choice():随机选取一个元素
# print(f'\033[034m{blue_ball:0>2d}\033[0m')



# import random
# n=int(input("请输入"))
# red_balls = [i for i in range(1,34)]
# blue_balls = [i for i in range(1,17)]
# for _ in range(n):
#     selected_balls = random.sample(red_balls,6)     #sample():随机选取多个元素(不重复)
#     selected_balls.sort()
#     for ball in selected_balls:
#         print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
#     blue_ball  =random.choice(blue_balls)             #choice():随机选取一个元素
#     print(f'\033[034m{blue_ball:0>2d}\033[0m')





# import random
#
# from rich.console import Console
# from rich.table import Table
#
# console = Console()
#
# n=int(input("请输入"))
# red_balls = [i for i in range(1,34)]
# blue_balls = [i for i in range(1,17)]
# table = Table(show_header=True)
# for col_name in ('序号','红球','蓝球'):
#     table.add_column(col_name,justify='center')
# for i in range(n):
#     selected_balls = random.sample(red_balls,6)     #sample():随机选取多个元素(不重复)
#     selected_balls.sort()
#     blue_ball  =random.choice(blue_balls)             #choice():随机选取一个元素
#     table.add_row(
#         str(i + 1),
#         f'[red]{" ".join([f"{ball:0>2d}"for ball in selected_balls])}[/red]',
#         f'[blue]{blue_ball:0>2d}[/blue]'
#     )
# console.print(table)


                    # day10
# t1 = (33,333,222,2123)
# t2 = (9,99,8,84,45)
# print(t2[:])
# print((t1[1:3]))
# for i in t1:
#     print(i)
# print(33 in t1)
# print(33 in t2)
# print(99 not in t2)
# t3 = t1+t2
# print(t3)
#
# t4=('g',)#定义单元素元组
#
# #解包
# i,j,k,l=t1
# print(i,j,k,l)
#
# z,x,*c = t2
# print(z,x,c)

# a=5
# b=9
# a,b = b,a#交换值
# print(a,b)

        #day11

# s2='!'*3
# print(s2)

# print(ord('h')) #ord():获取编码
# print(ord('乔'))
# s='hello world'
# print(len(s))

# s = 'abc123456'
# n = len(s)
# print(s[0], s[-n])
# for i in range(len(s)):
#     print(s[i])
# for i in s:
    # print(i)

# S=s.capitalize()    #首字母大写
# print(S)
# S0=s.title()        #每个单词首字母大写
# print(S0)
# S1 = s.upper()
# print(S1)
# s0 = s.lower()
# print(s0)

# print(s.find('34',0))
# print(s.index('34',2))  #正向查找
#
# print(s.rfind('34',0))
# print(s.rindex('34',0)) #反向查找


# print(s.startswith('ab'))#是否以...开头
# print(s.endswith('ab'))#是否以...结尾
#
# print(s.isdigit())  #判断是否完全以数字组成
# print(s.isalpha())  #判断是否完全以字母组成
# print(s.isalnum())  #判断是否完全以数字和字母组成


# s0 = 'hello world'
# print(s0.center(20,'*'))    #在左右添加*并补充成20字节,居中
# print(s0.rjust(20,'*'))#将字符串 s0 右对齐 显示，总长度固定为 20 个字符；
# # 如果 s0 的长度小于 20，左侧用空格补齐；如果 s0 长度≥20，则直接显示原字符串（不截断）。
# print(s0.ljust(20,'*'))#左对齐
# print('33'.zfill(5))#左侧补零至5个字节
# print('-33'.zfill(5))#-0033


# a=321
# b=123
# print('%d*%d=%d'%(a,b,a*b))

# s1 = '      qwe       '
# print(s1.strip())
# s2 = '?qwe?'
# print(s2.lstrip('?'))
# print(s2.rstrip('?'))

# s='hello world'
# print(s.replace('l','zzz'))
# print(s.replace('l','zzz',1))
#
# k=s.split()     #拆分
# print(k)
# print('~'.join(k))  #用~合并

            # day12
set1 = {1,2,3,4,5,6,7}
set2 = {2,4,6,8,10}
# print(set1 & set2)  #交集
# print(set1.intersection(set2))    #交集
#
# print(set1 | set2)  #并集
# print(set1.union(set2))#并集
#
# print(set1 - set2)#差集
# print(set1.difference(set2))#差集
#
# print(set1 ^ set2)#对称差
# print(set1.symmetric_difference(set2))#对称差

# print(set1<=set2)#判断set1是否为set2的子集
# print(set1<set2)#判断set1是否为set2的真子集
# print(set1.issubset(set2))#判断set1是否为set2的子集
#
# print(set1>set2)#判断set1是否为set2的超集
# print(set1.issuperset(set2))#判断set1是否为set2的超集

# set2.add(0) #添加
# print(set2)
# set2.discard(0) #删除
# print(set2)
# set2.clear()#清空
# print(set2)
# set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
# for elem in set1:
#     print(elem)

# print(set1.isdisjoint(set2))#判断两个集合有没有相同的元素，如果没有相同元素，该方法返回True，否则该方法返回False
#
# fset1 =frozenset(range(1,6))    #不可变集合(除了不可以添加或删除，其他同集合)


        #day13
# items = dict(zip('ABCDE','12345'))
# print(items)
#
# for key in items:   #只对键进行遍历
#     print(key)
#
# print(items.get('A'))
# print(items.keys())#获取所有键
# print(items.values())#获取所有值
# print(items.items())#获取所有键值对

# person1 = {'name': '王大锤', 'age': 55, 'height': 178}
# person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
# # person1.update(person2) #将person2中的键值对更新到person1中
# person1 |= person2  #同update()
# print(person1)  # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
#
# print(person1.popitem())#删除获得键和值



# 输入一段话，统计每个英文字母出现的次数，按出现次数从高到低输出。
# sentence = input('请输入一段话:')
# counter = {}
# for ch in sentence:
#     if 'A' < ch <'Z' or 'a'<ch<'z':
#         counter[ch] = counter.get(ch,0) + 1 #counter.get(ch,0):获取ch的值，若不存在则返回0
# sorted_keys = sorted(counter, key=counter.get,reverse=True)#sorted(可迭代对象, key=排序依据, reverse=是否降序)
# for key in sorted_keys:
#     print(f'{key}出现了{counter[key]}次')



# 在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
# stocks = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# # dic = {}
# # for key,value in stocks.items():
# #     if value > 100:
# #        dic[key] = value
# # print(dic)
# stocks2 = {key : value for key ,value in stocks.items() if value>100}
# print(stocks2)



            # day14

# def accumulate(n):
#     consequence=1
#     for i in range(1,n+1):
#         consequence*=i
#     return consequence
# consequence0 = accumulate(7)//(accumulate(3)*accumulate(4))
# print(consequence0)

# from math import factorial
# print(factorial(7)//factorial(3)//factorial(4))


            # day15

# # 设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置。
# import random
# import string
#
# ALL_CHARS = string.digits + string.ascii_letters #string.digits:所有数字形成的字符串，
#                                                  # string.ascii_letters：大小写字母形成的字符串
# def generate_code(code_len=4):
#     k=random.sample(ALL_CHARS,code_len)
#     return ''.join(k)   #拼接
# for _ in range(5):
#     print(generate_code(6))




#设计一个判断给定的大于1的正整数是不是质数的函数。
#质数是只能被1和自身整除的正整数（大于1），如果一个大于 1 的正整数N是质数，
#那就意味着在 2 到N-1之间都没有它的因子。

# def zhi_shu():
#     num = int(input('请输入\n'))
#     isprime = 1
#     for i in range(2,num):
#         if num % i != 0:
#             isprime = 1
#         else:
#             isprime = 0
#             break
#     if isprime == 1:
#         print('是质数')
#     else:
#         print('不是质数')
# zhi_shu()


# def is_prime(num:int) ->bool:
#     for i in range(2,int(num ** 0.5)+1):
#         if num % i == 0:
#             return False
#     return True
# print(is_prime(9))






# def gcd(x,y):
#     for i in range(min(x,y),0,-1):
#         if x % i ==0 and y % i == 0:
#             return i
#
# def lcm(x,y):
#     for i in range(max(x,y), x * y + 1):
#         if i % x == 0 and i % y == 0 :
#             return i
#
# print(lcm(4,3))
# print(gcd(9,6))



# def lcm(x:int,y:int)->int:
#     return x*y//gcd(x,y)
# def gcd(x:int,y:int)->int:
#     while y%x!=0:
#         x,y = y%x,x
#     return  x
# print(lcm(4,3))
# print(gcd(9,6))





# def sample_mean(*x):
#     x_total = sum(x)
#     y = x_total / len(x)
#     return y
#
# def sample_variance(*x):
#     x_total = 0
#     for i in range(len(x)):
#         x_total += (x[i]-sample_mean(*x))**2
#     y = x_total/(len(x)-1)
#     return y
#
# def sample_standard_deviation(*x):
#     y =sample_variance(*x)**0.5
#     return y
#
# def coefficient_of_sample_variation(*x):
#     y = sample_standard_deviation(*x)/sample_mean(*x)
#     return y
#
# def ji_cha(*x):
#     y = max(x)-min(x)
#     return y
#
# def zhong_wei_shu(*x):
#     if len(x) % 2 == 1:
#         y1  = x[len(x)//2]
#         return y1
#     elif len(x) % 2 == 0:
#         y1 = x[len(x)//2-1]
#         y2 = x[len(x)//2]
#         y =(y1+y2)/2
#         return y
#
# def total(*x):
#     y0 = sample_mean(*x)
#     y1 = sample_variance(*x)
#     y2 = sample_standard_deviation(*x)
#     y3 = coefficient_of_sample_variation(*x)
#     y4 = ji_cha(*x)
#     y5 = zhong_wei_shu(*x)
#     print(f"样本均值:{y0},样本方差:{y1},样本标准差:{y2},变异系数:{y3},极差:{y4},中位数:{y5}")
#     return y0,y1,y2,y3,y4,y5
# total(4,5,67,8,9,4,9,876,5,5,4,6)



                #day16

# def calc(init_value,op_func,*args,**kwargs):
#     items = list(args)+list(kwargs.values())
#     result = init_value
#     for item in items:
#         if type(item) in (int,float):
#             result  = op_func(result,item)
#     return result
#
# def add(x,y):
#     return x+y
# def mul(x,y):
#     return x*y
# print(calc(0,add,1,2,3,4))
# print(calc(1,mul,1,2,3,4))


# def is_even(num):
#     return num%2==0
# def square(num):
#     return num**2
# old_nums = [35,12,8,99,60,52]
# new_nums = list(map(square,filter(is_even,old_nums)))   #filter:筛选;map:对所有元素执行操作
# print(new_nums)

# old_nums = [35,12,8,99,60,52]
# new_nums = [i**2 for i in old_nums if i %2==0]
# print(new_nums)


# old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
# new_strings = sorted(old_strings)
# print(new_strings)  # ['apple', 'in', 'pear', waxberry', 'zoo']
#
# old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
# new_strings = sorted(old_strings,key=len)
# print(new_strings)  # ['apple', 'in', 'pear', waxberry', 'zoo']


# # lambda :匿名函数
# old_nums = [35,12,8,99,60,52]
# new_nums = list(map(lambda x:x**2,filter(lambda x:x%2==0,old_nums)))
# print(new_nums)


# import functools
#
# int2 = functools.partial(int ,base = 2)
# int8 = functools.partial(int ,base = 8)
# int16 = functools.partial(int ,base = 16)
# print(int('1001'))    # 1001
# print(int2('1001'))   # 9
# print(int8('1001'))   # 513
# print(int16('1001'))  # 4097



                        #day17
# import time
# def record_time(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f'{func.__name__},{end-start:.9f}')
#         return result
#     return wrapper
# @record_time
# def add(x,y):
#     time.sleep(0.001)
#     return x+y
# add(5,6)
# # time0 = record_time(add)
# # time0(5,6)

# def fac(num):
#     if num == 1:
#         return 1
#     else:
#         return num * fac(num-1)
# print(fac(3))

# from functools import lru_cache
# @lru_cache()        #缓存该函数的执行结果从而避免在递归调用的过程中产生大量的重复运算
# def fib1(num):
#     if num == 1 or num ==2:
#         return 1
#     return fib1(num-1)+fib1(num-2)
# for i in range(1,51):
#     print(fib1(i))

                            # day18


# import time
#
# class Clock:
#     def __init__(self,hour = 0,minute = 0,second=0):
#         self.hour = hour
#         self.min = minute
#         self.sec = second
#
#     def run(self):
#         self.sec +=1
#         if self.sec ==60:
#             self.sec=0
#             self.min+=1
#             if self.min==60:
#                 self.min = 0
#                 self.hour+=1
#                 if self.hour==24:
#                     self.hour=0
#     def show(self):
#         return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'
#
# clock = Clock()
# while True:
#     print(clock.show())
#     time.sleep(1)
#     clock.run()


# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#     def qiu(self,x,y):
#         self.x =int(input('请输入'))
#         self.y =int(input('请输入'))
#         return ((self.x-x)**2+(self.y-y)**2)**0.5
#
# point = Point()
# print(point.qiu(5,6))


# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#     def distance_to(self,other):
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return (dx*dx+dy*dy)**0.5
#     def __str__(self):
#         return f'({self.x},{self.y})'
#
# p1 = Point(4,6)
# p2 = Point(6,8)
# print(p1)
# print(p2)
# print(p1.distance_to(p2))


                                    #day19
# class Student:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#
#     def study(self,courage_name):
#         print(f'{self.__name},{courage_name}')
# stu = Student('qwe',22)
# stu.study('eee')
#
#
# class Student:
#     __slots__ = ('name', 'age') #使类无法进行外部添加属性
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def study(self, courage_name):
#         print(f'{self.name},{courage_name}')
#
#
# stu = Student('qwe', 22)
# stu.study('eee')


                                #day20

#     # 扑克游戏
# from enum import Enum
#
# class Suite(Enum):
#     SPADE,HEART,CLUB,DIMOND =   range(4)
#
# # for suite in Suite:
# #     print(f'{suite}:{suite.value}')
#
# class Card:
#     def __init__(self,suite,face):
#         self.suite = suite
#         self.face =  face
#     def __repr__(self):
#         suites = '♠♥♣♦'
#         faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#         return  f'{suites[self.suite.value]}{faces[self.face]}'
#     def __lt__(self,other):
#         if self.suite == other.suite:
#             return self.face < other.face
#         return self.suite.value < other.suite.value
#
# # card1 =Card(Suite.SPADE,5)
# # card2 =Card(Suite.HEART,13)
# # print(card1)
# # print(card2)
#
# import random
#
# class Poker:
#     def __init__(self):
#         self.cards = [Card(suite,face)
#                       for suite in Suite
#                       for face in range(1,14)]
#         self.current = 0
#
#     def shuffle(self):
#         self.current = 0
#         random.shuffle(self.cards)
#
#     def deal(self):
#         card = self.cards[self.current]
#         self.current +=1
#         return card
#     @property
#     def has_next(self):
#         return self.current<len(self.cards)
#
# # poker = Poker()
# # print(poker.cards)
# # poker.shuffle()
# # print(poker.cards)
#
#
# class Player:
#     def __init__(self,name):
#         self.name = name
#         self.cards = []
#     def get_one(self,card):
#         self.cards.append(card)
#     def arrange(self):
#         self.cards.sort()
#
# poker = Poker()
# poker.shuffle()
# players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
# for _ in range(13):
#     for player in players:
#         player.get_one(poker.deal())
#
# for player in players:
#      player.arrange()
#      print(f'{player.name}:',end=' ')
#      print(player.cards)


#     # 工资结算系统
#
# class Employee:
#     def __init__(self,work_time=0):
#         self.monthly_salary = 0
#         self.work_time = work_time
#     def moon_money(self):
#         return f'{self.monthly_salary}'
#
# class Department_Manager(Employee):
#     def __init__(self):
#         super().__init__()
#         self.monthly_salary = 15000
#
# class Programmer(Employee):
#     def __init__(self,work_time):
#         super().__init__(work_time)
#
#     def moon_money(self):
#         self.monthly_salary = 200 * self.work_time
#         return super().moon_money()
#
# class Salesperson(Employee):
#     def __init__(self,sales_volume):
#         super().__init__()
#         self.sales_volume = sales_volume
#     def moon_money(self):
#         self.monthly_salary = 1800 + self.sales_volume*0.05
#         return super().moon_money()
# mana = Department_Manager()
# print(mana.moon_money())
#
# pro = Programmer(200)
# print(pro.moon_money())
#
# sal = Salesperson(180000)
# print(sal.moon_money())





# from abc import ABCMeta,abstractmethod
#
# class Employee(metaclass=ABCMeta):
#
#     def __init__(self,name):
#         self.name = name
#
#     @abstractmethod
#     def get_salary(self):
#         pass
#
# class Manager(Employee):
#     def get_salary(self):
#         return 15000.0
#
# class Programmer(Employee):
#     def __init__(self,name,working_hour=0):
#         super().__init__(name)
#         self.working_hour = working_hour
#
#     def get_salary(self):
#         return 200 * self.working_hour
#
# class Salesman(Employee):
#     def __init__(self,name,sales=0):
#         super().__init__(name)
#         self.sales = sales
#
#     def get_salary(self):
#         return 1800 + self.sales * 0.05
# emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Salesman('张辽')]
# for emp in emps:
#     if isinstance(emp,Programmer):      #isinstance(对象, 类)，判断一个对象是否属于指定的类（或其子类）
#         emp.working_hour = int(input(f'请输入{emp.name}本月工作时间:'))
#     elif isinstance(emp,Salesman):
#         emp.sales = float(input(f'请输入{emp.name}本月销售量:'))
#     print(f'{emp.name}本月工资为:{emp.get_salary():.2f}元')



                                    # day21
# file = open('致橡树.txt','r',encoding='utf-8')
# # print(file.read())
# # file.close()
#
# # for line in file:
# #     print(line,end=' ')
# # file.close()
#
# lines = file.readline()
# for line in lines:
#     print(line,end=' ')
# file.close()


# file = open('致橡树.txt','a',encoding='utf-8')
# file.write('\n标题:《致橡树》')
# file.write('\n作者:舒婷')
# file.write('\n时间:1977年3月')
# file.close()

# file = None
# try:
#     file = open('致橡树.txt','r',encoding='utf-8')
#     print(file.read())
# except FileNotFoundError:
#     print('无法打开指定的文件!')
# except LookupError:
#     print('指定了未知的编码!')
# except UnicodeDecodeError:
#     print('读取文件时解码错误!')
# finally:
#     if file:
#         file.close()


# class InputError(ValueError):
#     """自定义异常类型"""
#     pass
#
# def fac(num):
#     if num <0 :
#         raise InputError('只能计算非负整数的阶乘')
#     if num in (0,1):
#         return 1
#     return num * fac(num - 1)
#
# flag = True
# while flag:
#     num = int(input('n= '))
#     try:
#         print(f'{num}! = {fac(num)}')   #若此处fac(num)抛出异常，则会被下面的Except捕获，才会进一步执行except下面的代码
#         flag = False
#     except InputError as err:
#         print(err)





# try:
#     with open('致橡树.txt','r',encoding='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('无法打开指定的文件!')
# except LookupError:
#     print('指定了未知的编码!')
# except UnicodeDecodeError:
#     print('读取文件时解码错误!')


# try:
#     with open('guido。jpg','rb') as file1:
#         data = file1.read()
#     with open('吉多.jpg','wb') as file2:
#         file2.write(data)
# except FileNotFoundError:
#     print('指定的文件无法打开')
# except IOError:
#     print('读写文件时出现错误')
# print('程序执行结束')


# try:
#     with open('guido.jpg','rb') as file1,open('吉多.jpg','wb') as file2:
#         data = file1.read(512)
#         while data:
#             file2.write(data)
#             data = file1.read()
# except FileNotFoundError:
#     print('指定的文件无法打开')
# except IOError:
#     print('读写文件时出现错误')
# print('程序执行完成')


                                    #day22
                                    # JSON
# import json
# my_dict={
#     "name":"周星驰",
#     "age":40,
#     "friends":["汪东城","白远方"],
#     "cars" : [
#         {'brand': 'BWM',  "max_speed": 240},
#         {'brand': 'Audi', 'max_speed': 280},
#         {'brand': 'Benz', 'max_speed': 280}
#
#     ]
# }
# # print(json.dumps(my_dict))
# with open('data.json','w') as file:
#     json.dump(my_dict,file)
#
# with open('data.json','r') as file:
#     my_dict = json.load(file)
#     print(type(my_dict))
#     print(my_dict)

# import requests
#
# resp = requests.get('https://api.tianapi.com/guonei/?key=APIKey&num=10')
# if resp.status_code == 200:
#     data_model = resp.json()
#     for news in data_model['newslist']:
#         print(news['title'])
#         print(news['url'])
#         print('-'*60)

# import requests
# from lxml import etree
# url = 'https://www.baidu.com'
# resp = requests.get(url)
# resp.encoding = 'utf-8'
# if resp.status_code == 200:
#     # print(resp.text)
#     html = etree.HTML(resp.text)
#     title = html.xpath('//title/text()')
#     print('标题:',title[0])

# import requests
# from lxml import etree
# from PIL import Image
# from io import BytesIO
#
# headers = {
#     'User-Agent' : "Mozilla/5.0"
# }
# url = 'https://ys.mihoyo.com/'
# resp = requests.get(url,headers=headers)
# resp.encoding = 'utf-8'
# if resp.status_code == 200:
#     html = etree.HTML(resp.text)
#     title = html.xpath('//title/text()')
#     print(title[0])
#     img_list = html.xpath('//img/@src')
#     if img_list:
#         img_src = img_list[0]
#
#         if img_src.startswith('//'):
#             img_url = 'https:' + img_src
#         else:
#             img_url = img_src
#         print(img_url)
#
#         img_resp = requests.get(img_url,headers=headers)
#         img = Image.open(BytesIO(img_resp.content))
#         img.show()
#     else:
#         print("未找到图片")
                            # day23
                            # csv
# import csv
# import random
#
# with open('scores.csv','w',encoding='utf-8',newline='') as file:
#     writer = csv.writer(file,delimiter='|',quoting=csv.QUOTE_ALL)
#     writer.writerow(['姓名','语文','数学','英语'])
#     names = ['关羽','张飞','赵云','马超','黄忠']
#     for name in names:
#         scores = [random.randrange(50,101) for _ in range(3)]
#         scores.insert(0,name)
#         writer.writerow(scores)

# import csv
# with open('scores.csv','r',encoding='utf-8') as file :
#     reader = csv.reader(file,delimiter=',')
#     for data_list in reader:#将每行取成一个列表
#         print(reader.line_num,end='\t')
#         for elem in data_list:
#             print(elem,end='\t')
#         print()
                        #day28

# from PIL import Image
#
# image0 = Image.open('Default.jpg')
# print(image0.format)
# print(image0.size)
# print(image0.mode)
# # image0.show()
# # image0.crop((80, 20, 310, 360)).show()#裁剪
#
# # image0.thumbnail((1280,1280))#缩放
# # image0.show()
#
# image1 = Image.open('rm.png')
# print(image1.size)
# image12 = image1.crop((60,40,260,120))
# image12.show()
# width,height = image12.size
# image0.paste(image12.resize((int(width/1.5),int(height/1.5))),(1012,660))
# image0.show()
# image12.rotate(45).show()#旋转45度
# image12.transpose(Image.FLIP_TOP_BOTTOM).show()#上下翻转
# image12.transpose(Image.FLIP_LEFT_RIGHT).show()#左右翻转

# for x in range(80,310):
#     for y in range(20,300):
#         image0.putpixel((x,y),(128,128,128))
# image0.show()

# from PIL import ImageFilter
# image0.filter(ImageFilter.CONTOUR).show()
# image1.show()
# image1.filter(ImageFilter.CONTOUR).show()
# image1.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
# image1.filter(ImageFilter.EMBOSS).show()
# image1.filter(ImageFilter.BLUR).show()


# import random
# from PIL import Image,ImageDraw,ImageFont
#
# def random_color():
#     red = random.randint(0,255)
#     green = random.randint(0,255)
#     blue = random.randint(0,255)
#     return red,green,blue
# width,height = 800,600
# image00 = Image.new(mode='RGB',size=(width,height),color=(255,255,255))
# drawer = ImageDraw.Draw(image00)
# font = ImageFont.load_default()
# drawer.text((300,50),'Hello World!',fill=(255,0,0),font=font)
# drawer.line((0,0,width,height),fill=(0,0,255),width=2)
# drawer.line((width,0,0,height),fill=(0,0,255),width=2)
# xy = width//2-60,height//2-60,width//2+60,height//2+60
# drawer.rectangle(xy,outline=(255,0,0),width=2)
# for i in range(4):
#     left,top,right,bottom = 150+i*120,220,310+i*120,380
#     drawer.ellipse((left,top,right,bottom),outline=random_color(),width=8)
# image00.show()
                            #day30
# import re
# username = input('请输入用户名:')
# qq = input('请输入QQ号:')
# m1 = re.match(r'[0-9a-zA-Z_]{6,20}$',username)
# if not m1:
#     print('请输入有效用户名.')
# m2 = re.match(r'[1-9]\d{4,11}',qq)
# if not m2:
#     print('请输入有效QQ号.')
# if m1 and m2:
#     print('有效')

# import re
# pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
# sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
# 不是15600998765，也不是110或119，王大锤的手机号才是15600998765。'''
# 方法一
# tels_list = re.findall(pattern,sentence)
# for tel in tels_list:
#     print(tel)

#方法二
# for temp in pattern.finditer(sentence):
#     print(temp.group())

# 方法三
# m = pattern.search(sentence)
# while m :
#     print(m.group())
#     m=pattern.search(sentence,m.end())



# import re
# sentence = 'Oh, shit! 你是傻逼吗? Fuck you.'
# purified = re.sub('fuck|shit|[傻煞沙]|[比笔逼叉缺吊碉雕]','*',sentence,
#                   flags=re.IGNORECASE)
# print(purified)

# import re
# poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
# sentences_list = re.split(r'[，。]',poem)
# sentences_list = [sentence for sentence in sentences_list if sentence]
# for sentence in sentences_list:
#     print(sentence)
#                     #day31
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# prices2 = {key:value for key,value in prices.items() if value >100}
# print(prices2)

# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
#
# scores = [[None]*len(courses) for _ in names ]
# for row,name in enumerate(names):
#     for col,course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}的成绩'))
# print(scores)


# import heapq
#
# list1= [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print(heapq.nlargest(3,list1))
# print(heapq.nsmallest(3,list1))
# print(heapq.nlargest(2,list2,key=lambda x:x['price']))
# print(heapq.nlargest(2,list2,key=lambda x:x['shares']))

# import heapq

# nums = [10, 3, 8, 9, 15, 2, 7, 20, 1, 25]
# print(heapq.nlargest(4,nums))
# print(heapq.nsmallest(5,nums))

# students = [
#     {'name': '小明', 'score': 88},
#     {'name': '小红', 'score': 95},
#     {'name': '小刚', 'score': 72},
#     {'name': '小李', 'score': 100},
#     {'name': '小王', 'score': 63}
# ]
# print(heapq.nlargest(3,students,key=lambda x:x['score']))



# goods = [
#     {'name': '手机', 'price': 3999, 'sales': 1200},
#     {'name': '电脑', 'price': 6999, 'sales': 500},
#     {'name': '耳机', 'price': 299, 'sales': 3500},
#     {'name': '平板', 'price': 2499, 'sales': 800},
#     {'name': '手表', 'price': 1299, 'sales': 2100}
# ]
# print(heapq.nlargest(2,goods,key=lambda x:x['price']))
# print(heapq.nsmallest(3,goods,key=lambda x:x['sales']))


# import itertools
# A=list(itertools.permutations('ABCD'))
# B=list(itertools.combinations('ABCDE',3))
# C=list(itertools.product('ABCD','123'))
# D=itertools.cycle(('A','B','C'))
# print(A)
# print(B)
# print(C)
# print(next(D))
# print(next(D))
# print(next(D))
# print(next(D))
# print(next(D))


# import itertools
# # 请补全代码
# result = list(itertools.permutations('123'))
# print(result)


# import itertools
# # 请补全
# result = list(itertools.combinations('WXYZ', 2))
# print(result)




# import itertools
# result = list(itertools.product(['红','蓝'], ['大','小']))
# print(result)


# import itertools
#
# it = itertools.cycle(('↑','→','↓','←'))
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))



# from collections import Counter
#
# # words = [
# #     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# #     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
# #     'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
# #     'look', 'into', 'my', 'eyes', "you're", 'under'
# # ]
# # counter = Counter(words)
# # print(counter.most_common(3))
#
#
# num = [1,2,3,4,436,45,745,76,57,457,457,57,45,745,7,45,5,3532,523,42,2,47,8,9,679,2,967,7,56,4]
# counter = Counter(num)
# print(counter.most_common(2))

# def select_sort(items,comp=lambda x,y:x<y):
#     """简单选择排序"""
#     items = items[:]
#     for i in range(len(items)-1):
#         min_index = i
#         for j in range(i+1,len(items)):
#             if comp(items[j],items[min_index]):
#                 min_index=j
#         items[i],items[min_index] = items[min_index],items[i]
#     return items


# def bubble_sort(items,comp = lambda x,y:x>y):
#     items = items[:]
#     for i in range(len(items)-1):
#         swapped = False
#         for j in range(len(items)-1-i):
#             if comp(items[j],items[j+1]):
#                 items[j],items[j+1] = items[j+1],items[j]
#                 swapped=True
#         if not swapped:
#             break
#     return items
#
# num = [1,2,3,4,436,45,745,76,57,457,457,57,45,745,7,45,5,3532,523,42,2,47,8,9,679,2,967,7,56,4]
# print(bubble_sort(num))



# def bubble_sort(items,comp=lambda x,y:x>y):
#     items = items[:]
#     for i in range(len(items)-1):
#         swapped = False
#         for j in range(len(items)-1-i):
#             if comp(items[j],items[j+1]):
#                 items[j],items[j+1]=items[j+1],items[j]
#                 swapped = True
#         if swapped:
#             swapped=False
#             for j in range(len(items)-2-i,i,-1):
#                 if comp(items[j-1],items[j]):
#                     items[j],items[j-1]=items[j-1],items[j]
#                     swapped=True
#         if not swapped:
#             break
#     return items
# num = [1,2,3,4,436,45,745,76,57,457,457,57,45,745,7,45,5,3532,523,42,2,47,8,9,679,2,967,7,56,4]
# print(bubble_sort(num))


# def merge(items1,items2,comp=lambda x,y:x<y):
#     items = []
#     index1,index2 = 0,0
#     while index1<len(items1) and index2<len(items2):
#         if comp(items1[index1],items2[index2]):
#             items.append(items1[index1])
#             index1+=1
#         else:
#             items.append(items2[index2])
#             index2+=1
#     items += items1[index1:]
#     items += items2[index2:]
#     return items
# def merge_sort(items,comp=lambda x,y:x<y):
#     return _merge_sort(list(items),comp)
#
# def _merge_sort(items,comp):
#     if len(items)<2:
#         return items
#     mid = len(items)//2
#     left = _merge_sort(items[:mid],comp)
#     right = _merge_sort(items[mid:],comp)
#     return merge(left,right,comp)
# num = [1,2,3,4,436,45,745,76,57,457,457,57,45,745,7,45,5,3532,523,42,2,47,8,9,679,2,967,7,56,4]
# # print(merge_sort(num))
#
#
# def seq_search(items,key):
#     for index,item in enumerate(items):
#         if item==key:
#             return index
#     return -1
#
# print(seq_search(merge_sort(num),57))
#
# #
# def bin_search(items,key):
#     start,end=0,len(items)-1
#     while start<=end:
#         mid = (start+end)//2
#         if key>items[mid]:
#             start=mid+1
#         elif key<items[mid]:
#             end=mid-1
#         else:
#             return mid
#     return -1
#
# print(bin_search(merge_sort(num),57))



# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只

# for x in range(20):
#     for y in range(33):
#         for z in range(300):
#             if x+y+z==100 and x*5+y*3+z/3==100:
#                 print(f'公鸡:{x}只,母鸡{y}只,小鸡:{z}只')





# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

# fish0=6
# # (((fish-1)/5)*4)**5
# cnt=0
# while True:
#     fish = fish0
#     for i in range(5):
#         if (fish-1)%5==0:
#             fish = (fish-1)//5*4
#             cnt+=1
#         else:
#             break
#     if cnt == 5:
#         print(fish0)
#         break
#     cnt=0
#     fish0+=5

"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""

# class Thing(object):
#     def __init__(self,name,price,weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#     @property
#     def value(self):
#         return self.price/self.weight
# def input_thing():
#     name_str,price_str,weight_str = input().split()
#     return name_str,int(price_str),int(weight_str)
#
# def main():
#     max_weight,num_of_things = map(int,input().split())
#     all_things = []
#     for _ in range(num_of_things):
#         all_things.append(Thing(*input_thing()))
#     all_things.sort(key=lambda x:x.value,reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + thing.weight<=max_weight:
#             print(f'小偷拿走了{thing.name}')
#             total_weight+=thing.weight
#             total_price+=thing.price
#     print(f'总价值: {total_price}美元')
#
# if __name__=='__main__':
#     main()



# import sys
# import time
# SIZE=5
# total = 0
#
# def print_board(board):
#     for row in board:
#         for col in row:
#             print(str(col).center(4),end='')
#         print()
# def patrol(board,row,col,step=1):
#     if row>=0 and row<SIZE and \
#         col>=0 and col<SIZE and \
#         board[row][col] == 0:
#         board[row][col] = step
#         if step==SIZE*SIZE:
#             global total
#             total+=1
#             print(f'第{total}种走法: ')
#             print_board(board)
#         patrol(board, row - 2, col - 1, step + 1)
#         patrol(board, row - 1, col - 2, step + 1)
#         patrol(board, row + 1, col - 2, step + 1)
#         patrol(board, row + 2, col - 1, step + 1)
#         patrol(board, row + 2, col + 1, step + 1)
#         patrol(board, row + 1, col + 2, step + 1)
#         patrol(board, row - 1, col + 2, step + 1)
#         patrol(board, row - 2, col + 1, step + 1)
#         board[row][col]=0
#
# def main():
#     board = [[0]*SIZE  for _ in range(SIZE)]
#     patrol(board,SIZE-1,SIZE-1)
#
# if __name__=='__main__':
#     main()

# def main():
#     items = list(map(int,input().split()))
#     overall = partial = items[0]
#     for i in range(1,len(items)):
#         partial = max(items[i],partial+items[i])
#         overall = max(partial,overall)
#     print(overall)
# if __name__=='__main__':
#     main()


# items1 = list(map(lambda x:x**2,filter(lambda x:x%2,range(1,10))))
# items2 = [x**2 for x in range(1,10) if x%2]

# import time
# def record_time(func):
#     """自定义装饰函数的装饰器"""
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         print(f'{func.__name__}:{time.time()-start}')
#         return result
#     return wrapper


# from functools import wraps
# from time import time
# def record(output):
#     def decorate(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             start = time()
#             result = func(*args,kwargs)
#             output(func.__name__,time()-start)
#             return result
#         return wrapper
#     return decorate


# from functools import wraps
# import time
# class Record():
#     def __init__(self,output):
#         self.output = output
#     def __call__(self, func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             start = time.time()
#             result = func(*args,**kwargs)
#             self.output(func.__name__,time.time()-start)
#             return result
#         return wrapper
# # 自定义输出函数
# def my_print(name, t):
#     print(f"【运行结束】函数：{name}，耗时：{t:.4f} 秒")
#
# # 用类装饰器
# @Record(my_print)
# def test():
#     time.sleep(1)
#
# test()


# from functools import wraps
#
# def singleton(cls):
#     instances={}
#     @wraps(cls)
#     def wrapper(*args,**kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args,**kwargs)
#         return instances[cls]
#     return wrapper
# @singleton
# class President:
#     pass



# from functools import wraps
# from threading import RLock
# def singleton(cls):
#     instances={}
#     locker = RLock()
#     @wraps(cls)
#     def wrapper(*args,**kwargs):
#         if cls not in instances:
#             with locker:
#                 if cls not in instances:
#                     instances[cls] = cls(*args,**kwargs)
#         return instances[cls]
#     return wrapper
# @singleton
# class President:
#     pass




