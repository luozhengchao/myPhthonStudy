print("hello world")

day = (1, 2, 3)
year = [range(2000, 2019)]

if day[1] < 10:
    print('%s > 10', day[1])
else:
    print(str(day[1] < 10))

import time

print(time.time())

# while 测试
# sum = 1
# # while True:
# #     print(filter(sum,day))
# #     sum = sum + 1
# #     if sum > 10:
# #         break

# 字符串基本操作：：，+ ，*
# 序列：列表，字符串，元组
chanise_a = "狗猪鼠牛虎兔龙蛇马鸡"
print(chanise_a[1:4])
print('鸡' in chanise_a)
print(chanise_a + "haah")
print(chanise_a * 2)

# 列表
a_list = ['a', 'b', 'c']
a_list.append('1')
print(a_list)
a_list.remove('a')
print(a_list)

