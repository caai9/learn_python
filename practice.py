#随机密码生成器
import random,string
length = int(input('请输入密码长度'))
chars = string.ascii_letters + string.digits +'!@#$%^&*'
password = ''.join(random.choice(chars) for _ in range(length))
print(password)