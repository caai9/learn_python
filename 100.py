                # day5
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
items = dict(zip('ABCDE','12345'))
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