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
# # 4. 简易计算器
# import string
# cal = input('请输入')
# sign=''
# for i in range(len(cal)):
#     if cal[i] not in string.digits:
#         sign = cal[i]
#         break
# if sign == '+':
#     num1,num2=cal.split('+')
#     print(f'{int(num1)}+{int(num2)}={int(num1)+int(num2)}')
# elif sign == '-':
#     num1, num2 = cal.split('-')
#     print(f'{int(num1)}-{int(num2)}={int(num1)-int(num2)}')
# elif sign == '*':
#     num1, num2 = cal.split('*')
#     print(f'{int(num1)}*{int(num2)}={int(num1) * int(num2)}')
# elif sign == '/':
#     num1, num2 = cal.split('/')
#     try:
#         result = int(num1)/int(num2)
#         print(f'{int(num1)}/{int(num2)}={result}')
#     except ZeroDivisionError:
#         print('除数不能为0')

# class Solution(object):
#     def distributeCandies(self, candies, num_people):
#         """
#         :type candies: int
#         :type num_people: int
#         :rtype: List[int]
#         """
#         ans = [0]*num_people
#         num = 1
#         while candies>0:
#             for i in range(num_people):
#                  # if cnt == num_people and num < candies:
#                 if num<=candies :
#                     ans[i]+=num
#                     candies-=num
#                     num+=1
#                 else:
#                     ans[i]+=candies
#                     candies=0
#                     break
#         return ans
# candies = int(input('candies='))
# num_people = int(input('num_people='))
# s1 =Solution()
# ans=s1.distributeCandies(candies,num_people)
# print(ans)
import bisect

class ExamTracker(object):

    def __init__(self):
        self.score = dict()
        self.total_score = 0

    def record(self, time, score):
        self.score[time] = score

    def totalScore(self, startTime, endTime):
        ss = sorted(self.score)
        self.total_score = 0

        for key in ss:
            if endTime >= key >= startTime:
                self.total_score += self.score[key]

        return self.total_score

class ExamTracker(object):

    def __init__(self):
        self.time = []
        self.score = []
        self.total_score = [0]
    def record(self, time, score):
        """
        :type time: int
        :type score: int
        :rtype: None
        """
        idx = bisect.bisect_left(self.time,time)
        self.time.insert(idx,time)
        self.score.insert(idx,score)
        self.total_score.append(self.total_score[-1]+score)
    def totalScore(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        idx1 = bisect.bisect_left(self.time,startTime)#查询合适位置并返回索引
        idx2 = bisect.bisect_right(self.time,endTime)
        totalss = self.total_score[idx2]-self.total_score[idx1]
        return totalss


import os
import sys
import json
# import re
from datetime import datetime
# phone_pattern = re.compile

class Solution(object):
    def countFancy(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """

        def is_fancy(n):
            num = str(n)
            is_decrease = True
            is_increase = True
            if n < 10:
                return True
            for i in range(1, len(num)):
                if num[i] <= num[i - 1]:
                    is_increase = False
                    break
            for i in range(1, len(num)):
                if num[i] >= num[i - 1]:
                    is_decrease = False
                    break
            return is_decrease or is_increase

        def sum_good(n):
            return sum(int(cn) for cn in str(n))

        cnt = 0
        for i in range(l, r + 1):
            bool1 = is_fancy(i)

            if bool1 == True:
                cnt += 1
            else:
                if is_fancy(sum_good(i)):
                    cnt += 1

        return cnt









                    #桶算法和滑动窗口
    #1.
# if valuediff<0:
#     return False
# bucket = {}
# bucket_size = valuediff +1
# for i ,num in enumerate(nums):
#     key = num//bucket_size
#     if key in bucket:
#           return True
#     if key-1 in bucket and abs(num-bucket[key-1])<=valuediff:
#              return True
#     if key+1 in bucket and abs(num-bucket[key+1])<=valuediff:
#              return True
#     bucket[key] = num
#     if i>=indexdiff:
#          del bucket[nums[i-indexdiff]//bucket_size]
# return False

    # 2.
def ccc(nums, k):
    bucket = set()
    for i, num in enumerate(nums):
        # key = num//1
        if num in bucket:
            return True
        bucket.add(num)
        if i >= k:
            bucket.remove(num[i - k])
    return False




p = [1,3,4,3,5534,3]
# p.remove(3)
del p[1]
print(p)


class Solution(object):
    def numRescueBoats(self, people, limit):
        cnt = 0
        # 换成系统快排，直接过
        people.sort(reverse=True)  # 重的在前

        i = 0
        j = len(people)-1

        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
            cnt += 1

        return cnt