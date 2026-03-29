# #1.随机密码生成器
# import random,string
# length = int(input('请输入密码长度'))
# chars = string.ascii_letters + string.digits +'!@#$%^&*'
# password = ''.join(random.choice(chars) for _ in range(length))
# print(password)


# 2. 猜数字游戏
# import random
# flag=1
# count = 0
# num = random.randrange(1,101)
# while flag:
#     x = int(input('请输入'))
#     count+=1
#     if x == num:
#         print('猜对了')
#         flag=0
#     elif x<num:
#         print('猜小了')
#     else:
#         print('猜大了')
#     print()
# print(f'猜了{count}次')

# 3. 温度转换器（℃ ↔ ℉）
# mode = int(input('请选择模式(0表示摄氏度转华氏摄氏度，1表示华氏摄氏度转摄氏度)'))
#
# tem = int(input('请输入温度:'))
# if mode == 0:
#     print(tem*9/5+32)
# else:
#     print((tem-32)*5/9)
# 4. 简易计算器
import string
cal = input('请输入')
sign=''
for i in range(len(cal)):
    if cal[i] not in string.digits:
        sign = cal[i]
        break
if sign == '+':
    num1,num2=cal.split('+')
    print(f'{int(num1)}+{int(num2)}={int(num1)+int(num2)}')
elif sign == '-':
    num1, num2 = cal.split('-')
    print(f'{int(num1)}-{int(num2)}={int(num1)-int(num2)}')
elif sign == '*':
    num1, num2 = cal.split('*')
    print(f'{int(num1)}*{int(num2)}={int(num1) * int(num2)}')
elif sign == '/':
    num1, num2 = cal.split('/')
    try:
        result = int(num1)/int(num2)
        print(f'{int(num1)}/{int(num2)}={result}')
    except ZeroDivisionError:
        print('除数不能为0')
